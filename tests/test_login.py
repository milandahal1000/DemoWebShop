"""
Automated tests for Authentication & Session management.
Maps to manual test cases:
- TC-010: Login with valid credentials
- TC-011: Login with invalid password
- TC-012: Login with unregistered email
- TC-014: Logout terminates session
- TC-130: Protected page redirection for unauthenticated visitors
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import DEMO_EMAIL, DEMO_PASSWORD, EXPLICIT_WAIT
from config.test_data import ENDPOINTS


@pytest.mark.auth
class TestAuthentication:
    """Test suite covering user login, logout, and protected route access."""

    def test_login_with_valid_credentials(self, driver):
        """TC-010: Successful login renders account email and logout button."""
        driver.get(ENDPOINTS["login"])
        wait = WebDriverWait(driver, EXPLICIT_WAIT)

        # Enter credentials and submit
        driver.find_element(By.ID, "Email").send_keys(DEMO_EMAIL)
        driver.find_element(By.ID, "Password").send_keys(DEMO_PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "input.login-button").click()

        # Verify authenticated state
        account_link = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.header-links a.account"))
        )
        logout_link = driver.find_element(By.CSS_SELECTOR, "div.header-links a.ico-logout")

        assert account_link.text == DEMO_EMAIL, f"Expected {DEMO_EMAIL}, got {account_link.text}"
        assert logout_link.is_displayed(), "Logout link is not visible"

    def test_login_with_invalid_password(self, driver):
        """TC-011: Login fails when password is incorrect."""
        driver.get(ENDPOINTS["login"])
        wait = WebDriverWait(driver, EXPLICIT_WAIT)

        driver.find_element(By.ID, "Email").send_keys(DEMO_EMAIL)
        driver.find_element(By.ID, "Password").send_keys("WrongPassword999!")
        driver.find_element(By.CSS_SELECTOR, "input.login-button").click()

        error_summary = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.validation-summary-errors"))
        )
        assert "The credentials provided are incorrect" in error_summary.text

    def test_login_with_unregistered_email(self, driver):
        """TC-012: Login fails with message when email is unregistered."""
        driver.get(ENDPOINTS["login"])
        wait = WebDriverWait(driver, EXPLICIT_WAIT)

        driver.find_element(By.ID, "Email").send_keys("nonexistent.user.2026@example.com")
        driver.find_element(By.ID, "Password").send_keys("SomePassword123")
        driver.find_element(By.CSS_SELECTOR, "input.login-button").click()

        error_summary = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.validation-summary-errors"))
        )
        assert "No customer account found" in error_summary.text

    def test_logout_terminates_session(self, driver):
        """TC-014: Logging out restores header to unauthenticated state."""
        driver.get(ENDPOINTS["login"])
        wait = WebDriverWait(driver, EXPLICIT_WAIT)

        # Login
        driver.find_element(By.ID, "Email").send_keys(DEMO_EMAIL)
        driver.find_element(By.ID, "Password").send_keys(DEMO_PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "input.login-button").click()

        logout_link = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.header-links a.ico-logout"))
        )
        logout_link.click()

        # Verify unauthenticated header
        login_link = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.header-links a.ico-login"))
        )
        register_link = driver.find_element(By.CSS_SELECTOR, "div.header-links a.ico-register")

        assert login_link.is_displayed(), "Log in link should be visible after logout"
        assert register_link.is_displayed(), "Register link should be visible after logout"

    def test_unauthenticated_protected_page_redirect(self, driver):
        """TC-130: Accessing /customer/info while signed out redirects to login."""
        driver.get(ENDPOINTS["customer_info"])
        wait = WebDriverWait(driver, EXPLICIT_WAIT)

        wait.until(EC.url_contains("/login?ReturnUrl=%2fcustomer%2finfo"))
        login_box = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.returning-wrapper"))
        )
        assert login_box.is_displayed(), "Login box should be visible on redirected page"
        assert "login" in driver.current_url.lower()
