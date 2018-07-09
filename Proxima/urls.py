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
from Zanbil import views,BusinessPageController,BusinessSelectPageController,AccountPageController,ServicePageController,SearchController

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('Businesses/<int:category_id>', BusinessSelectPageController.BusinessSelectPage.Render, name='Businesses'),
    path('account/<int:user_id>', AccountPageController.AccountPageController.Render, name='account'),
    path('ServicePage/<int:service_id>', ServicePageController.ServicePageController.Render, name='ServicesPage'),
    path('BusinessPage/<int:business_id>', BusinessPageController.BusinessPageController.Render, name='BusinessPage'),
    path('business/',SearchController.SearchController.Search , name='search'),
    path('ServicePage/timetable/', ServicePageController.ServicePageController.RenderTimeTable, name='timetable'),
    path('book/', ServicePageController.ServicePageController.Book, name='book'),
    path('comment/<int:id>/', BusinessPageController.comment, name='comment'),
    path('createBusiness/<int:id>',AccountPageController.createBusiness,name='createBusiness'),
    path('test',views.test),
    path('dashboard/<int:business_id>',dashboardController.render_dashboard , name='dashboard'),
    path('changePhoto/<int:id>',dashboardController.changePhoto,name='changePhoto'),
    path('test/<int:id>',views.imagetest,name='imagetest'),
    path('addService/<int:business_id>',dashboardController.addService,name="addService"),
    path('editService/<int:service_id>',editServiceController.Render,name='editServicePage') ,
    path('addBusiness',addAndDeleteBusinessController.addBusiness,name = 'addBusiness'),
    path('deleteSans/<int:sans_id>/<int:service_id>',editServiceController.deleteSans,name='deleteSans'),
    path('buildTimeTable/<int:service_id>', editServiceController.buildTimeTable , name = 'buildTimeTable')

]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)