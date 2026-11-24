"""
Authentication test suite refactored with centralized test data and parametrization.
Maps to manual test cases: TC-010, TC-011, TC-012, TC-014, TC-130.
"""
import pytest
from pages.login_page import LoginPage
from config.test_data import TEST_USER, INVALID_CREDENTIALS, ENDPOINTS


@pytest.mark.auth
class TestAuthentication:
    """Authentication tests utilizing centralized test data and parameterization."""

    def test_login_with_valid_credentials(self, driver):
        """TC-010: Successful login renders account email and logout button."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(TEST_USER["email"], TEST_USER["password"])

        assert login_page.get_account_email() == TEST_USER["email"]
        assert login_page.is_logout_link_visible()

    @pytest.mark.parametrize(
        "cred",
        INVALID_CREDENTIALS,
        ids=[c["id"] for c in INVALID_CREDENTIALS]
    )
    def test_login_with_invalid_credentials(self, driver, cred):
        """
        Data-driven test for authentication errors.
        - TC-011: Login with invalid password
        - TC-012: Login with unregistered email
        """
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(cred["email"], cred["password"])

        error_text = login_page.get_error_summary_text()
        assert cred["expected_error"] in error_text, (
            f"[{cred['manual_tc']}] Expected '{cred['expected_error']}' in error summary, got: '{error_text}'"
        )

    def test_logout_terminates_session(self, driver):
        """TC-014: Logging out restores header to unauthenticated state."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(TEST_USER["email"], TEST_USER["password"])

        login_page.click_logout()

        assert login_page.is_login_link_visible(), "Log in link should be visible after logout"
        assert login_page.is_register_link_visible(), "Register link should be visible after logout"

    def test_unauthenticated_protected_page_redirect(self, driver):
        """TC-130: Accessing protected customer info while signed out redirects to login."""
        login_page = LoginPage(driver)
        driver.get(ENDPOINTS["customer_info"])

        assert "login" in login_page.get_current_url().lower()
        assert "ReturnUrl=%2fcustomer%2finfo" in login_page.get_current_url()
        assert login_page.is_login_box_visible(), "Login box should be visible on redirected page"
