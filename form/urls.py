from . import views
from django.urls import path

urlpatterns = [
    path('', views.form),
    path('ty/', views.ty)
]