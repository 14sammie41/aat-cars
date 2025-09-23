from django.contrib import admin
from .models import Contactus, ContactMessage
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Contactus)
# This model is designed to connect the contact us form to the admin
# interface. It uses SummernoteModelAdmin to make it more user friendly.
class ContactusAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

admin.site.register(ContactMessage)
