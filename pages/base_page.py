"""
BasePage class providing reusable Selenium WebDriver interactions and common header navigation.
All specialized Page Objects inherit from this class.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import EXPLICIT_WAIT, BASE_URL


class BasePage:
    """Base class for all Page Objects in the Demo Web Shop automation suite."""

    # Common Header Locators
    LOGO = (By.CSS_SELECTOR, "div.header-logo a")
    REGISTER_LINK = (By.CSS_SELECTOR, "div.header-links a.ico-register")
    LOGIN_LINK = (By.CSS_SELECTOR, "div.header-links a.ico-login")
    LOGOUT_LINK = (By.CSS_SELECTOR, "div.header-links a.ico-logout")
    ACCOUNT_EMAIL_LINK = (By.CSS_SELECTOR, "div.header-links a.account")
    CART_HEADER_LINK = (By.CSS_SELECTOR, "div.header-links a.ico-cart")
    WISHLIST_HEADER_LINK = (By.CSS_SELECTOR, "div.header-links a.ico-wishlist")
    HEADER_SEARCH_INPUT = (By.ID, "small-searchterms")
    HEADER_SEARCH_BUTTON = (By.CSS_SELECTOR, "input.search-box-button")
    NOTIFICATION_BANNER = (By.CSS_SELECTOR, "div.bar-notification")
    NOTIFICATION_SUCCESS = (By.CSS_SELECTOR, "div.bar-notification.success")

    def __init__(self, driver, timeout=EXPLICIT_WAIT):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def open(self, url):
        """Navigate to a specified URL."""
        self.driver.get(url)

    def find(self, locator):
        """Wait for an element to be visible and return it."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        """Wait for elements to be present and return list."""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        """Wait for an element to be clickable and click it."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator, text, clear=True):
        """Type text into an input field, clearing existing content if clear=True."""
        element = self.find(locator)
        if clear:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Retrieve visible text of an element."""
        return self.find(locator).text.strip()

    def is_visible(self, locator, timeout=None):
        """Check if an element is visible within a given timeout."""
        t = timeout if timeout is not None else self.timeout
        try:
            WebDriverWait(self.driver, t).until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def get_title(self):
        """Return the current page title."""
        return self.driver.title

    def get_current_url(self):
        """Return the current URL."""
        return self.driver.current_url

    # --- Header Interactions ---
    def is_logo_visible(self):
        return self.is_visible(self.LOGO)

    def is_register_link_visible(self):
        return self.is_visible(self.REGISTER_LINK)

    def is_login_link_visible(self):
        return self.is_visible(self.LOGIN_LINK)

    def is_logout_link_visible(self):
        return self.is_visible(self.LOGOUT_LINK)

    def is_cart_link_visible(self):
        return self.is_visible(self.CART_HEADER_LINK)

    def is_search_input_visible(self):
        return self.is_visible(self.HEADER_SEARCH_INPUT)

    def get_account_email(self):
        return self.get_text(self.ACCOUNT_EMAIL_LINK)

    def click_logout(self):
        self.click(self.LOGOUT_LINK)

    def search_header(self, keyword):
        self.type(self.HEADER_SEARCH_INPUT, keyword)
        self.click(self.HEADER_SEARCH_BUTTON)

    def wait_for_notification_success(self):
        return self.find(self.NOTIFICATION_SUCCESS)
