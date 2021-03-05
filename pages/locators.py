from selenium.webdriver.common.by import By


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    NAME = (By.CSS_SELECTOR, ".product_main h1")
    ALERT_LIST = (By.CSS_SELECTOR, ".alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_PAGE_BUTTON = (By.CSS_SELECTOR, "span.btn-group")


class BasketPageLocators():
    CONTENT_INNER = (By.CSS_SELECTOR, "#content_inner")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#id_form-0-quantity")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")