from django.urls import path
from front import views


urlpatterns = [
    path('', views.home , name='home' ),
    path('about/' , views.about , name='about'),
    path('contact/' , views.contact , name='contact'),
    path('gallery/' , views.gallery , name='gallery'),
    path('properties/' , views.properties , name='properties'),
    path('service/' , views.service , name='service')

    
    
]
