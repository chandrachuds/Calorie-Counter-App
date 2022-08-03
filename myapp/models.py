from django.db import models
#Inbuilt User model in django
from django.contrib.auth.models import User
# Create your models here.

class food(models.Model):
    def __str__(self):
        return self.name
    # Macronutrients
    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    calories = models.IntegerField()

class Consume(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # Foreign key = Pirmary key of food models
    food_consumed = models.ForeignKey(food,on_delete=models.CASCADE)
    