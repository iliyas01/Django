
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.homePage,name='home'),
    path('accounts/',include('allauth.urls')),
    path('dashboard',views.dashbo,name='dashboard'),
    path('profile/<str:pk>', views.profile, name='users-profile'),
    path('update-user',views.update,name='update-user'),




]
