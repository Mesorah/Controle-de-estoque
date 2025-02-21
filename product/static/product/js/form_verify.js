class FormVerify {
    constructor() {
        this.form = document.querySelector('.create-product-form');
        this.form.addEventListener('submit', (e) => {
            e.preventDefault();
            if(this.validateFormInputs()) this.form.submit();
        });
    }
    
    validateFormInputs() {
        const elements = document.querySelectorAll('.form-verify');
        return this.verifyInput(elements);
    }
    
    addError(element, msg) {
        const errorElement = document.createElement('div');
        errorElement.className = 'class-error';
        errorElement.innerText = msg;
        element.insertAdjacentElement('beforeBegin', errorElement);
    }
    
    verifyInput(elements) {
        const classErrors = document.querySelectorAll('.class-error');
        let valid = true;
    
        for(const error of classErrors) {
            error.remove();
        }
    
        for(const element of elements) {
            if(!element.value) {
                this.addError(element, 'Incomplete field');
                valid = false;
            }
        }
    
        const barcode = document.getElementById('id_barcode');
        const barcodeVerification = this.verifyBarcode(barcode);
    
        const costPrice = document.getElementById('id_cost_price');
        const salePrice = document.getElementById('id_sale_price');
    
        const priceVerification = this.verifyPrice(costPrice, salePrice);
    
        if (valid && barcodeVerification && priceVerification) {
            return true;
        }

        return false;
    }
    
    verifyBarcode(barcode) {
        if(barcode.value.length !== 13) {
            this.addError(barcode, 'The size of barcode field has to be 13 digits');
    
            return false;
        }

        return true;
    }
    
    verifyPrice(costPrice, salePrice) {
        const costPriceFloat = parseFloat(costPrice.value);
        const salePriceFloat = parseFloat(salePrice.value);
    
        let valid = true;
    
        if(costPriceFloat <= 0) {
            this.addError(
                costPrice, 'The cost price cannot be less than or equal to zero'
            );
    
            valid = false;
        }
    
        if(costPriceFloat > salePriceFloat || costPriceFloat === salePriceFloat) {
            this.addError(
                costPrice, 'The cost price cannot be greater than or equal to the selling price'
            );
    
            valid = false;
        }
    
        return valid;
    }
}

new FormVerify();
