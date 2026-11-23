"""
CartPage object representing the shopping cart page.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.test_data import ENDPOINTS


class CartPage(BasePage):
    """Page object for shopping cart inspection, quantity updates, and checkout initiation."""

    ORDER_SUMMARY_CONTENT = (By.CSS_SELECTOR, "div.order-summary-content")
    CART_TABLE = (By.CSS_SELECTOR, "table.cart")
    PRODUCT_NAMES = (By.CSS_SELECTOR, "table.cart a.product-name")
    QTY_INPUT = (By.CSS_SELECTOR, "input.qty-input")
    UPDATE_CART_BUTTON = (By.NAME, "updatecart")
    REMOVE_CHECKBOX = (By.NAME, "removefromcart")
    PRODUCT_SUBTOTAL = (By.CSS_SELECTOR, "span.product-subtotal")
    TERMS_OF_SERVICE_CHECKBOX = (By.ID, "termsofservice")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    TOS_WARNING_BOX = (By.ID, "terms-of-service-warning-box")

    def open(self):
        super().open(ENDPOINTS["cart"])

    def get_order_summary_text(self):
        return self.get_text(self.ORDER_SUMMARY_CONTENT)

    def get_product_names(self):
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [e.text.strip() for e in elements]

    def update_quantity(self, new_qty):
        self.type(self.QTY_INPUT, str(new_qty))
        self.click(self.UPDATE_CART_BUTTON)

    def get_first_item_subtotal(self):
        return self.get_text(self.PRODUCT_SUBTOTAL)

    def remove_item(self):
        self.click(self.REMOVE_CHECKBOX)
        self.click(self.UPDATE_CART_BUTTON)

    def clear_cart_if_not_empty(self):
        """Helper to ensure cart is empty."""
        remove_boxes = self.driver.find_elements(*self.REMOVE_CHECKBOX)
        if remove_boxes:
            for cb in remove_boxes:
                if not cb.is_selected():
                    cb.click()
            self.click(self.UPDATE_CART_BUTTON)

    def set_terms_agreement(self, agree=True):
        cb = self.find(self.TERMS_OF_SERVICE_CHECKBOX)
        if agree and not cb.is_selected():
            cb.click()
        elif not agree and cb.is_selected():
            cb.click()

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def get_tos_warning_text(self):
        return self.get_text(self.TOS_WARNING_BOX)
