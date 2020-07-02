# Register your models here.
from django.contrib import admin
from firstapp.models import AccessRecord,Topic,Webpage,InputUser  # this line added
admin.site.register(AccessRecord)#this line added
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(InputUser)