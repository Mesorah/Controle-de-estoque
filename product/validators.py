class ProductValidator:
    def __init__(self, data, error=None, ErrorClass=None):
        self.data = data
        self.ErrorClass = ErrorClass
        self.error = error if error is not None else {}

        self.clean()

    def clean_description(self):
        description = self.data.get('description', '')

        if len(description) == 0:
            self.error['description'] = 'Incomplete field'

        return description

    def clean_barcode(self):
        barcode = self.data.get('barcode', '')

        if len(barcode) != 13:
            self.error['barcode'] = (
                'The size of barcode field has to be 13 digits'
            )

        return barcode

    def clean_cost_price(self):
        cost_price = self.data.get('cost_price', 0)

        if cost_price <= 0:
            self.error['cost_price'] = (
                'The cost price cannot be less than or equal to zero'
            )

        return cost_price

    def clean_sale_price(self):
        cost_price = self.data.get('cost_price', 0)
        sale_price = self.data.get('sale_price', 0)

        if cost_price > sale_price or cost_price == sale_price:
            self.error['sale_price'] = (
                'The cost price cannot be greater'
                'than or equal to the selling price'
            )

        return sale_price

    def clean(self):
        self.clean_description()
        self.clean_barcode()
        self.clean_cost_price()
        self.clean_sale_price()

        if self.error:
            raise self.ErrorClass(self.error)
