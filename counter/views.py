from django.shortcuts import render
from django.views.generic import ListView
from .models import (
    Food,
    FoodInstance,
    FoodTag
)

class RecentDaysView(ListView):
    model = FoodInstance
    context_object_name = 'foods'
    paginate_by = 5
    template_name = 'counter/home.html'