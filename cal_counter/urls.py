from django.contrib import admin
from django.urls import path
from counter import views as counter_views

urlpatterns = [
    path('food/<pk>', counter_views.FoodDetailView.as_view(), name='food_detail'),
    path('', counter_views.MyFoodInstancesListView.as_view(), name='home'),
    path('admin/', admin.site.urls),
]
