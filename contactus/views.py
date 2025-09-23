from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage, Contactus
from .forms import ContactForm


# Create your views here.
def contact_us(request):
    """
    A view to return the contact us page and handle the form
    submission.
    1. If the request method is POST, it processes the submitted form data.
    2. If the form is valid, it saves the form data to the database,
        displays a success message, and redirects to the contact us page.
    3. If the request method is not POST, it retrieves the latest Contactus
        instance and initializes an empty ContactForm.
    4. Finally, it renders the contact us page with the contact information
        and the contact form.
    5. The view uses Django's messages framework to provide feedback to the user.
    6. The contact us page is rendered using the 'contactus/contactus.html'
        template.
    7. The Contactus model is used to store and retrieve contact information,
        while the ContactForm is used to handle user submissions.
    8. The view is accessible via the URL pattern named 'contactus'.
    9. The contact form includes fields for the user's name, email, subject,
        and message.
    10. The view ensures that the contact form is always available on the
        contact us page, regardless of whether the form has been submitted or
        not.
    11. The latest Contactus instance is determined by ordering the instances
        by the 'updated_on' field in descending order and selecting the first
        instance.
    12. The view handles both GET and POST requests, making it versatile for
        displaying the form and processing submissions.
    13. The success message is displayed using Django's messages framework,
        which allows for easy integration with the template to show feedback
        to the user.
    14. The view is designed to be user-friendly, providing clear feedback and
        ensuring that the contact form is always accessible.
    """

    if request.method == "POST":
        print("Received a POST request")
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(
                request,
                """Thank you for your message,
                we will get back to you as soon as possible.""")
            return redirect("contactus")

    contactus = Contactus.objects.all().order_by('-updated_on').first()

    contact_form = ContactForm()

    return render(
        request,
        "contactus/contactus.html",
        {
            "contactus": contactus,
            "contact_form": contact_form,
        },
    )
