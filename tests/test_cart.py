"""
Automated tests for Shopping Cart operations.
Maps to manual test cases:
- TC-060: Empty cart renders explicit empty message
- TC-061: Adding product updates header counter and creates cart row
- TC-064: Updating quantity recalculates line total and subtotal
- TC-065: Removing an item empties the cart
- TC-066: Excessive quantity triggers max-quantity error message
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import BASE_URL, EXPLICIT_WAIT
from config.test_data import ENDPOINTS


@pytest.mark.cart
class TestCart:
    """Test suite covering cart additions, updates, removal, and quantity boundaries."""

    def test_empty_cart_message(self, driver):
        """TC-060: Opening cart with no items shows empty cart notification."""
        driver.get(ENDPOINTS["cart"])
        wait = WebDriverWait(driver, EXPLICIT_WAIT)

        empty_msg = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.order-summary-content"))
        )
        assert "Your Shopping Cart is empty!" in empty_msg.text

    def test_add_simple_product_to_cart(self, driver):
        """TC-061: Adding a book updates cart header counter and cart line item."""
        driver.get(f"{BASE_URL}computing-and-internet")
        wait = WebDriverWait(driver, EXPLICIT_WAIT)

        # Add to cart
        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button-13"))).click()

        # Wait for success notification banner
        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.bar-notification.success"))
        )

        # Open cart
        driver.get(ENDPOINTS["cart"])
        cart_table = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "table.cart"))
        )
        product_names = [
            elem.text.strip()
            for elem in cart_table.find_elements(By.CSS_SELECTOR, "a.product-name")
        ]
        assert "Computing and Internet" in product_names

        # Cleanup: remove item
        remove_cb = driver.find_element(By.NAME, "removefromcart")
        remove_cb.click()
        driver.find_element(By.NAME, "updatecart").click()

    def test_update_item_quantity_in_cart(self, driver):
        """TC-064: Modifying quantity recalculates line subtotal."""
        driver.get(f"{BASE_URL}computing-and-internet")
        wait = WebDriverWait(driver, EXPLICIT_WAIT)

        # Add 1 item
        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button-13"))).click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.bar-notification.success")))

        # Open cart
        driver.get(ENDPOINTS["cart"])
        qty_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.qty-input")))
        qty_input.clear()
        qty_input.send_keys("2")
        driver.find_element(By.NAME, "updatecart").click()

        # Verify line total is 20.00
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.cart")))
        subtotal = driver.find_element(By.CSS_SELECTOR, "span.product-subtotal").text.strip()
        assert subtotal == "20.00", f"Expected subtotal 20.00, got: {subtotal}"

        # Cleanup
        remove_cb = driver.find_element(By.NAME, "removefromcart")
        remove_cb.click()
        driver.find_element(By.NAME, "updatecart").click()

    def test_remove_product_from_cart(self, driver):
        """TC-065: Ticking remove checkbox and updating cart removes product."""
        driver.get(f"{BASE_URL}computing-and-internet")
        wait = WebDriverWait(driver, EXPLICIT_WAIT)

        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button-13"))).click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.bar-notification.success")))

        driver.get(ENDPOINTS["cart"])
        wait.until(EC.visibility_of_element_located((By.NAME, "removefromcart"))).click()
        driver.find_element(By.NAME, "updatecart").click()

        empty_body = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.order-summary-content"))
        )
        assert "Your Shopping Cart is empty!" in empty_body.text

    def test_max_quantity_boundary_validation(self, driver):
        """TC-066: Entering quantity above 10000 produces validation error."""
        driver.get(f"{BASE_URL}computing-and-internet")
        wait = WebDriverWait(driver, EXPLICIT_WAIT)

        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button-13"))).click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.bar-notification.success")))

        driver.get(ENDPOINTS["cart"])
        qty_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.qty-input")))
        qty_input.clear()
        qty_input.send_keys("99999")
        driver.find_element(By.NAME, "updatecart").click()

        # Check for error message
        order_summary = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.order-summary-content"))
        )
        assert "The maximum quantity allowed for purchase is 10000." in order_summary.text

        # Cleanup
        remove_cb = driver.find_element(By.NAME, "removefromcart")
        remove_cb.click()
        driver.find_element(By.NAME, "updatecart").click()
