import pytest
from playwright.sync_api import Page, expect
from pages.cart_page import CartPage
from pages.products_page import ProductsPage
from pages.user_login import Login
from config import Config

def test_remove_product_from_cart(page):

    # Perform login

    login = Login(page)
    login.fill_username(Config.valid_username)
    login.fill_password(Config.valid_password)
    login.login_button_click()

    products_page = ProductsPage(page)

    # Add all products to the cart
    products_page.add_multiple_products_to_cart()

    # click on cart icon button once the items are added to the cart
    products_page.click_cart_icon()


    # Remove a product from the cart

    cart_page = CartPage(page)
    cart_page.remove_product_from_cart()

    # Verify that the product count in the cart is now 0
    assert products_page.cart_count() == 0

