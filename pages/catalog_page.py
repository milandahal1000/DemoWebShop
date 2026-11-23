"""
CatalogPage object representing category listings, search, and sorting.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from config.config import BASE_URL


class CatalogPage(BasePage):
    """Page object for product browsing, keyword search, and sorting."""

    TOP_MENU_LINKS = (By.XPATH, "//ul[contains(@class, 'top-menu')]/li/a")
    SEARCH_INPUT = (By.ID, "small-searchterms")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input.search-box-button")
    SEARCH_RESULTS_CONTAINER = (By.CSS_SELECTOR, "div.search-results")
    PRODUCT_ITEMS = (By.CSS_SELECTOR, "div.product-item")
    NO_RESULTS_MESSAGE = (By.CSS_SELECTOR, "strong.result")
    SORT_DROPDOWN = (By.ID, "products-orderby")
    PRODUCT_GRID = (By.CSS_SELECTOR, "div.product-grid")
    PRODUCT_TITLES = (By.CSS_SELECTOR, "h2.product-title a")

    def open_home(self):
        super().open(BASE_URL)

    def open_category(self, slug):
        super().open(f"{BASE_URL}{slug}")

    def get_top_level_category_names(self):
        links = self.find_all(self.TOP_MENU_LINKS)
        return [l.text.strip() for l in links if l.text.strip()]

    def search_for(self, keyword):
        self.type(self.SEARCH_INPUT, keyword)
        self.click(self.SEARCH_BUTTON)
        # Wait for search results container or no-results message
        self.wait.until(
            lambda d: d.find_elements(*self.SEARCH_RESULTS_CONTAINER)
            or d.find_elements(*self.NO_RESULTS_MESSAGE)
        )

    def get_search_results_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))

    def get_no_results_text(self):
        return self.get_text(self.NO_RESULTS_MESSAGE)

    def sort_by(self, visible_text):
        dropdown = self.find(self.SORT_DROPDOWN)
        Select(dropdown).select_by_visible_text(visible_text)
        self.find(self.PRODUCT_GRID)

    def get_displayed_product_titles(self):
        elements = self.find_all(self.PRODUCT_TITLES)
        return [elem.text.strip() for elem in elements]
