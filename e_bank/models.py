

from django.db import models

# Create your models here.
class Ways(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='ways',blank=True)

    def __str__(self):
        return '{}'.format(self.name)

# class Contact(models.Model):
#     name = models.CharField(max_length = 150)
#     email = models.EmailField()
#     message = models.TextField()