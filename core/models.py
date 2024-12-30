from  django.db import models
from django.contrib.auth.models import User, AbstractUser

from django.template.context_processors import media
User_type=(
     ('Admin', 'Admin'),
     ('Tenants', 'Tenants'),
      ('Landroad', 'Landroad'),
 )

class User(AbstractUser):
    user_type = models.CharField(choices=User_type, default='Tenants',max_length=100)
    pass
    def __str__(self):
        return f"{self.username}-{self.last_name}"
class Contact_User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.message}"
class Signup(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=200)
    birth_date = models.DateField()
    password = models.CharField(max_length=100)
    user_type = models.CharField(choices=User_type, default='Tenants',max_length=100)
    def __str__(self):
        return f"{self.email} - {self.first_name} - {self.last_name}-{self.email}- {self.birth_date}"





