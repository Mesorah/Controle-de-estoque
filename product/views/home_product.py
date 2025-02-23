from django.db.models import Q
from django.shortcuts import redirect, render
from django.utils import translation
from django.views import View
from django.views.generic import ListView

from product import models


class BaseProductMixin(ListView):
    allow_empty = True
    model = models.Product
    paginate_by = 10
    context_object_name = 'products'
    ordering = '-id'
    template_name = 'product/home.html'

    def get_queryset(self):
        qs = super().get_queryset()

        qs = qs.select_related('category')

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        html_language = translation.get_language()

        context['html_language'] = html_language

        return context


class HomeListView(BaseProductMixin):
    pass


class ProductSearch(BaseProductMixin):
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('search').strip()

        qs = qs.filter(
            Q(name__icontains=query) |
            Q(barcode__icontains=query) |
            Q(category__name__icontains=query)
        )

        return qs


class Dashboard(View):
    def return_render(self, session):
        return render(self.request, 'product/dashboard.html', context={
            'products': session
        })

    def get(self, *args, **kwargs):
        session = self.request.session.get('products')

        if not session:
            return redirect('product:home')

        return self.return_render(session)

    def post(self, *args, **kwargs):
        session = self.request.session.get('products')

        if session:
            for product in session.values():
                category = models.Category.objects.filter(
                    name=product['category']
                ).first()

                product['category'] = category
                models.Product.objects.create(**product)

            del self.request.session['products']

        return redirect('product:home')
