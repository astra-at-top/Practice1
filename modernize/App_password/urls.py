from django.urls import path
from .views import PassworsView

urlpatterns = [
    path("password", PassworsView.as_view(), name="Password")
]
