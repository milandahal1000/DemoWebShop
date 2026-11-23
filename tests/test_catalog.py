"""
Automated tests for Catalog Navigation, Search, and Product Sorting.
Maps to manual test cases:
- TC-020: Category navigation renders top-level categories
- TC-040: Search with matching term displays relevant results
- TC-041: Search with non-matching term displays empty results notice
- TC-043: Search is case-insensitive
- TC-050: Sorting category products by Name: A to Z
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from config.config import BASE_URL, EXPLICIT_WAIT


@pytest.mark.catalog
class TestCatalog:
    """Test suite covering catalog browsing, keyword search, and sorting."""

    def test_top_level_categories_accessible(self, driver):
        """TC-020: Home page renders 7 top-level categories."""
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, EXPLICIT_WAIT)

        menu = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.top-menu"))
        )
        category_links = menu.find_elements(By.XPATH, "./li/a")
        category_names = [c.text.strip() for c in category_links if c.text.strip()]

        expected_categories = [
            "BOOKS", "COMPUTERS", "ELECTRONICS",
            "APPAREL & SHOES", "DIGITAL DOWNLOADS",
            "JEWELRY", "GIFT CARDS"
        ]
        assert len(category_names) >= 7, f"Expected at least 7 categories, got {len(category_names)}"
        for expected in expected_categories:
            assert any(expected in cat for cat in category_names), f"Missing category: {expected}"

    def test_search_with_matching_keyword(self, driver):
        """TC-040: Searching for 'computer' returns matching product items."""
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, EXPLICIT_WAIT)

        search_input = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        search_input.clear()
        search_input.send_keys("computer")
        driver.find_element(By.CSS_SELECTOR, "input.search-box-button").click()

        # Verify results container
        results = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.search-results"))
        )
        product_items = results.find_elements(By.CSS_SELECTOR, "div.product-item")
        assert len(product_items) > 0, "Expected search results for 'computer', but none found"

    def test_search_with_no_matches(self, driver):
        """TC-041: Searching for non-existent term displays no products found message."""
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, EXPLICIT_WAIT)

        search_input = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        search_input.clear()
        search_input.send_keys("xyznonexistentterm999")
        driver.find_element(By.CSS_SELECTOR, "input.search-box-button").click()

        result_message = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "strong.result"))
        )
        assert "No products were found that matched your criteria." in result_message.text

    def test_search_case_insensitivity(self, driver):
        """TC-043: Searching with different casing returns consistent results."""
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, EXPLICIT_WAIT)

        # Lowercase search
        search_input = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        search_input.clear()
        search_input.send_keys("fiction")
        driver.find_element(By.CSS_SELECTOR, "input.search-box-button").click()

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.search-results")))
        lower_items = driver.find_elements(By.CSS_SELECTOR, "div.product-item")
        lower_count = len(lower_items)
        assert lower_count > 0, "Lowercase search returned no results"

        # Uppercase search
        search_input = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        search_input.clear()
        search_input.send_keys("FICTION")
        driver.find_element(By.CSS_SELECTOR, "input.search-box-button").click()

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.search-results")))
        upper_items = driver.find_elements(By.CSS_SELECTOR, "div.product-item")
        upper_count = len(upper_items)

        assert lower_count == upper_count, f"Case sensitivity mismatch: {lower_count} vs {upper_count}"

    def test_sort_products_by_name_a_to_z(self, driver):
        """TC-050: Sorting Books category by Name: A to Z orders products alphabetically."""
        driver.get(f"{BASE_URL}books")
        wait = WebDriverWait(driver, EXPLICIT_WAIT)

        # Select 'Name: A to Z' from sort dropdown
        sort_dropdown = wait.until(EC.visibility_of_element_located((By.ID, "products-orderby")))
        select = Select(sort_dropdown)
        select.select_by_visible_text("Name: A to Z")

        # Wait for page reload/update
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-grid")))
        product_titles = [
            elem.text.strip()
            for elem in driver.find_elements(By.CSS_SELECTOR, "h2.product-title a")
        ]
        assert len(product_titles) >= 2, "Expected at least 2 products to verify sort order"
        assert product_titles == sorted(product_titles), f"Products not sorted A-Z: {product_titles}"
