from django.db import models

# Create your models here.
class tablemodel(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.TextField()
    number=models.IntegerField()
    image=models.ImageField(blank=True,upload_to='imgs')
