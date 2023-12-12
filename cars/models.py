from django.db import models

# Create your models here.
class users(models.Model):
    first_name=models.CharField(max_length=122)
    last_name=models.CharField(max_length=122)
    email=models.CharField(max_length=152)
    username=models.CharField(max_length=122)
    password=models.CharField(max_length=150)

    def __str__(self):
        return self.first_name
        