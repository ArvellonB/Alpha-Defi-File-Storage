from django.urls import path
from . import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('dark/', views.dark, name="dark"),
    path('light/', views.light, name="light"),
    path('complete/', views.complete, name="complete"),
]