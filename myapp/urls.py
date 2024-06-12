from django.urls import include, path
from django.contrib.auth.views import LogoutView
from myspa.views import (HomePage, Login, Register)


urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/', include('allauth.urls')),
]