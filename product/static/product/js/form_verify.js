function init() {
    const form = document.querySelector('.create-product-form');
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        if(getElements()) form.submit();
    })
}

function getElements() {
    const elements = document.querySelectorAll('.form-verify');
    return verifyInput(elements);
}

function addError(element, msg) {
    const errorElement = document.createElement('div');
    errorElement.className = 'class-error';
    errorElement.innerText = msg;
    element.insertAdjacentElement('beforeBegin', errorElement);
}

function verifyInput(elements) {
    const classErrors = document.querySelectorAll('.class-error');
    let valid = true;

    for(const error of classErrors) {
        error.remove();
    }

    for(const element of elements) {
        if(!element.value) addError(element, 'Incomplete field');
        valid = false;
    }

    const barcode = document.getElementById('id_barcode');
    const barcodeVerification = verifyBarcode(barcode);

    const costPrice = document.getElementById('id_cost_price');
    const salePrice = document.getElementById('id_sale_price');

    const priceVerification = verifyPrice(costPrice, salePrice);

    if (valid && barcodeVerification && priceVerification) {
        return false
    }
}

function verifyBarcode(barcode) {
    if(barcode.value.length !== 13) {
        addError(barcode, 'The size of barcode field has to be 13 digits');

        return false;
    }
}

function verifyPrice(costPrice, salePrice) {
    costPriceFloat = parseFloat(costPrice.value);
    salePriceFloat = parseFloat(salePrice.value);

    let valid = true;

    if(costPriceFloat === 0) {
        addError(
            costPrice, 'The cost price cannot be 0'
        );

        valid = false;
    }

    if(costPriceFloat > salePriceFloat || costPriceFloat === salePriceFloat) {
        addError(
            costPrice, 'The cost price cannot be greater than or equal to the selling price'
        );

        valid = false;
    }

    return valid;
}


init();