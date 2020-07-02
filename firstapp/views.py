from django.shortcuts import render
from django.http import HttpResponse
from firstapp.forms import FormName
from .models import Topic,Webpage,AccessRecord,InputUser
# Create your views here.
def first(request):
    return render(request,'firstapp/first.html')
def relativetemplate(request):
    return render(request,'firstapp/relativetemplate.html')
def contact(request):
    return render(request,'firstapp/contact.html')
def aboutus(request):
    return render(request,'firstapp/aboutus.html')
def service(request):
    return render(request,'firstapp/service.html')
def index(request):
    field_list=InputUser.objects.order_by('name')
    name_list=AccessRecord.objects.order_by('name')#not compulsory to put request you can put anything
    my_dict={'field_records':field_list,'access_records':name_list}
    return render(request, 'firstapp/index.html',context=my_dict)
def form_name(request):
    form=FormName()
    if request.method == "POST":
        form=FormName(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error form is invalid')
    return render(request,'firstapp//form_page.html',{'form':form})