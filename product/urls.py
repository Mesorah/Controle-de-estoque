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

    path(
        'search/',
        staff_member_required(
            views.ProductSearch.as_view(),
            login_url=reverse_lazy('authors:login')
        ),
        name='search'
    ),

    path(
        'create/',
        staff_member_required(
            views.CreateProductSession.as_view(),
            login_url=reverse_lazy('authors:login')
        ),
        name='create'
    ),

    path(
        'delete/<str:id>/',
        staff_member_required(
            views.DeleteProductSession.as_view(),
            login_url=reverse_lazy('authors:login')
        ),
        name='delete'
    ),

    path(
        'dashboard/',
        staff_member_required(
            views.Dashboard.as_view(),
            login_url=reverse_lazy('authors:login')
        ),
        name='dashboard'
    ),
]
