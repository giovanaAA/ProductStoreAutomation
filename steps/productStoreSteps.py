from behave import Step
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from core.global_variables import BASE_URI
from core.pages.CartPage import CartPage
from core.pages.CategoryPage import CategoryPage
from core.pages.MenuPage import MenuPage
from core.pages.SignUpPage import SignUpPage
from core.pages.LogInPage import LogInPage


@Step("ir a la página")
def goto_page(context):
    context.page.driver.get(BASE_URI)


@Step("click en el botón 'Sign Up'")
def goto_sign_up(context):
    menu = MenuPage(context.page)
    menu.click_on_sign_up()


@Step("llenar el campo '{username}' y '{password}'")
def fill_username_and_password(context, username, password):
    signup = SignUpPage(context.page)
    signup.fill_signup_page(username=username, password=password)


@Step("click en el botón 'Sign up' y 'Aceptar'")
def click_button_signup_and_aceptar(context):
    button_signup = SignUpPage(context.page)
    button_signup.click_button_sign_up()
    WebDriverWait(context.page.driver, 10).until(EC.alert_is_present())
    context.page.driver.switch_to.alert.accept()


@Step("click en el botón 'Close'")
def click_button_close(context):
    button_close = SignUpPage(context.page)
    button_close.click_button_close()


@Step("click en el botón 'Log in'")
def goto_log_in(context):
    menu1 = MenuPage(context.page)
    menu1.click_on_log_in()


#
@Step("llenar '{username2}' y '{password2}'")
def fill_username_and_password2(context, username2, password2):
    login = LogInPage(context.page)
    login.fill_login_page(username=username2, password=password2)


@Step("click en el botón de cierre 'Log in'")
def click_button_login(context):
    menu = LogInPage(context.page)
    menu.click_button_login_close()


@Step("click en el botón 'Laptops'")
def goto_category(context):
    select_category = CategoryPage(context.page)
    select_category.select_category()


@Step("click en el primer item")
def click_on_first_item(context):
    select_item = CategoryPage(context.page)
    select_item.select_first_item()


@Step("click en el botón 'Add to cart'")
def click_button_add_to_cart(context):
    add_to_cart = CategoryPage(context.page)
    add_to_cart.click_on_add_to_cart()
    WebDriverWait(context.page.driver, 10).until(EC.alert_is_present())
    context.page.driver.switch_to.alert.accept()


@Step("click en la pestaña 'Cart'")
def goto_cart(context):
    menu = MenuPage(context.page)
    menu.click_on_cart()


@Step("click en el botón 'Place Order'")
def click_button_place_order(context):
    place_order = CartPage(context.page)
    place_order.select_place_order()


@Step("llenar el formulario de compra '{name}', '{country}', '{city}', '{credit_card}', '{month}', '{year}'")
def fill_form(context, name, country, city, credit_card, month, year):
    form = CartPage(context.page)
    form.fill_form_purchase(name=name, country=country, city=city, credit_card=credit_card, month=month, year=year)


@Step("click en el botón 'Purchase'")
def click_on_purchase(context):
    purchase = CartPage(context.page)
    purchase.click_button_purchase()


@Step("click en el botón 'Ok'")
def click_on_ok(context):
    button_ok = CartPage(context.page)
    button_ok.click_button_ok()
