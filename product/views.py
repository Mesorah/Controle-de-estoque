from django.views.generic import ListView

from product import models


class HomeListView(ListView):
    allow_empty = True
    model = models.Product
    paginate_by = 1
    context_object_name = 'products'
    ordering = '-id'
    template_name = 'product/home.html'
