"""
module docstring
"""
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .forms import LoginForm


class Login(LoginView):
    form_class = LoginForm
    template_name = 'super_user/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        user = self.request.user
        if user.is_superuser and user.is_staff:
            return reverse_lazy("cost:home")
        else:
            return reverse_lazy("cost:plain_user_home")

    def form_valid(self, form):
        messages.success(self.request, 'با موفقیت وارد شدید!')
        return super().form_valid(form)
