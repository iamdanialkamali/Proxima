from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Zanbil import views,BusinessPageController , editServiceController
from Zanbil import BusinessSelectPageController,AccountPageController,ServicePageController,SearchController
from Zanbil import dashboardController,addAndDeleteBusinessController,editServiceController

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
    path('editSans/<int:sans_id>/<int:service_id>', editServiceController.editsans, name='editSans'),
    path('buildTimeTable/<int:service_id>', editServiceController.buildTimeTable , name = 'buildTimeTable')

]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)