"""
Pytest configuration and reusable fixtures for Demo Web Shop automation.
Provides WebDriver lifecycle, reusable preconditions, and failure reporting hooks.
"""
from pathlib import Path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pytest_html import extras

from config.config import BROWSER_BINARY, BASE_URL, PAGE_LOAD_TIMEOUT, DEMO_EMAIL, DEMO_PASSWORD
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from config.test_data import PRODUCT_DATA


def pytest_addoption(parser):
    """Add custom command-line options for test execution."""
    parser.addoption(
        "--headless",
        action="store_true",
        default=True,
        help="Run browser in headless mode (default: True)"
    )
    parser.addoption(
        "--no-headless",
        action="store_false",
        dest="headless",
        help="Run browser with visible UI"
    )


@pytest.fixture(scope="session")
def base_url():
    """Returns the application base URL."""
    return BASE_URL


@pytest.fixture(scope="function")
def driver(request):
    """
    Initializes and yields a configured Selenium WebDriver instance.
    Automatically shuts down the browser after each test.
    """
    is_headless = request.config.getoption("--headless")

    options = Options()
    if BROWSER_BINARY:
        options.binary_location = BROWSER_BINARY

    if is_headless:
        options.add_argument("--headless=new")

    # Standard Linux stability flags
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver_instance = webdriver.Chrome(options=options)
    driver_instance.set_page_load_timeout(PAGE_LOAD_TIMEOUT)

    yield driver_instance

    # Teardown
    driver_instance.quit()


@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """
    Reusable fixture providing an authenticated session.
    Logs in with test credentials and confirms authenticated state before test runs.
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(DEMO_EMAIL, DEMO_PASSWORD)
    assert login_page.is_logout_link_visible(), "Precondition failed: login unsuccessful"

    yield driver


@pytest.fixture(scope="function")
def cart_with_item(driver):
    """
    Reusable fixture that ensures the shopping cart contains one standard item.
    Guarantees clean cart teardown after the test finishes.
    """
    product_page = ProductPage(driver)
    product_page.open(PRODUCT_DATA["simple_book"]["slug"])
    product_page.add_to_cart()

    yield driver

    # Teardown: clear cart to avoid leftover state
    try:
        cart_page = CartPage(driver)
        cart_page.open()
        cart_page.clear_cart_if_not_empty()
    except Exception:
        pass


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture screenshot on test failure, save to disk, and attach to HTML report.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver_instance = item.funcargs.get("driver") or item.funcargs.get("logged_in_driver")
        if driver_instance:
            reports_dir = Path("reports/screenshots")
            reports_dir.mkdir(parents=True, exist_ok=True)
            screenshot_path = reports_dir / f"{item.name}_failed.png"
            driver_instance.save_screenshot(str(screenshot_path))

            # Attach to pytest-html report
            extra = getattr(report, "extra", [])
            extra.append(extras.image(str(screenshot_path)))
            report.extra = extra


def pytest_html_report_title(report):
    """Customize the title of the HTML test report."""
    report.title = "Demo Web Shop — QA Automation Test Report"


def pytest_metadata(metadata, config):
    """
    Customize the environment and test suite metadata displayed in the HTML report.
    """
    metadata["Project Name"] = "Demo Web Shop QA Automation Portfolio"
    metadata["QA Engineer"] = "Milan Dahal"
    metadata["Application Under Test"] = BASE_URL
    metadata["Browser"] = "Brave (Headless)" if BROWSER_BINARY else "Default Chrome"
    metadata["Automation Framework"] = "Selenium WebDriver 4.54 + Pytest 9.2"
    metadata["Design Pattern"] = "Page Object Model (POM)"
    metadata["Environment"] = "Public Demo Store"

    # Clean up verbose system environment variables from report table
    for noisy_key in ["JAVA_HOME", "SHELL", "PWD"]:
        metadata.pop(noisy_key, None)

