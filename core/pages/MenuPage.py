from core.pages.BasePage import BasePage


class MenuPage(BasePage):
    locators = {
        "signUpBtn": ('XPATH', '//a[@id="signin2"]'),
        "logInBtn": ('XPATH', '//a[@id="login2"]'),
        "cartBtn": ('XPATH', '//a[@id="cartur"]'),
        "logOutBtn": ('XPATH', '//a[@id= "logout2"]'),
        **BasePage.locators
    }

    def click_on_sign_up(self):
        """
        Método que permite hacer click en el botón "Sign Up" que ingresa al registro de usuarios
        """
        self.signUpBtn.click_button()

    def click_on_log_in(self):
        """
        Método que permite hacer click en el botón "Log in" que ingresa a la página
        """
        self.logInBtn.click_button()

    def click_on_cart(self):
        """
        Método que permite hacer click en el botón "Cart" que ingresa al carrito de compra
        """
        self.cartBtn.click_button()

    def click_on_log_out(self):
        """
        Método que permite cerrar sesión
        """
        self.logOutBtn.click_button()
