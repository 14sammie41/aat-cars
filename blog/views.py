from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


# Create your views here.
class PostList(generic.ListView):
    """ 
    Display all :model:`blog.Post` posts
    in descending order of creation date.
    """
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    # Chosen to show 6 per page for user readability and flex design
    paginate_by = 6


def post_detail(request, slug):
    """
    Display one :model:`blog.Post` by slug.
    Handle comment submission.
    Display comments in descending order of creation date.
    Show comment count.
    Handle comment form submission.
    ** context **
    `post`
        :model:`blog.Post` object
    `comments`
        All :model:`blog.Comment` objects related to the post
    `comment_count`
        Count of approved comments related to the post
    `comment_form`
        A form for users to leave comments
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
            print("About to render template")
            return redirect('post_detail', slug=post.slug)

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    Display and handle editing comments
    1. Ensure the comment belongs to the user
    2. Handle comment form submission
    3. Redirect to the post detail page
    4. Show success or error messages
    5. Comments are set to unapproved after editing
    6. Only POST requests are allowed
    ** context **
    `post`
        :model:`blog.Post` object
    `comment`
        :model:`blog.Comment` object
    `comment_form`
        A form for users to edit their comments
    7. Redirect to the post detail page after processing
    8. Show success or error messages using Django's messages framework
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, id=comment_id, post=post)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment updated'
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                'Error updating comment'
            )
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    View to delete comments
    """
    comment = get_object_or_404(Comment, id=comment_id, post__slug=slug)
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, id=comment_id, post=post)

        if comment.author == request.user:
            comment.delete()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment deleted'
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                'You can only delete your own comments'
            )
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
    