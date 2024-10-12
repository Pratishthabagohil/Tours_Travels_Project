from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    place = models.CharField(max_length=100)
    number_of_persons = models.IntegerField()
    departure_date = models.DateField()
    return_date = models.DateField()
    transportation_method = models.CharField(max_length=10, choices=[('Flight', 'Flight'), ('Train', 'Train')])
    
    def __str__(self):
        return f"Inquiry from {self.name} for {self.place}"

class Location(models.Model):
    line = models.TextField(null=True)
    Cname = models.CharField(max_length=255,default="India") 
    name = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=255)
    age_group = models.CharField(max_length=255)
    altitude = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    includes = models.JSONField()  # To store a list of inclusions
    about = models.TextField()
    image = models.CharField(max_length=255) 
    brochure = models.FileField(upload_to='brochures/', null=True, blank=True)
    backimage = models.CharField(null=True,max_length=255) 
    
    def __str__(self):
        return self.name
