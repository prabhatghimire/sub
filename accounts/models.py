from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from .managers import UserManager


# Create your models here.


BLOOD_CHOICES = (
    ('O-', 'O-'),
    ('O+', 'O+'),
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
)


class Location(models.Model):
     district = models.CharField(max_length=140)
     municipality = models.CharField(max_length=140, unique=True)

     class meta:
         fields = ['district', 'municipality']
         unique_together = (('district', 'municipality'),)

     def __str__(self):
         return self.district + ', ' + self.municipality


class User(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)
    address = models.ForeignKey(
        'Location', default=1, on_delete=models.PROTECT)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    middle_name = models.CharField(max_length=140, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    phone = models.CharField(max_length=10)
    bloodgroup = models.CharField(max_length=5, choices=BLOOD_CHOICES)
    last_donate_date = models.DateField(default='2017-01-01')
    donation_no = models.IntegerField(null=True, default=0)

    objects = UserManager()  # This is the new line in the User model. ##

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.first_name == '':
            return self.email
        else:
            return self.first_name+' '+self.last_name

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
