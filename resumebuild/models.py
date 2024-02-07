from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
class UserResume(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    projects = models.ManyToManyField(Project)