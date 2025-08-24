from django.db import models


# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=100)
    description=models.TextField()
    image=models.FileField(upload_to='images/',blank=True,null=True)
    def __str__(self):
        return self.name
