from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    # Chosen to show 6 per page for user readability and flex design
    paginate_by = 6
    
    
def post_detail(request, slug):
    """
    Display one :model:`blog.Post` by slug.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    
    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )