from django.shortcuts import render, redirect
from django.contrib import messages
from storedetails.models import userdetails

# Create your views here.
def index(request):
    return render(request, 'index.html')

def name(request):
    if request.method == 'POST':
        Name = request.POST['name']
        Phone  = request.POST['phonenumber']
        Cv   = request.POST['cv']
        email      = request.POST['email']
        website  = request.POST['websiteaddress']

        if Cv is None or Cv == "":
            messages.info(request, 'CV Manditory')
            return redirect('/')

    user = userdetails(Name= Name,Phone=Phone,Cv=Cv,email=email,website=website)
    user.save();

    # return redirect('login')
    return render(request, 'name.html',{'result':{'name':request.POST['name'],'phonenumber':request.POST['phonenumber'],'cv':request.POST['cv'],'email':request.POST['email'],'webaddress':request.POST['websiteaddress']}})