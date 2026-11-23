"""
CheckoutPage object representing the one-page checkout flow.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import BASE_URL


class CheckoutPage(BasePage):
    """Page object for the multi-step onepagecheckout flow."""

    BILLING_STEP = (By.ID, "opc-billing")

    def open_onepagecheckout(self):
        super().open(f"{BASE_URL}onepagecheckout")

    def is_billing_step_active(self):
        return self.is_visible(self.BILLING_STEP)
