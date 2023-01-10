from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('detail/<int:id>/', views.post_detail),
]