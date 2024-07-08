from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.views import View
from django.shortcuts import redirect, render

from .forms import SignUpForm


class SignupView(View):
    form_class = SignUpForm
    template_name = 'users/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, self.template_name, {'form': form})


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
