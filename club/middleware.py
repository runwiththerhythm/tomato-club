from django.shortcuts import redirect
from django.urls import reverse

class RedirectAuthenticatedUsersMiddleware:
    AUTH_URL_NAMES = {"account_login", "account_signup"}

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            auth_paths = {reverse(name) for name in self.AUTH_URL_NAMES}
            if request.path in auth_paths:
                return redirect("club:home")
        return self.get_response(request)
