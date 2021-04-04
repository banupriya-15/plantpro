from django.urls import path
from .views import userRegister, userLogin

urlpatterns = [
    path('register/', userRegister, name="register"),
    path('login/', userLogin, name="login")
    
    
]