from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage, Contactus

# Create your views here.
def contact_us(request):
    """
    Renders the Contactus page
    """
    contactus = Contactus.objects.all().order_by('-updated_on').first()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("enquiry")
        ContactMessage.objects.create(name=name, email=email, message=message)
        messages.success(request, "Thank you for your message, we will get back to you as soon as possible.")
        return redirect("contactus")
    return render(
        request,
        "contactus/contactus.html",
        {"contactus": contactus},
    )
