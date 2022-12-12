import re
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

class ServiceTypes(models.Model):
    service = models.CharField(max_length=250)
    quote = models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer gravida mauris non mi gravida, at sollicitudin.')
    service_image = models.ImageField(upload_to='service_images/', default='service_images/default.jpg')
    
    def __str__(self):
        return self.service
    class Meta:
        verbose_name_plural = 'Service Types'

class Enquiry(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=255, blank=False)
    mobile_number = models.CharField(max_length=10)
    # Override the clean method and check the number is in correct format
    def clean(self):
       if not re.match(r'^\d{10}$', self.mobile_number):
           raise ValidationError('Invalid mobile number')
    address = models.TextField()
    select_service = models.ForeignKey(ServiceTypes, on_delete=models.CASCADE)
    service_status = models.BooleanField(default=False)
    enquiry_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Enquiries'
        
    def __str__(self):
        return self.name
    
    
class ContactInfo(models.Model):
    email = models.EmailField(max_length=255)

    mobile_number = models.CharField(max_length=10)
    # Override the clean method and check the number is in correct format
    def clean(self):
       if not re.match(r'^\d{10}$', self.mobile_number):
           raise ValidationError('Invalid mobile number')

    telephone_number = models.CharField(max_length=15)
    def clean(self):
       if not re.match(r'^\d{10}$', self.mobile_number):
           raise ValidationError('Invalid mobile number')
    address = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Owner Contact Info'
        
    def  __str__(self):
        return self.email
    
    
class Newsletter(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    
    def __str__(self):
        return self.email
    
    
class Team(models.Model):
    image = models.ImageField(upload_to='team_images')
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()
    
    

class ClientQuotes(models.Model):
    image = models.ImageField(upload_to='client_images')
    name = models.CharField(max_length=255)
    text = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Client Quotes'
    def __str__(self):
        return self.name
    
    
# Tag model for project related tagging
class Tag(models.Model):
    tag = models.CharField(max_length=255)
    
    def __str__(self):
        return self.tag
    

# Project model for storing images of all our work
class Project(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    project_images = models.ImageField(upload_to='project_images')
    
    def __str__(self):
        return self.tag.tag
    
    
class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    