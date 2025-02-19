from django.db.models import Q
from django.shortcuts import render
from django.utils import translation
from django.views import View
from django.views.generic import ListView

from product import forms, models


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
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        print(self.request.session.get('products'), 'euu')

        return ctx


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


class CreateProduct(View):
    def return_render(self, form):
        return render(self.request, 'product/create.html', context={
            'form': form
        })

    def get(self, *args, **kwargs):
        form = forms.CreateProductForm()

        return self.return_render(form)

    def post(self, *args, **kwargs):
        # del self.request.session['products']
        products = self.request.session.get('products')

        if not products:
            id_variation = 0
            products = self.request.session['products'] = {}
            products[id_variation] = {
                'id': 0
            }
        else:
            max_number = 0
            for product in products:
                max_number = max(max_number, int(product))

            id_variation = max_number

        form = forms.CreateProductForm(self.request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            stock = form.cleaned_data.get('stock')
            barcode = form.cleaned_data.get('barcode')
            category = form.cleaned_data.get('category')
            cost_price = form.cleaned_data.get('cost_price')
            sale_price = form.cleaned_data.get('sale_price')
            id_variation += 1

            products[id_variation] = {
                'name': name,
                'description': description,
                'stock': stock,
                'barcode': barcode,
                'category': category.name,
                'cost_price': cost_price,
                'sale_price': sale_price
            }

            self.request.session['products'] = products
        else:
            form = forms.CreateProductForm(self.request.POST)
            print(form.errors)

        print(self.request.session.get('products'))

        return self.return_render(form)
