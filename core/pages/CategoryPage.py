from core.pages.BasePage import BasePage

class CategoryPage(BasePage):
    # Diccionario de localizadores para seleccionar la categoría de "Laptops"
    # seleccionar el primer item y añadir al carrito
    locators = {
        "laptopsCategoryBtn": ('XPATH', '//a[@id="cat"]//following-sibling::a[contains(text(), "Laptops")]'),
        "selectItem": ('XPATH', '//h4/a[@href="prod.html?idp_=9"]'),
        "addToCartBtn": ('XPATH', '//a[@onclick="addToCart(9)"]'),
        **BasePage.locators
    }

    def select_category(self):
        """
        Método que permite seleccionar una categoría:Laptops
        """
        self.laptopsCategoryBtn.click_button()

    def select_first_item(self):
        """
        Método que permite seleccionar el primer item dentro la categoría
        """
        self.selectItem.click_button()

    def click_on_add_to_cart(self):
        """
        Método que permite hacer click en el botón "Add to cart" para añadir la compra
        """
        self.addToCartBtn.click_button()


