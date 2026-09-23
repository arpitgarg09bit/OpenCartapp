import pytest
from playwright.sync_api import Page, expect
from pages.user_login import Login
from config import Config
from pages.products_page import ProductsPage



def test_valid_login_page(page):

    # Find the username and password fields
    login = Login(page)

    # Fill in the username and password
    login.fill_username(Config.valid_username)
    login.fill_password(Config.valid_password)

    # Click the login button
    login.login_button_click()

    # Assert that the login was successful
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page).to_have_title("Swag Labs")
    expect(page.locator('.inventory_list')).to_be_visible()


@pytest.mark.skip
def test_invalid_login_page(page):

    # Find the username and password fields
    login = Login(page)

    # Fill in the username and password
    login.fill_username(Config.invalid_username)
    login.fill_password(Config.invalid_password)

    # Click the login button
    login.login_button_click()

    # Assert that the login was successful
    expect(page.locator("[data-test='error']")).to_be_visible()


