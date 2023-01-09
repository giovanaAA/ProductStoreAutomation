from core.drivers.DriverManager import DriverManager


def before_all(context):
    context.page = DriverManager()


def after_all(context):
    context.page .driver.quit()
