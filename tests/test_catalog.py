"""
Catalog test suite refactored with Page Object Model (CatalogPage).
Maps to manual test cases: TC-020, TC-040, TC-041, TC-043, TC-050.
"""
import pytest
from pages.catalog_page import CatalogPage


@pytest.mark.catalog
class TestCatalog:
    """Catalog browsing, search, and sorting tests using CatalogPage."""

    def test_top_level_categories_accessible(self, driver):
        """TC-020: Home page renders 7 top-level categories."""
        catalog_page = CatalogPage(driver)
        catalog_page.open_home()

        categories = catalog_page.get_top_level_category_names()
        expected_categories = [
            "BOOKS", "COMPUTERS", "ELECTRONICS",
            "APPAREL & SHOES", "DIGITAL DOWNLOADS",
            "JEWELRY", "GIFT CARDS"
        ]
        assert len(categories) >= 7, f"Expected at least 7 categories, got {len(categories)}"
        for expected in expected_categories:
            assert any(expected in cat for cat in categories), f"Missing category: {expected}"

    def test_search_with_matching_keyword(self, driver):
        """TC-040: Searching for 'computer' returns matching product items."""
        catalog_page = CatalogPage(driver)
        catalog_page.open_home()
        catalog_page.search_for("computer")

        count = catalog_page.get_search_results_count()
        assert count > 0, "Expected search results for 'computer', but none found"

    def test_search_with_no_matches(self, driver):
        """TC-041: Searching for non-existent term displays no products found message."""
        catalog_page = CatalogPage(driver)
        catalog_page.open_home()
        catalog_page.search_for("xyznonexistentterm999")

        message = catalog_page.get_no_results_text()
        assert "No products were found that matched your criteria." in message

    def test_search_case_insensitivity(self, driver):
        """TC-043: Searching with different casing returns consistent results."""
        catalog_page = CatalogPage(driver)

        # Lowercase search
        catalog_page.open_home()
        catalog_page.search_for("fiction")
        lower_count = catalog_page.get_search_results_count()
        assert lower_count > 0, "Lowercase search returned no results"

        # Uppercase search
        catalog_page.open_home()
        catalog_page.search_for("FICTION")
        upper_count = catalog_page.get_search_results_count()

        assert lower_count == upper_count, f"Case sensitivity mismatch: {lower_count} vs {upper_count}"

    def test_sort_products_by_name_a_to_z(self, driver):
        """TC-050: Sorting Books category by Name: A to Z orders products alphabetically."""
        catalog_page = CatalogPage(driver)
        catalog_page.open_category("books")
        catalog_page.sort_by("Name: A to Z")

        titles = catalog_page.get_displayed_product_titles()
        assert len(titles) >= 2, "Expected at least 2 products to verify sort order"
        assert titles == sorted(titles), f"Products not sorted A-Z: {titles}"
