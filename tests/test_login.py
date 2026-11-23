"""
Authentication test suite refactored with Page Object Model (LoginPage).
Maps to manual test cases: TC-010, TC-011, TC-012, TC-014, TC-130.
"""
import pytest
from pages.login_page import LoginPage
from config.config import DEMO_EMAIL, DEMO_PASSWORD
from config.test_data import ENDPOINTS


@pytest.mark.auth
class TestAuthentication:
    """Authentication tests refactored with LoginPage."""

    def test_login_with_valid_credentials(self, driver):
        """TC-010: Successful login renders account email and logout button."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(DEMO_EMAIL, DEMO_PASSWORD)

        assert login_page.get_account_email() == DEMO_EMAIL
        assert login_page.is_logout_link_visible()

    def test_login_with_invalid_password(self, driver):
        """TC-011: Login fails when password is incorrect."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(DEMO_EMAIL, "WrongPassword999!")

        error_text = login_page.get_error_summary_text()
        assert "The credentials provided are incorrect" in error_text

    def test_login_with_unregistered_email(self, driver):
        """TC-012: Login fails with message when email is unregistered."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("nonexistent.user.2026@example.com", "SomePassword123")

        error_text = login_page.get_error_summary_text()
        assert "No customer account found" in error_text

    def test_logout_terminates_session(self, driver):
        """TC-014: Logging out restores header to unauthenticated state."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(DEMO_EMAIL, DEMO_PASSWORD)

        login_page.click_logout()

        assert login_page.is_login_link_visible(), "Log in link should be visible after logout"
        assert login_page.is_register_link_visible(), "Register link should be visible after logout"

    def test_unauthenticated_protected_page_redirect(self, driver):
        """TC-130: Accessing /customer/info while signed out redirects to login."""
        login_page = LoginPage(driver)
        login_page.open_url = ENDPOINTS["customer_info"]
        driver.get(ENDPOINTS["customer_info"])

        assert "login" in login_page.get_current_url().lower()
        assert "ReturnUrl=%2fcustomer%2finfo" in login_page.get_current_url()
        assert login_page.is_login_box_visible(), "Login box should be visible on redirected page"
