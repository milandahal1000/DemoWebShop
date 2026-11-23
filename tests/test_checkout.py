"""
Automated tests for Checkout operations.
Maps to manual test cases:
- TC-080: Empty cart redirect when attempting checkout
- TC-088: Terms of service checkbox gates progression to checkout
- TC-082 / TC-086: One-page checkout flow initialization for authenticated user
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import BASE_URL, DEMO_EMAIL, DEMO_PASSWORD, EXPLICIT_WAIT
from config.test_data import ENDPOINTS


@pytest.mark.cart
class TestCheckout:
    """Test suite covering checkout gates, validation, and multi-step progress."""

    def test_empty_cart_checkout_redirect(self, driver):
        """TC-080: Navigating directly to /onepagecheckout with an empty cart redirects to /cart."""
        driver.get(f"{BASE_URL}onepagecheckout")
        wait = WebDriverWait(driver, EXPLICIT_WAIT)

        wait.until(EC.url_contains("/cart"))
        empty_msg = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.order-summary-content"))
        )
        assert "Your Shopping Cart is empty!" in empty_msg.text

    def test_terms_of_service_gates_checkout(self, driver):
        """TC-088: Clicking Checkout without agreeing to TOS displays warning dialog and blocks navigation."""
        driver.get(f"{BASE_URL}computing-and-internet")
        wait = WebDriverWait(driver, EXPLICIT_WAIT)

        # Add item to cart
        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button-13"))).click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.bar-notification.success")))

        # Navigate to cart
        driver.get(ENDPOINTS["cart"])
        wait.until(EC.visibility_of_element_located((By.ID, "checkout")))

        # Ensure terms of service is NOT checked
        tos_checkbox = driver.find_element(By.ID, "termsofservice")
        if tos_checkbox.is_selected():
            tos_checkbox.click()

        # Click checkout
        driver.find_element(By.ID, "checkout").click()

        # Warning dialog appears
        warning_dialog = wait.until(
            EC.visibility_of_element_located((By.ID, "terms-of-service-warning-box"))
        )
        assert "Please accept the terms of service before the next step." in warning_dialog.text
        assert "cart" in driver.current_url.lower()

        # Cleanup: remove item
        remove_cb = driver.find_element(By.NAME, "removefromcart")
        remove_cb.click()
        driver.find_element(By.NAME, "updatecart").click()

    def test_authenticated_checkout_navigation(self, driver):
        """TC-082: Authenticated user agreeing to TOS enters one-page checkout successfully."""
        wait = WebDriverWait(driver, EXPLICIT_WAIT)

        # 1. Log in
        driver.get(ENDPOINTS["login"])
        driver.find_element(By.ID, "Email").send_keys(DEMO_EMAIL)
        driver.find_element(By.ID, "Password").send_keys(DEMO_PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "input.login-button").click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.header-links a.account")))

        # 2. Add product
        driver.get(f"{BASE_URL}computing-and-internet")
        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button-13"))).click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.bar-notification.success")))

        # 3. Open cart & agree to TOS
        driver.get(ENDPOINTS["cart"])
        tos_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "termsofservice")))
        if not tos_checkbox.is_selected():
            tos_checkbox.click()

        driver.find_element(By.ID, "checkout").click()

        # 4. Verify onepagecheckout loads
        wait.until(EC.url_contains("/onepagecheckout"))
        billing_step = wait.until(
            EC.visibility_of_element_located((By.ID, "opc-billing"))
        )
        assert billing_step.is_displayed(), "Billing address step should be active"

        # 5. Cleanup: Return to cart and remove item
        driver.get(ENDPOINTS["cart"])
        wait.until(EC.visibility_of_element_located((By.NAME, "removefromcart"))).click()
        driver.find_element(By.NAME, "updatecart").click()
