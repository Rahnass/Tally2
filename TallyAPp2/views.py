from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def units(request):
    return render(request,'units.html')    

def currencies(request):
    return render(request,'currencies.html')      

def atten_prod(request):
    return render(request,'attend_prod.html')   

def emp_groups(request):
    return render(request,'employye_group.html')  

def employee(request):
    return render(request,'employyee.html')      