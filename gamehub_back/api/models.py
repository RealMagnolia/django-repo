from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Game(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    is_active = models.BooleanField()
    author = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


# class Manager(AbstractUser):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)