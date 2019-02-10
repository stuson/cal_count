from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from .models import (
    Food,
    FoodInstance,
    FoodTag
)

class MyFoodInstancesListView(ListView):
    model = FoodInstance
    context_object_name = 'foodInstances'
    paginate_by = 5
    template_name = 'counter/home.html'

    def get_queryset(self):
        return FoodInstance.objects.filter(user=self.request.user).order_by('-date')

class FoodDetailView(DetailView):
    model = Food
    template_name = 'counter/food_detail.html'