from django.urls import path
from . import views

urlpatterns = [
    path('animal_list/', views.animal_list, name='animal_list'),
    path('profile/<int:id>/', views.animal_profile),
    path('create_page/', views.create_page),
]
