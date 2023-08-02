from django.shortcuts import render

# Create your views here.
from django.views.generic import View,TemplateView
from app.forms import *
from django.http import HttpResponse
class data_render(View):
    def get(self,request):
        d={'name':'ASHU'}
        return render(request,'data_render.html',d)

def insert_fbv(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('Data is Inserted')
    return render(request,'insert_fbv.html',d)


class cbv_insert(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'cbv_insert.html',d)
    
    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
        return HttpResponse('cbv_insert')


class temp(TemplateView):
    template_name='temp.html'




