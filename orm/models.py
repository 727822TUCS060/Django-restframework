from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=3)
    is_active =models.BooleanField(default=True)
    joined_date =models.DateField(auto_now_add=True ,null=True)

    def __str__(self):
        return self.name
class Author(models.Model):
    name=models.CharField(max_length=100)
class Book(models.Model):
    title = models.CharField(max_length=100)
    author=models.ForeignKey(Author , on_delete=models.CASCADE ,related_name='books',null=True)
    #author=models.CharField(max_length=100 , null=True)
    published_year=models.IntegerField(default=0)
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.user.username
    