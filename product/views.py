from django.views.generic import ListView

from product import models


class HomeListView(ListView):
    allow_empty = True
    queryset = None
    model = models.Product
    # paginate_by = None
    context_object_name = 'products'
    # paginator_class = Paginator
    ordering = '-id'
    template_name = 'product/home.html'
