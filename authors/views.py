from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class AuthorLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'authors/login.html'

    def get_success_url(self):
        return reverse_lazy('product:home')


class AuthorLogoutView(LogoutView):
    success_url = reverse_lazy('product:home')
