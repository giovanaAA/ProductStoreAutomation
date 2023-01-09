from core.pages.BasePage import BasePage

class SignUpPage(BasePage):
    # Diccionario de localizadores para registro de usuarios
    locators = {
        "usernameInput": ('XPATH', '//input[@id="sign-username"]'),
        "passwordInput": ('XPATH', '//input[@id="sign-password"]'),
        "signupBtn": ('XPATH', '//button[@type="button" and contains(text(), "Sign up")]'),
        "closeBtn": ('XPATH', '//div[@id="signInModal"]//button[contains(text(), "Close")]'),
        **BasePage.locators
    }

    def fill_signup_page(self, username, password):
        """
        Método que permite registrar a usuarios.
        Parámetro username: nombre de usuario
        Parámetro password: contraseña de usuario
        """
        self.usernameInput.set_text(username)
        self.passwordInput.set_text(password)

    def click_button_sign_up(self):
        """
        Método que permite acpetar el registro de usuario
        """
        self.signupBtn.click_button()

    def click_button_close(self):
        """
        Método que permite cerrar el registro
        """
        self.closeBtn.click_button()


