from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Food(models.Model):
    name = models.CharField(max_length=60, primary_key=True)
    created_by = models.ForeignKey(User, null=True, related_name='created_by', on_delete=models.SET_NULL)
    last_modified_by = models.ForeignKey(User, null=True, related_name='last_modified_by', on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    energy = models.DecimalField(max_digits=6, decimal_places=2, null=False) # kcal / 100g
    carbohydrate = models.DecimalField(max_digits=5, decimal_places=2, null=False) # kg / 100g
    protein = models.DecimalField(max_digits=5, decimal_places=2, null=False) # g / 100g
    fat = models.DecimalField(max_digits=5, decimal_places=2, null=False) # g / 100g
    fibre = models.DecimalField(max_digits=5, decimal_places=2, null=False) # g / 100g
    sodium = models.DecimalField(max_digits=4, decimal_places=2, null=False) # g / 100g

    def __str__(self):
        return self.name

class FoodTag(models.Model):
    tag = models.CharField(max_length=20, primary_key=True)
    food = models.ManyToManyField(Food)

    def __str__(self):
        return self.tag

class FoodInstance(models.Model):
    food = models.ForeignKey(Food, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    amount = models.IntegerField() # g

    def __str__(self):
        return f'{self.food} - {self.date}'