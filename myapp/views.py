from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import login
from forms.forms import LoginUserForm, RegisterUserForm
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DeleteView, UpdateView, CreateView


class Login(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        user = self.request.user
        if user.is_staff:
            return reverse_lazy('index')
        else:
            return reverse_lazy('index')


class Register(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = '/'

    def form_valid(self, form):
        result = super().form_valid(form=form)
        login(self.request, self.object)
        return result


class HomePage(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
