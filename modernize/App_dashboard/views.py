from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# @login_required(login_url="/login")
class Dashboard(LoginRequiredMixin, View):
    template_name = "dashboard.html"
    login_url = '/login'

    def get(self, request):
        print(request.user.is_authenticated,"request.user.is_authenticated")
        return render(request, self.template_name)

    def post(self, request):
        pass