from django.shortcuts import render , redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.

class Logout(View):
    def get(self, request):
        print("=========logout")
        logout(request)
        return redirect("/login")

class Login(View):
    template_name = "authentication-login.html"
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            msg = ""
            print(username, password,"=====passw")
            if not username or not password:
                msg = "Some credintials are missing"
            else:
                user = authenticate(request, username=username, password=password)
                if not user:
                    msg = "Either username or password is wrong"
                else:
                    login(request, user)
                    return redirect("/")
        
        except Exception as e:
            print(e)
            pass

        return render(request, self.template_name,{
            "msg" : msg
        })

   

class Signup(View):
    template_name = "authentication-register.html"
    
    def get(self, request):
        msg = "Fail to Signup"
        msg = None
        return render(request, self.template_name, {
            "msg" : msg
        })
    
    def post(self, request):
        try:
            msg = ""
            username = request.POST.get("username")
            password = request.POST.get("password")
            confirmpassword = request.POST.get("confirmpassword")
            if username and password and confirmpassword:
                if password != confirmpassword:
                    msg = "Password and Confirm password do not match"
                else:
                    User.objects.create_user(username=username, password=password)
                    return redirect("/login")
            else:
                msg = "Some fields are missing"
        except Exception as e:
            print(e)
            msg = "Some thing went wrong"        
        
        return render(request, self.template_name,{
            "msg" : msg
        })

