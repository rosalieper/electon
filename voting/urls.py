from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
     path('home', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]