from django.urls import path

from product import views

urlpatterns = [
    path(
        '',
        views.HomeListView.as_view(),
        name='home'
    ),
]
