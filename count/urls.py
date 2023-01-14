from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('like/<pk1>/', views.like, name="like"),
        path('dislike/<pk1>/', views.dslike, name="dislike"),
]
