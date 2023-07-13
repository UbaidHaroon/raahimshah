from django.shortcuts import render,HttpResponse
from home.models import Contact

# Create your views here.
def index(request):
    context={
        "variable":"this is sent"
    }
    return render(request,'index.html')
    #return HttpResponse("this is home page")

# def home(request):
#       return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return HttpResponse("this is Services page")

def contacts(request):

    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone= request.POST.get('phone')
        contacts=Contact(name =name,email=email,phone=phone)
        contacts.save()

    return render(request,'contact.html')