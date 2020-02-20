from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from login.models import Logintb



class Me(View):
    def get(self,request,*args,**kwargs):
        print ("something")
        return render(request,"login.html")

    def post(self,request,*args,**kwargs):
        do=Logintb()
        do.uname=request.POST.get('username')
        do.pwd=request.POST.get('password')
        do.save()
        return HttpResponse('<b>Successfully Data Stored</b>')


me=Me.as_view()

