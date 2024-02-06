from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
