from django.shortcuts import render

# Create your views here.

from . models import Mobile


def home(request):
	obj=Mobile.objects.all()
	return render(request,'home.html',{'obj':obj})