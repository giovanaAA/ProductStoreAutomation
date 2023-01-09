from selenium import webdriver

from core.global_variables import PATH_FIREFOX_DRIVER


class FirefoxDriver:

    @staticmethod
    def get_driver():
        """
        Método que inicializa el controlador de Firefox y devuelve la instancia
        :return: instancia del controlador de Firefox
        """
        driver = webdriver.Firefox(PATH_FIREFOX_DRIVER)
        return driver
