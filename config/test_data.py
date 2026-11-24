"""
Centralized test data, application endpoints, and reusable test constants.
Separates data management from test logic and page interactions.
"""
from config.config import DEMO_EMAIL, DEMO_PASSWORD, BASE_URL

# Test User Credentials
TEST_USER = {
    "email": DEMO_EMAIL,
    "password": DEMO_PASSWORD,
    "first_name": "Milan",
    "last_name": "Dahal",
}

# Invalid Credentials for Authentication Testing
INVALID_CREDENTIALS = [
    {
        "id": "wrong_password",
        "email": DEMO_EMAIL,
        "password": "WrongPassword999!",
        "expected_error": "The credentials provided are incorrect",
        "manual_tc": "TC-011",
    },
    {
        "id": "unregistered_email",
        "email": "nonexistent.user.2026@example.com",
        "password": "SomePassword123",
        "expected_error": "No customer account found",
        "manual_tc": "TC-012",
    },
]

# Application URLs and Endpoints
ENDPOINTS = {
    "home": BASE_URL,
    "login": f"{BASE_URL}login",
    "register": f"{BASE_URL}register",
    "cart": f"{BASE_URL}cart",
    "wishlist": f"{BASE_URL}wishlist",
    "compare": f"{BASE_URL}compareproducts",
    "contact_us": f"{BASE_URL}contactus",
    "customer_info": f"{BASE_URL}customer/info",
    "customer_orders": f"{BASE_URL}customer/orders",
    "customer_addresses": f"{BASE_URL}customer/addresses",
    "change_password": f"{BASE_URL}customer/changepassword",
    "onepagecheckout": f"{BASE_URL}onepagecheckout",
}

# Catalog and Navigation Data
TOP_LEVEL_CATEGORIES = [
    "BOOKS",
    "COMPUTERS",
    "ELECTRONICS",
    "APPAREL & SHOES",
    "DIGITAL DOWNLOADS",
    "JEWELRY",
    "GIFT CARDS",
]

# Search Test Data
SEARCH_DATA = {
    "matching_keywords": ["computer", "fiction"],
    "non_matching_keyword": "xyznonexistentterm999",
    "no_results_message": "No products were found that matched your criteria.",
    "case_sensitivity_pair": ("fiction", "FICTION"),
}

# Product Test Data
PRODUCT_DATA = {
    "simple_book": {
        "slug": "computing-and-internet",
        "name": "Computing and Internet",
        "unit_price": "10.00",
        "double_qty_subtotal": "20.00",
    }
}

# Shopping Cart Constants
CART_DATA = {
    "empty_message": "Your Shopping Cart is empty!",
    "max_qty_input": "99999",
    "max_qty_error": "The maximum quantity allowed for purchase is 10000.",
}

# Checkout Constants
CHECKOUT_DATA = {
    "tos_warning": "Please accept the terms of service before the next step.",
    "billing_address": {
        "first_name": "Test",
        "last_name": "Address",
        "email": DEMO_EMAIL,
        "country": "United States",
        "state": "California",
        "city": "San Jose",
        "address1": "100 Innovation Way",
        "zip": "95134",
        "phone": "4081234567",
    },
}
