from django.urls import path
from firstapp import views
#Template tagging
#the application url
app_name='firstapp'
urlpatterns = [
    path('first',views.first,name='first'),
    path('',views.index,name='index'),
    path('relativetemplate',views.relativetemplate,name='relativetemplate'),
    path('formpage/', views.form_name, name='form_name'),
    path('contact',views.contact,name='contact'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('service',views.service,name='service'),
]