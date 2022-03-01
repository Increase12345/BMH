from . import views
from django.urls import path
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.form),
    path('ty/', views.ty),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('login/content_user/', views.conten),
]