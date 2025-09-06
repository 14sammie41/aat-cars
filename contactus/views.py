from django.shortcuts import render
from .models import Contactus

# Create your views here.
def contact_us(request):
    """
    Renders the Contactus page
    """
    contactus = Contactus.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "contactus/contactus.html",
        {"contactus": contactus},
    )
