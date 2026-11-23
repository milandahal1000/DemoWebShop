"""
Centralized test data and endpoint constants.
"""
from config.config import DEMO_EMAIL, DEMO_PASSWORD, BASE_URL

# Test User Credentials
TEST_USER = {
    "email": DEMO_EMAIL,
    "password": DEMO_PASSWORD,
    "first_name": "Milan",
    "last_name": "Dahal",
}

# Key Application Endpoints
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
}
