from django.db import models

# Create your models here.
class Contactus(models.Model):
    """
    Model for the Contact Us page content
    related to the admin interface.
    """
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class ContactMessage(models.Model):
    """
    Model for storing contact messages
    related to the contact us form.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} <{self.email}>"