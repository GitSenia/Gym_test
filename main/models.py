from django.db import models

# Create your models here.

class Equipment(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)     # категория (кардио, силовой, функциональный)
    description = models.TextField(blank=True, null=True)  # описание (для чего предназначен)
    image = models.ImageField(upload_to="equipment/", blank=True, null=True)  # фото тренажёра
    image_muscles = models.ImageField(upload_to="equipment/", blank=True, null=True)  # фото тренажёра
    manufacturer = models.CharField(max_length=150, blank=True, null=True)    # производитель (Life Fitness, Technogym...)
    condition = models.CharField(
        max_length=50,
        choices=[("new", "Новый"), ("good", "Хорошее"), ("repair", "Требует ремонта")],
        default="good"
    )  # состояние
    is_active = models.BooleanField(default=True)      # используется ли сейчас в зале
    def __str__(self):
        return self.name

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=100)
    description=models.TextField()
    image=models.FileField(upload_to='services_images/',blank=True,null=True)
    slag=models.CharField(max_length=50)
    def __str__(self):
        return self.name

