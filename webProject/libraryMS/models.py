from django.db import models
from django.contrib.auth import password_validation
from django.contrib.auth.models import AbstractUser
from django.conf import settings
#from django.utils.timezone import datetime
from datetime import datetime  
from datetime import timedelta
import uuid

# Create your models here.

#User._meta.get_field('email')._unique = True



class User(AbstractUser):
    is_library_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    password1 = models.CharField(max_length=30, default='') #help_text=password_validation.password_validators_help_text_html
    password2 = models.CharField(max_length=30, default='')
    image = models.ImageField(upload_to='Images/users', null=True, blank=True)
    

    AbstractUser._meta.get_field('email')._unique = True
    AbstractUser.REQUIRED_FIELDS = ['username', 'password']
    AbstractUser.USERNAME_FIELD = 'email'



class Library_admin(models.Model):
    user = models.OneToOneField(User, on_delete = models.PROTECT, primary_key = True)
    books = models.ManyToManyField(to='Book')

    def __str__(self):
        email = self.user.email
        return email




class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.PROTECT, primary_key = True)
    books = models.ManyToManyField(to='Book')

    def __str__(self):
        email = self.user.email
        return email
    



class Book(models.Model):
    book_status=[
        ('available', 'available'),
        ('unavailable', 'unavailable')
    ]
    isbn = models.CharField('ISBN', max_length=13, unique=True, primary_key=True, default='')
    Title = models.CharField(verbose_name='Title' ,max_length=60)
    Author = models.CharField(max_length=30, null=True, blank=True)
    Price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, default=0.00)
    image = models.ImageField(upload_to='images/books', null=True, blank=True)
    status = models.CharField(max_length=30, choices=book_status, default='available')
    active = models.BooleanField(default=True , null=True, blank=True)
    #Duration =


    def __str__(self):
        return self.Title


    class Meta:
        managed =True
        constraints = [
            models.CheckConstraint(check=models.Q(Price__gte='0.01'), name='product_price_non_negative'),
        ]


class BorrowingPeriod(models.Model):
    afterDays = datetime.now() + timedelta(days=7)

    student = models.ForeignKey(to='Student', on_delete=models.PROTECT, null=True, blank=True)
    book = models.ForeignKey(to='Book', on_delete=models.PROTECT, null=True, blank=True)
    period = models.DateField(default=afterDays)

    def __str__(self):
        return self.student.user.email
