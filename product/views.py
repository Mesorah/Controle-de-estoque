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

    def init_product(self):
        id_variation = 0
        products = self.request.session['products'] = {}
        products[id_variation] = {}

        return id_variation, products

    def get_max_id(self, products):
        max_number = 0
        for product in products:
            max_number = max(max_number, int(product))

        id_variation = max_number

        return id_variation

    def get_attributes(self, form):
        name = form.cleaned_data.get('name')
        description = form.cleaned_data.get('description')
        stock = form.cleaned_data.get('stock')
        barcode = form.cleaned_data.get('barcode')
        category = form.cleaned_data.get('category')
        cost_price = form.cleaned_data.get('cost_price')
        sale_price = form.cleaned_data.get('sale_price')

        attributes = {
            'name': name,
            'description': description,
            'stock': stock,
            'barcode': barcode,
            'category': category,
            'cost_price':  cost_price,
            'sale_price': sale_price
        }

        return attributes

    def set_product(self, products, id_variation, attributes):
        products[id_variation] = {
                'name': attributes['name'],
                'description': attributes['description'],
                'stock': attributes['stock'],
                'barcode': attributes['barcode'],
                'category': attributes['category'].name,
                'cost_price': attributes['cost_price'],
                'sale_price': attributes['sale_price']
            }

        return products

    def post(self, *args, **kwargs):
        products = self.request.session.get('products')

        if not products:
            id_variation, products = self.init_product()
        else:
            id_variation = self.get_max_id(products)

        form = forms.CreateProductForm(self.request.POST)

        if form.is_valid():
            attributes = self.get_attributes(form)
            id_variation += 1

            self.set_product(products, id_variation, attributes)

            self.request.session['products'] = products
            self.request.session.modified = True
        else:
            form = forms.CreateProductForm(self.request.POST)
            print(form.errors)

        print(self.request.session.get('products'))

        return self.return_render(form)
