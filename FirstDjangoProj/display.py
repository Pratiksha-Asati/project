from django.shortcuts import render
def home(request):
    return  render(request,'form.html')

def about(request):
    return render(request,'about.html')

def contactUs(request):
    return render(request,'contactUs.html')

def index(request):
    return render(request,'index.html')


