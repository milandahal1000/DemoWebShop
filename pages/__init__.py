"""
Page Objects package exports.
"""
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

__all__ = [
    "BasePage",
    "LoginPage",
    "CatalogPage",
    "ProductPage",
    "CartPage",
    "CheckoutPage",
]
