from django.contrib import admin
from .models import Contactus, ContactMessage
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Contactus)
class ContactusAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

admin.site.register(ContactMessage)
