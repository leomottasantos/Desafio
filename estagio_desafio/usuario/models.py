from django.contrib.auth.models import User
from django.db import models

class Usuario(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  email = models.EmailField(unique=True)


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField(blank=True)
    

  def __str__(self):
        return self.user.username