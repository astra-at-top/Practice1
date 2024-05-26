from django.urls import path
from .views import Login, Signup , Logout

urlpatterns = [
    path("login", Login.as_view(), name="Login"),
    path("signup", Signup.as_view(), name="Signup"),
    path("logout", Logout.as_view(), name="Logout"),
]
