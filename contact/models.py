from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.timezone import datetime


class Contact(models.Model):
    created_by = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    number = models.IntegerField()
    gender = models.CharField(choices=(
                              ("male", "Male"), ("female", "Female")), max_length=30)
    info = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering =['-id']