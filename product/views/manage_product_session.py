from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View

from product import forms, models


class ProductSession(View):
    def return_render(self, form):
        return render(self.request, 'product/form.html', context={
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

            try:
                del products[0]
            except KeyError:
                pass

            self.request.session.modified = True

            print(self.request.session['products'])

            return redirect('product:home')
        else:
            form = forms.CreateProductForm(self.request.POST)
            print(form.errors)

        return self.return_render(form)


class CreateProductSession(ProductSession):
    pass


class UpdateProductSession(ProductSession):
    def set_category_product(self, product):
        product['category'] = models.Category.objects.filter(
            name=product['category']
        ).first()

        return product

    def get(self, request, id, *args, **kwargs):
        try:
            product = self.request.session.get('products')[str(id)]
        except (TypeError, KeyError):
            return redirect('product:dashboard')

        self.set_category_product(product)

        form = forms.CreateProductForm(initial=product)

        return self.return_render(form)

    def post(self, request, id, *args, **kwargs):
        products = self.request.session.get('products')
        product = products[str(id)]
        self.set_category_product(product)

        form = forms.CreateProductForm(self.request.POST)
        if form.is_valid():
            attributes = self.get_attributes(form)

            self.set_product(products, str(id), attributes)

            product = products[str(id)]  # Criando novamente para atualizar

            self.request.session['products'][str(id)] = product

            self.request.session.modified = True

            return redirect('product:dashboard')
        else:
            form = forms.CreateProductForm(initial=product)
            messages.add_message(request, messages.ERROR, "Form error")

        return self.return_render(form)


class DeleteProductSession(View):
    def post(self, request, id, *args, **kwargs):
        session = self.request.session['products']
        del session[id]

        self.request.session.modified = True

        return redirect('product:dashboard')
