from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Portfolio
from portfolio.models import MainImage
 
 

# Create your views here.

def home(request):
    list_object=Portfolio.objects.all()
    top_img=MainImage.objects.all()
     
    params={"objects":list_object,'main':top_img}
    return render(request,"portfolio/index.html", params)
