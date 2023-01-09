from selenium import webdriver

from core.global_variables import PATH_CHROME_DRIVER


class ChromeDriver:

    @staticmethod
    def get_driver():
        """
        Método que inicializa el controlador de Chrome y devuelve la instancia
        :return: la instancia del controlador
        """
        driver = webdriver.Chrome(executable_path=PATH_CHROME_DRIVER)
        return driver
