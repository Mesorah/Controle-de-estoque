from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path, reverse_lazy
from rest_framework.routers import SimpleRouter

from product import views

product_api_router = SimpleRouter()

product_api_router.register(
    'api',
    views.ProducAPIViewSet,
    basename='api'
)

app_name = 'product'


def staff_member(view):
    return staff_member_required(
        view,
        login_url=reverse_lazy('authors:login')
    )


urlpatterns = [
    path(
        '',
        staff_member(views.HomeListView.as_view()),
        name='home'
    ),

    path(
        'search/',
        staff_member(views.ProductSearch.as_view()),
        name='search'
    ),

    path(
        'create/',
        staff_member(views.CreateProductSession.as_view()),
        name='create'
    ),

    path(
        'update/<int:pk>/',
        staff_member(views.UpdateProduct.as_view()),
        name='update'
    ),

    path(
        'update_session/<int:id>/',
        staff_member(views.UpdateProductSession.as_view()),
        name='update_session'
    ),

    path(
        'delete/<str:id>/',
        staff_member(views.DeleteProductSession.as_view()),
        name='delete'
    ),

    path(
        'dashboard/',
        staff_member(views.Dashboard.as_view()),
        name='dashboard'
    ),

    # path(
    #     'api/',
    #     views.ProducAPIViewSet.as_view(),
    #     name='product_list'
    # ),
    # path(
    #     'api/<int:pk>/',
    #     views.ProducAPIViewSet.as_view(),
    #     name='product_detail'
    # ),
]

urlpatterns += product_api_router.urls
