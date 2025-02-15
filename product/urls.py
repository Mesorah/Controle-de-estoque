from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path

from product import views

urlpatterns = [
    path(
        '',
        staff_member_required(
            views.HomeListView.as_view(),
        ),
        name='home'
    ),
]
