from django.contrib import admin
from .models import Services,Business,TimeTable,Reserves,Review,Categories,Sans

admin.site.register(Services)
admin.site.register(Business)
admin.site.register(TimeTable)
admin.site.register(Review)
admin.site.register(Reserves)
admin.site.register(Categories)
admin.site.register(Sans)