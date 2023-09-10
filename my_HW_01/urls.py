from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main_page, name='main_page'),
    path('about_me/', views.about_me, name='about_me')
]
