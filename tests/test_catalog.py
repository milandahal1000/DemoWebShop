"""
Catalog test suite refactored with centralized test data and parametrization.
Maps to manual test cases: TC-020, TC-040, TC-041, TC-043, TC-050.
"""
import pytest
from pages.catalog_page import CatalogPage
from config.test_data import TOP_LEVEL_CATEGORIES, SEARCH_DATA


@pytest.mark.catalog
class TestCatalog:
    """Catalog browsing, keyword search, and sorting tests using centralized data."""

    def test_top_level_categories_accessible(self, driver):
        """TC-020: Home page renders all 7 top-level categories."""
        catalog_page = CatalogPage(driver)
        catalog_page.open_home()

        categories = catalog_page.get_top_level_category_names()
        assert len(categories) >= len(TOP_LEVEL_CATEGORIES), (
            f"Expected at least {len(TOP_LEVEL_CATEGORIES)} categories, got {len(categories)}"
        )
        for expected in TOP_LEVEL_CATEGORIES:
            assert any(expected in cat for cat in categories), f"Missing category: {expected}"

    @pytest.mark.parametrize("keyword", SEARCH_DATA["matching_keywords"])
    def test_search_with_matching_keyword(self, driver, keyword):
        """TC-040: Data-driven keyword search returns matching product items."""
        catalog_page = CatalogPage(driver)
        catalog_page.open_home()
        catalog_page.search_for(keyword)

        count = catalog_page.get_search_results_count()
        assert count > 0, f"Expected search results for keyword '{keyword}', but found none"

    def test_search_with_no_matches(self, driver):
        """TC-041: Searching for non-existent term displays no products found message."""
        catalog_page = CatalogPage(driver)
        catalog_page.open_home()
        catalog_page.search_for(SEARCH_DATA["non_matching_keyword"])

        message = catalog_page.get_no_results_text()
        assert SEARCH_DATA["no_results_message"] in message

    def test_search_case_insensitivity(self, driver):
        """TC-043: Searching with different casing returns consistent results."""
        catalog_page = CatalogPage(driver)
        term_lower, term_upper = SEARCH_DATA["case_sensitivity_pair"]

        # Lowercase search
        catalog_page.open_home()
        catalog_page.search_for(term_lower)
        lower_count = catalog_page.get_search_results_count()
        assert lower_count > 0, f"Lowercase search for '{term_lower}' returned no results"

        # Uppercase search
        catalog_page.open_home()
        catalog_page.search_for(term_upper)
        upper_count = catalog_page.get_search_results_count()

        assert lower_count == upper_count, (
            f"Case sensitivity mismatch: '{term_lower}' returned {lower_count}, '{term_upper}' returned {upper_count}"
        )

    def test_sort_products_by_name_a_to_z(self, driver):
        """TC-050: Sorting Books category by Name: A to Z orders products alphabetically."""
        catalog_page = CatalogPage(driver)
        catalog_page.open_category("books")
        catalog_page.sort_by("Name: A to Z")

        titles = catalog_page.get_displayed_product_titles()
        assert len(titles) >= 2, "Expected at least 2 products to verify sort order"
        assert titles == sorted(titles), f"Products not sorted A-Z: {titles}"
