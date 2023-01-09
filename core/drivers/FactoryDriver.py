from core.drivers.ChormeDriver import ChromeDriver
from core.drivers.FirefoxDriver import FirefoxDriver


class FactoryDriver:

    @staticmethod
    def get_driver_manager(driver_type):
        """
    Método que obtiene el controlador
        :param driver_type: nombre del controlador
        :return: Objeto controlador
        """
        if 'chrome' == driver_type:
            return ChromeDriver.get_driver()
        if 'firefox' == driver_type:
            return FirefoxDriver.get_driver()
