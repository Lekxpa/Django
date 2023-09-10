from django.urls import path
from . import views

urlpatterns = [
    path('heads/', views.heads_tails, name='heads_tails'),
    path('cube/', views.cube, name='cube'),
    path('number/', views.rand_num, name='rand_num')
]
