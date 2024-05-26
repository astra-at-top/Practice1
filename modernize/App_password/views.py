from django.shortcuts import render
from .forms import PasswordForm
from .models import PasswordModle
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers


class PassworsView(LoginRequiredMixin,View):
    template_name = "password.html"
    login_url = '/login'

    def get(self, request):
        try:
            passwordForm = PasswordForm()
            allData = PasswordModle.objects.all()
            if "action" in request.GET:
                action = request.GET.get("action")
                if action == "filter":
                    return self.__fetchData(request)
                
                return JsonResponse({
                    "msg" : "Successfully handled "
                })
            else:    
                return render(request,self.template_name,{
                    "form" : passwordForm,
                    "password_data" : allData
                })
        except Exception as e:
            print(e)
            return JsonResponse({
                "error_msg": "Something went wrong"
            }, status=400)

    def post(self, request, *args, **kwargs):
        try:
            action = request.POST.get("action")
            if action:
                if action == "add_data":
                    return self.__addPassword(request)
                if action == "update_data":
                    return self.__upadtePassword(request)
                if action == "delete_data":
                    return self.__deleteData(request)
                else:
                    return JsonResponse({
                        "err_msg" : "This view is under constructions"
                    })
            else:
                return JsonResponse({
                    "err_msg" : "No action found"
                })    
        except Exception as e :
            return JsonResponse({
                    "err_msg" : " Something went wrong "
                })
    
    def __deleteData(self, request):
        print("delete", request.POST)
        id = request.POST.get("id")
        if id :
            getData = PasswordModle.objects.get(id=id)
            if getData:
                getData.delete()
                return JsonResponse({
                    "success_msg" : "Data deleted successfully",
                    "action" : "reload_page"
                })
            else:
                return JsonResponse({
                    "error_msg" : "Wrong data",
                }, status=500)    
        else:
            return JsonResponse({
                "error_msg" : "No id found"
            }, status=500)
        
   
   
    # update the data
    def __upadtePassword(self, request):
        try:
            pk = request.POST.get("pk")
            if pk : 
                data = PasswordModle.objects.get(pk=pk)
                website = request.POST.get("website")
                username  = request.POST.get("username")
                password  = request.POST.get("password")
                remarks  = request.POST.get("remarks")
                if data and website and username and password and remarks :
                    data.website = website
                    data.username = username
                    data.password = password
                    data.remarks = remarks
                    data.save()
                    return JsonResponse({
                        "success_msg" : "Data upadted successfully",
                        "action" : "reload_page"
                    })
                else:
                    return JsonResponse({
                        "error_msg" : "Enter valid data"
                    }, status=500)
            else:
                return JsonResponse({
                    "error_msg" : "No id found"
                }, status=500)
            return JsonResponse({
                "msg" : "UPdate message"
            })
        except:
            pass    
 
    # delete the data


    # this fuction will add the password data
    def __addPassword(self,req):
        form = PasswordForm(req.POST)
        if form.is_valid():
            website =  req.POST.get("website")
            if PasswordModle.objects.filter(website=website).exists():
                return JsonResponse({
                    "err_msg": "Website already exists"
                })
            else:
                form.save()
                return JsonResponse({
                    "success_msg" : "Record saved successfully",
                    "action" : "reload_page"
                })
        else:
            return JsonResponse({
                "err_msg" : "Enter proper Data"
            }) 
    
    #  filter out the certain 
    def __fetchData(self, request):
        id = request.GET.get("id")
        if id:
            data = PasswordModle.objects.filter(id=id).values("website", "username" ,"password" ,"remarks")
            if data : 
                data = list(data)
                return JsonResponse({
                    "success_msg" : "Data fetched successfully",
                    "data" : data[0]
                })
            else:
                return JsonResponse({
                    "err_msg" : "Enter valid data "
                })
        else:
            return JsonResponse({
                "err_msg" : "Enter the id"
            }, status=500)