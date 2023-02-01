import threading
from django.urls import reverse
from allauth.account.adapter import DefaultAccountAdapter


class MyAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        if request.user.is_admin:
            return reverse("dashboard:home")
