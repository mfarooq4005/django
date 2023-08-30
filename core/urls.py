"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin-panel/', admin.site.urls, name="admin"),
    path('aboutus/', views.about_us, name="about"),
    path('contact/', views.contact, name="contact"),
    path('', views.homePage, name="home"),
    path('service/', views.service, name="service"),
    path('shop/', views.shop, name="shop"),
    path('form/', views.form, name="form"),
    path('form_data/', views.form_data, name="form_data"),
    path('contact_data/', views.contact_data, name="contact_data"),
    path('calculator/', views.calculator, name="calculator"),
    path('evenodd/', views.evenodd, name="evenodd"),
    path('sheet/', views.sheet, name="sheet"),
]