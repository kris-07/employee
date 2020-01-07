from django.shortcuts import render,redirect
from .models import user
from django.contrib import messages
from django.contrib.auth.models import auth
import time

# Create your views here.
def register(req):
    try:
        if(req.method=='POST'):
            name=req.POST["full_name"]
            email=req.POST["email"]
            username=req.POST["username"]
            countrycode=req.POST["countrycode"]
            phone=req.POST["phone"]
            pincode=req.POST["pincode"]
            gender=req.POST["gender"]
            address=req.POST["address"]
            dob=req.POST["dob"]
            img=req.POST["img"]
            bio=req.POST["bio"]
            password=req.POST["password"]
            password1=req.POST["password1"]
            if(user.objects.filter(email=email).exists() ):
               return messages.error(req,'Email taken !!!')
            if(len(password)<=4):
               return messages.info(req,' password length too less')
            user1 = user(name=name,img=img,dob=dob, password=password,address=address,pincode=pincode,username=username,gender=gender,countrycode=countrycode,phone=phone, email=email, bio=bio)
            user1.save()
            print('User Created')
            return redirect('/login')
    except:
        return render(req,'register.html')
    return render(req,'register.html')


class cuid:
    id : str
uid = cuid()
def login(req):
    try:
        if(req.method=='POST'):
            email=req.POST["email"]
            password=req.POST["pass"]

            if(user.objects.filter(email=email).exists() ):
                if(user.objects.filter(password=password).exists()):

                    uid.id=user.objects.get(email=email).id

                    return redirect(("/userinfo"))
            else:
                return render(req,'login.html')
    except:
        return render(req,'login.html')
    return render(req,'login.html')


def userinfo(req):

    id = int(uid.id)
    return render(req,'userinfo.html',{'user' : user.objects.get(id=id)})