"""
LoginPage object representing the Demo Web Shop login screen.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.test_data import ENDPOINTS


class LoginPage(BasePage):
    """Page object for login and authentication workflows."""

    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.login-button")
    REMEMBER_ME_CHECKBOX = (By.ID, "RememberMe")
    VALIDATION_SUMMARY_ERRORS = (By.CSS_SELECTOR, "div.validation-summary-errors")
    RETURNING_WRAPPER = (By.CSS_SELECTOR, "div.returning-wrapper")

    def open(self):
        """Navigate to the login page."""
        super().open(ENDPOINTS["login"])

    def enter_email(self, email):
        self.type(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, email, password):
        """Convenience method to fill credentials and submit."""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def get_error_summary_text(self):
        """Retrieve authentication error message."""
        return self.get_text(self.VALIDATION_SUMMARY_ERRORS)

    def is_login_box_visible(self):
        return self.is_visible(self.RETURNING_WRAPPER)
