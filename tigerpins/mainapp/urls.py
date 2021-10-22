from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('userLocations/', views.userLocations, name='userLocations'),
    path('userLocations/someLink', views.someLink, name='someLink'),
    path('accounts/signup/', views.signup, name='signup'),
]