from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
      return "User object: {} {} {} ".format(self.first_name, self.last_name,self.email)

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=255)
    uploader = models.ForeignKey(User, related_name = "uploaded_books")
    liked_users = models.ManyToManyField(User, related_name="liked_books")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __repr__(self):
      return "Book object: {} {} ".format(self.name, self.desc)
