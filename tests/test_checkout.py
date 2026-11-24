"""
Checkout test suite refactored with centralized test data and reusable fixtures.
Maps to manual test cases: TC-080, TC-088, TC-082 / TC-086.
"""
import pytest
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
from config.test_data import CART_DATA, CHECKOUT_DATA, ENDPOINTS


@pytest.mark.cart
class TestCheckout:
    """Checkout gates and navigation using reusable fixtures (logged_in_driver, cart_with_item)."""

    def test_empty_cart_checkout_redirect(self, driver):
        """TC-080: Navigating directly to /onepagecheckout with an empty cart redirects to /cart."""
        checkout_page = CheckoutPage(driver)
        cart_page = CartPage(driver)

        checkout_page.open_onepagecheckout()

        assert "cart" in checkout_page.get_current_url().lower()
        assert CART_DATA["empty_message"] in cart_page.get_order_summary_text()

    def test_terms_of_service_gates_checkout(self, cart_with_item):
        """TC-088: Clicking Checkout without agreeing to TOS displays warning dialog using cart_with_item."""
        cart_page = CartPage(cart_with_item)

        cart_page.open()
        cart_page.set_terms_agreement(agree=False)
        cart_page.click_checkout()

        warning_text = cart_page.get_tos_warning_text()
        assert CHECKOUT_DATA["tos_warning"] in warning_text
        assert "cart" in cart_page.get_current_url().lower()

    def test_authenticated_checkout_navigation(self, logged_in_driver, cart_with_item):
        """TC-082: Authenticated user with cart item agreeing to TOS enters one-page checkout."""
        cart_page = CartPage(logged_in_driver)
        checkout_page = CheckoutPage(logged_in_driver)

        # Cart & agree to TOS
        cart_page.open()
        cart_page.set_terms_agreement(agree=True)
        cart_page.click_checkout()

        # Verify entry to onepagecheckout
        assert "onepagecheckout" in checkout_page.get_current_url()
        assert checkout_page.is_billing_step_active(), "Billing address step should be active"
