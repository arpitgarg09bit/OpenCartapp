import pytest
from playwright.sync_api import Page

class ProductsPage():
    """Page Object Model class for the Products Page."""

    def __init__(self, page: Page):
        """
        Constructor that initializes the Playwright Page instance
        and defines all locators used on the Products Page.
        """
        self.page = page

        # ===== Locators =====
        # Using CSS selectors to locate elements on the Products page.

        self.product_list = page.locator('.inventory_list')

        self.product_items = page.locator('.inventory_item')

        self.add_to_cart_buttons = page.get_by_role("button",name="Add to cart")

        self.cart_icon = page.locator('.shopping_cart_link')

    def add_multiple_products_to_cart(self):
        """
        Add all products displayed on the Products page to the cart.
        """
        try:
            while self.add_to_cart_buttons.count() > 0:
                self.add_to_cart_buttons.first.click()
        except Exception as e:
            print(f" Exception while adding multiple products to cart: {e}")
            raise

    def click_cart_icon(self):
        """
        Click the cart icon.
        """
        try:
            self.cart_icon.click()
        except Exception as e:
            print(f" Exception while clicking 'Cart' icon: {e}")
            raise

    def cart_count(self):
        """
        Return the count of items in the cart.
        """
        try:
            return self.page.locator('.cart_quantity').count()
        except Exception as e:
            print(f" Exception while getting cart count: {e}")
            raise



