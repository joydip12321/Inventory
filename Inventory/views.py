from django.shortcuts import render,redirect
from django.http import HttpResponse
from Inventory.models import *
from django.contrib import messages

# Create your views here.
def loginInventory(request):       
    return render(request,"login_page.html")

def registration(request):
    return render(request,"registration.html")

def sellerReg(request):
    if request.method=="POST":
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            username=request.POST.get('username')
            email=request.POST.get('email')
            # phone_no=request.POST.get('phone_no')
            # address=request.POST.get('address')
            password=request.POST.get('password')
            
            user=User.objects.filter(username=username)
            if user.exists():
                messages.info(request, "Username already taken")
                return redirect('/sellerReg/')
            
            user=User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
               
                
            )
            # authenticate=Authenticate.objects.create(
            #      phone_no=phone_no,
            #     address=address,
            # )
            user.set_password(password)
            user.save()
            # authenticate.save()
            messages.info(request, "Accout Created Successfully")
            return redirect('/')
        
    return render(request,"seller_registration.html")

def customerReg(request):
    return render(request,"customer_registration.html")