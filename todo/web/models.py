from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

# Create your models here.
class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE,default=1)
    title = models.CharField(max_length = 200)
    description = models.TextField(blank=True, null=True)
    datetime = models.DateTimeField()
    priority = models.CharField(max_length = 50, choices = [('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], default = 'medium')
    status = models.CharField(max_length = 50, choices = [('incomplete', 'Incomplete'), ('complete', 'Complete')], default = 'incomplete')








# class UserRegister(models.Model):
#     fullname = models.CharField(max_length = 100)
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=150, unique=True)  # Added username field
#     password = models.CharField(max_length = 128)
#     def save(self, *args, **kwargs):
#           if self.password:
#              self.password = make_password(self.password)
#           super().save(*args, **kwargs)
