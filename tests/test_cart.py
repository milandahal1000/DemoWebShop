"""
Shopping cart test suite refactored with centralized test data and reusable fixtures.
Maps to manual test cases: TC-060, TC-061, TC-064, TC-065, TC-066.
"""
import pytest
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from config.test_data import CART_DATA, PRODUCT_DATA


@pytest.mark.cart
class TestCart:
    """Shopping cart operations using centralized constants and reusable fixtures."""

    def test_empty_cart_message(self, driver):
        """TC-060: Opening cart with no items shows empty cart notification."""
        cart_page = CartPage(driver)
        cart_page.open()

        assert CART_DATA["empty_message"] in cart_page.get_order_summary_text()

    def test_add_simple_product_to_cart(self, driver):
        """TC-061: Adding a book updates cart header counter and cart line item."""
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)
        book = PRODUCT_DATA["simple_book"]

        product_page.open(book["slug"])
        product_page.add_to_cart()

        cart_page.open()
        assert book["name"] in cart_page.get_product_names()

        # Cleanup
        cart_page.remove_item()

    def test_update_item_quantity_in_cart(self, cart_with_item):
        """TC-064: Modifying quantity recalculates line subtotal using cart_with_item fixture."""
        cart_page = CartPage(cart_with_item)
        book = PRODUCT_DATA["simple_book"]

        cart_page.open()
        cart_page.update_quantity("2")

        subtotal = cart_page.get_first_item_subtotal()
        assert subtotal == book["double_qty_subtotal"], (
            f"Expected subtotal {book['double_qty_subtotal']}, got: {subtotal}"
        )

    def test_remove_product_from_cart(self, cart_with_item):
        """TC-065: Ticking remove checkbox and updating cart removes product."""
        cart_page = CartPage(cart_with_item)

        cart_page.open()
        cart_page.remove_item()

        assert CART_DATA["empty_message"] in cart_page.get_order_summary_text()

    def test_max_quantity_boundary_validation(self, cart_with_item):
        """TC-066: Entering quantity above 10000 produces validation error."""
        cart_page = CartPage(cart_with_item)

        cart_page.open()
        cart_page.update_quantity(CART_DATA["max_qty_input"])

        assert CART_DATA["max_qty_error"] in cart_page.get_order_summary_text()
