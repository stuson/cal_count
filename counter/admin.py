from django.contrib import admin
from .models import (
    Food,
    FoodInstance,
    FoodTag,
)

admin.site.register(Food)
admin.site.register(FoodTag)
admin.site.register(FoodInstance)