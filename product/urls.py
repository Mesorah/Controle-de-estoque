from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path, reverse_lazy

from product import views

app_name = 'product'

urlpatterns = [
    path(
        '',
        staff_member_required(
            views.HomeListView.as_view(),
            login_url=reverse_lazy('authors:login')
        ),
        name='home'
    ),
]
