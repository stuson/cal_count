from pandas import DataFrame
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.db.models import Sum
from .models import (
    Food,
    FoodInstance,
    FoodTag
)

class MyFoodInstancesListView(ListView):
    model = FoodInstance
    context_object_name = 'dates'
    # paginate_by = 5
    template_name = 'counter/home.html'

    def get_queryset(self):
        user_instances = FoodInstance.objects.filter(user=self.request.user)
        dates = user_instances.values_list('date', flat=True).distinct()
        grouped_list = []
        for date in dates:
            today = user_instances.filter(user=self.request.user, date=date)
            grouped_list.append({
                'date': date,
                'foodInstances': today,
                'day_totals': DataFrame([x.totals for x in today]).sum().to_dict()
            })

        return grouped_list

class FoodDetailView(DetailView):
    model = Food
    template_name = 'counter/food_detail.html'