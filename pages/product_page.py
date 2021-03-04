from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET)
        button.click()
        self.solve_quiz_and_get_code()

    def compare_name(self):
        alert_name = self.browser.find_elements(*ProductPageLocators.ALERT_LIST)[0]
        name = self.browser.find_element(*ProductPageLocators.NAME)
        assert alert_name.text == name.text, "Wrong name in the basket"

    def compare_price(self):
        alert_price = self.browser.find_elements(*ProductPageLocators.ALERT_LIST)[2]
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        assert alert_price.text == price.text, "Wrong price of the basket"

