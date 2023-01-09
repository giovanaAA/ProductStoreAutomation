from core.pages.BasePage import BasePage

class LogInPage(BasePage):
    # Diccionario de localizadores para iniciar sesión
    locators = {
        "usernameInput": ('XPATH', '//input[@id="loginusername"]'),
        "passwordInput": ('XPATH', '//input[@id="loginpassword"]'),
        "loginBtn": ('XPATH', '//button[@onclick="logIn()"]'),
        **BasePage.locators
    }

    def fill_login_page(self, username, password):
        """
        Método que permite iniciar sesión para ingresar a la página.
        Parámetro username: nombre de usuario
        Parámetro password: contraseña de usuario
        """
        self.usernameInput.set_text(username)
        self.passwordInput.set_text(password)

    def click_button_login_close(self):
        """
        Método que permite hacer click en el botón "Close"
        """
        self.loginBtn.click_button()