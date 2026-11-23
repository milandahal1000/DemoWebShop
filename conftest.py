"""
Pytest configuration and reusable fixtures for Demo Web Shop automation.
Configures WebDriver lifecycle, CLI arguments, and HTML test report enhancements.
"""
from pathlib import Path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.config import BROWSER_BINARY, BASE_URL, PAGE_LOAD_TIMEOUT


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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture screenshot on test failure and save to reports/screenshots/.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver_instance = item.funcargs.get("driver", None)
        if driver_instance:
            reports_dir = Path("reports/screenshots")
            reports_dir.mkdir(parents=True, exist_ok=True)
            screenshot_path = reports_dir / f"{item.name}_failed.png"
            driver_instance.save_screenshot(str(screenshot_path))
