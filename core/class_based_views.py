from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

class SecretView(LoginRequiredMixin, ListView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"