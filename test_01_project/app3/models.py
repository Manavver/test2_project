from django.db import models

# Create your models here.

class Villian(models.Model):
    Name = models.CharField(max_length=200)
    details = models.TextField()


    def __str__(self):
        return self.Name