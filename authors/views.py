from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class AuthorLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'authors/login.html'
    success_url = reverse_lazy('product:home')

    def get_redirect_url(self):
        return self.success_url


class AuthorLogoutView(LogoutView):
    success_url = reverse_lazy('authors:login')

    def get_redirect_url(self):
        return self.success_url
