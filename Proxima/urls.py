"""Proxima URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from Zanbil import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main,name='main'),
    path('Businesses/<int:category_id>',views.Businessesspage,name='Businesses'),
    path('beautysalon/',views.beautysalon,name='beautysalon'),
    path('cafe/',views.beautysalon,name='cafe'),
    path('doctor/',views.beautysalon,name='doctor'),
    path('hotel/',views.beautysalon,name='hotel'),
    path('resturant/',views.beautysalon,name='resturant'),
    path('account/',views.account,name = 'account'),
    path('account/createbusiness',views.createbusiness,name='createbusiness'),
    path('ServicePage/<int:service_id>',views.showservice,name = 'ServicesPage'),
    path('BusinessPage/<int:business_id>',views.showbusiness,name = 'BusinessPage'),
    path('business/',views.search,name='search'),
    path('ServicePage/timetable/',views.rendertimetable,name='timetable'),
    path('book/<int:sansId>/<str:date>',views.book,name = 'book')


]
