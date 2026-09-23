import pytest
from playwright.sync_api import Page

class CartPage():
    """Page Object Model class for the Cart Page."""

    def __init__(self, page: Page):
        """
        Constructor that initializes the Playwright Page instance
        and defines all locators used on the Cart Page.
        """
        self.page = page

        # ===== Locators =====

        # click on remove button that is added to the cart

        self.remove_button = page.locator("button:has-text('Remove')")

    def remove_product_from_cart(self):
        try:
            while self.remove_button.count() > 0:
                self.remove_button.first.click()
        except Exception as e:
            print(f"Exception while removing product from cart: {e}")
            raise
