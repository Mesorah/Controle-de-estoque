from product.models import Category


def create_session_product():
    category = Category.objects.create(name='TestCategory')

    data = {
        'name': 'TestProduct',
        'description': 'TestDescription',
        'stock': 10,
        'barcode': '1111111111111',
        'category': category.id,
        'cost_price': 5.99,
        'sale_price': 7.99
    }

    return data
