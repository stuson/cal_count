from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.models import User
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

    def get_queryset(self):
        return FoodInstance.objects.filter(user=self.request.user)