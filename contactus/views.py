from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage, Contactus
from .forms import ContactForm

# Create your views here.
def contact_us(request):
    """
    Renders the Contactus page
    """

    if request.method == "POST":
        print("Received a POST request")
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Thank you for your message, we will get back to you as soon as possible.")
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
