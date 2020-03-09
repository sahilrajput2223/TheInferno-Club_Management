from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)


class Profile(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    address = models.TextField()
    DOB = models.DateField()
    pincode = models.CharField(max_length=6)
    contact = models.CharField(max_length=10)
    profile_creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField(default='')

    def __str__(self):
        return self.name


class Bookclub(models.Model):
    email = models.EmailField()
    Amenities = models.CharField(max_length=15)
    Date = models.DateField()

    def __str__(self):
        return self.email


class Feedback(models.Model):
    email = models.EmailField()
    title = models.TextField(max_length=20)
    feedback = models.TextField()

    def __str__(self):
        return self.email
