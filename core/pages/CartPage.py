from core.pages.BasePage import BasePage

class CartPage(BasePage):
    # Diccionario de localizadores para realizar pedido y llenar el
    # formulario de compra
    locators = {
        "placeOrderBtn": ('XPATH', '//button[contains(text(), "Place Order")]'),
        "nameInput": ('XPATH', '//input[@id="name"]'),
        "countryInput": ('XPATH', '//input[@id="country"]'),
        "cityInput": ('XPATH', '//input[@id="city"]'),
        "creditCardInput": ('XPATH', '//input[@id="card"]'),
        "monthInput": ('XPATH', '//input[@id="month"]'),
        "yearInput": ('XPATH', '//input[@id="year"]'),
        "purchaseBtn": ('XPATH', '//button[@onclick="purchaseOrder()"]'),
        "okBtn": ('XPATH', '//button[@class="confirm btn btn-lg btn-primary"]'),
        **BasePage.locators
    }

    def select_place_order(self):
        """
        Método que permite hacer click en el botón "Place Order" para una orden de compra
        """
        self.placeOrderBtn.click_button()

    def fill_form_purchase(self, name, country, city, credit_card, month, year):
        """
        Método que abre un formulario para llenar una orden de compra de un producto
        """
        self.nameInput.set_text(name)
        self.countryInput.set_text(country)
        self.cityInput.set_text(city)
        self.creditCardInput.set_text(credit_card)
        self.monthInput.set_text(month)
        self.yearInput.set_text(year)

    def click_button_purchase(self):
        """
        Método que permite hacer click en el botón "Purchase" para realizar la compra
        """
        self.purchaseBtn.click_button()

    def click_button_ok(self):
        """
        Método que permite hacer click en el botón "Ok" que confirma la compra
        """
        self.okBtn.click_button()
