"""
Phase 3 Automation Smoke Test.
Validates:
1. WebDriver launches successfully.
2. Application loads at base URL.
3. Page title and key header elements render properly.
4. Clean browser teardown.
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import EXPLICIT_WAIT


@pytest.mark.smoke
class TestSmoke:
    """Baseline environment verification tests."""

    def test_application_up_and_running(self, driver, base_url):
        """
        Verify that the Demo Web Shop homepage loads, displays the expected title,
        and renders essential header navigation links.
        """
        driver.get(base_url)

        # 1. Title verification
        assert "Demo Web Shop" in driver.title, f"Expected 'Demo Web Shop' in title, got: {driver.title}"

        # 2. Header logo verification
        wait = WebDriverWait(driver, EXPLICIT_WAIT)
        logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.header-logo a")))
        assert logo.is_displayed(), "Header logo is not visible"

        # 3. Essential header links verification
        register_link = driver.find_element(By.CSS_SELECTOR, "a.ico-register")
        login_link = driver.find_element(By.CSS_SELECTOR, "a.ico-login")
        cart_link = driver.find_element(By.CSS_SELECTOR, "a.ico-cart")

        assert register_link.is_displayed(), "Register link is not visible"
        assert login_link.is_displayed(), "Log in link is not visible"
        assert cart_link.is_displayed(), "Shopping cart link is not visible"

        # 4. Search box verification
        search_box = driver.find_element(By.ID, "small-searchterms")
        assert search_box.is_displayed(), "Search input box is not visible"
