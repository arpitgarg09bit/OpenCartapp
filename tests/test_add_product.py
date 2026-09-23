import pytest
from playwright.sync_api import Page, expect
from pages.products_page import ProductsPage
from pages.user_login import Login
from config import Config


def test_add_product_to_cart(page):
    """
    Test to verify that multiple products can be added to the cart successfully.
    """

    # Perform login
    login = Login(page)
    login.fill_username(Config.valid_username)
    login.fill_password(Config.valid_password)
    login.login_button_click()

    # Initialize ProductsPage
    products_page = ProductsPage(page)

    # Add all products
    products_page.add_multiple_products_to_cart()

    # Click cart icon
    products_page.click_cart_icon()

    # Verify all 6 products are present in the cart
    assert products_page.cart_count() == 6




