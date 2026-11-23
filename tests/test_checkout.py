"""
Checkout test suite refactored with Page Object Model (CheckoutPage, CartPage, LoginPage, ProductPage).
Maps to manual test cases: TC-080, TC-088, TC-082 / TC-086.
"""
import pytest
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from config.config import DEMO_EMAIL, DEMO_PASSWORD


@pytest.mark.cart
class TestCheckout:
    """Checkout gate and navigation tests using Page Objects."""

    def test_empty_cart_checkout_redirect(self, driver):
        """TC-080: Navigating directly to /onepagecheckout with an empty cart redirects to /cart."""
        checkout_page = CheckoutPage(driver)
        cart_page = CartPage(driver)

        checkout_page.open_onepagecheckout()

        assert "cart" in checkout_page.get_current_url().lower()
        assert "Your Shopping Cart is empty!" in cart_page.get_order_summary_text()

    def test_terms_of_service_gates_checkout(self, driver):
        """TC-088: Clicking Checkout without agreeing to TOS displays warning dialog and blocks navigation."""
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        # Add item
        product_page.open("computing-and-internet")
        product_page.add_to_cart()

        cart_page.open()
        cart_page.set_terms_agreement(agree=False)
        cart_page.click_checkout()

        warning_text = cart_page.get_tos_warning_text()
        assert "Please accept the terms of service before the next step." in warning_text
        assert "cart" in cart_page.get_current_url().lower()

        # Cleanup
        cart_page.remove_item()

    def test_authenticated_checkout_navigation(self, driver):
        """TC-082: Authenticated user agreeing to TOS enters one-page checkout successfully."""
        login_page = LoginPage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        # 1. Log in
        login_page.open()
        login_page.login(DEMO_EMAIL, DEMO_PASSWORD)
        assert login_page.is_logout_link_visible()

        # 2. Add product
        product_page.open("computing-and-internet")
        product_page.add_to_cart()

        # 3. Cart & agree to TOS
        cart_page.open()
        cart_page.set_terms_agreement(agree=True)
        cart_page.click_checkout()

        # 4. Verify checkout entry
        assert "onepagecheckout" in checkout_page.get_current_url()
        assert checkout_page.is_billing_step_active(), "Billing address step should be active"

        # 5. Cleanup: return to cart and clear
        cart_page.open()
        cart_page.remove_item()
