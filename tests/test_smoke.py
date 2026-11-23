"""
Smoke test suite refactored with Page Object Model.
"""
import pytest
from pages.base_page import BasePage


@pytest.mark.smoke
class TestSmoke:
    """Baseline environment verification tests using POM."""

    def test_application_up_and_running(self, driver, base_url):
        """
        Verify that the Demo Web Shop homepage loads, displays expected title,
        and renders essential header navigation elements via BasePage.
        """
        base_page = BasePage(driver)
        base_page.open(base_url)

        # Assertions
        assert "Demo Web Shop" in base_page.get_title(), f"Title mismatch: {base_page.get_title()}"
        assert base_page.is_logo_visible(), "Header logo is not visible"
        assert base_page.is_register_link_visible(), "Register link is not visible"
        assert base_page.is_login_link_visible(), "Log in link is not visible"
        assert base_page.is_cart_link_visible(), "Shopping cart link is not visible"
        assert base_page.is_search_input_visible(), "Search input box is not visible"
