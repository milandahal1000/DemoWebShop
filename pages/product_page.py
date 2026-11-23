"""
ProductPage object representing product details and add-to-cart actions.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import BASE_URL


class ProductPage(BasePage):
    """Page object for individual product details and cart addition."""

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "input[id^='add-to-cart-button']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product-name h1")

    def open(self, slug):
        super().open(f"{BASE_URL}{slug}")

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
        self.wait_for_notification_success()
