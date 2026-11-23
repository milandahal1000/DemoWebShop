"""
Shopping cart test suite refactored with Page Object Model (CartPage, ProductPage).
Maps to manual test cases: TC-060, TC-061, TC-064, TC-065, TC-066.
"""
import pytest
from pages.cart_page import CartPage
from pages.product_page import ProductPage


@pytest.mark.cart
class TestCart:
    """Shopping cart operations using CartPage and ProductPage."""

    def test_empty_cart_message(self, driver):
        """TC-060: Opening cart with no items shows empty cart notification."""
        cart_page = CartPage(driver)
        cart_page.open()

        assert "Your Shopping Cart is empty!" in cart_page.get_order_summary_text()

    def test_add_simple_product_to_cart(self, driver):
        """TC-061: Adding a book updates cart header counter and cart line item."""
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        product_page.open("computing-and-internet")
        product_page.add_to_cart()

        cart_page.open()
        assert "Computing and Internet" in cart_page.get_product_names()

        # Cleanup
        cart_page.remove_item()

    def test_update_item_quantity_in_cart(self, driver):
        """TC-064: Modifying quantity recalculates line subtotal."""
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        product_page.open("computing-and-internet")
        product_page.add_to_cart()

        cart_page.open()
        cart_page.update_quantity("2")

        subtotal = cart_page.get_first_item_subtotal()
        assert subtotal == "20.00", f"Expected subtotal 20.00, got: {subtotal}"

        # Cleanup
        cart_page.remove_item()

    def test_remove_product_from_cart(self, driver):
        """TC-065: Ticking remove checkbox and updating cart removes product."""
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        product_page.open("computing-and-internet")
        product_page.add_to_cart()

        cart_page.open()
        cart_page.remove_item()

        assert "Your Shopping Cart is empty!" in cart_page.get_order_summary_text()

    def test_max_quantity_boundary_validation(self, driver):
        """TC-066: Entering quantity above 10000 produces validation error."""
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        product_page.open("computing-and-internet")
        product_page.add_to_cart()

        cart_page.open()
        cart_page.update_quantity("99999")

        assert "The maximum quantity allowed for purchase is 10000." in cart_page.get_order_summary_text()

        # Cleanup
        cart_page.remove_item()
