import pytest
from playwright.sync_api import Page, expect

class Login():
    def __init__(self, page: Page):
        self.page = page

    # grab the user name and password locator

        self.username_text=self.page.locator("#user-name")
        self.password_text=self.page.locator("#password")

    # click on login link
        self.login_button=self.page.locator("#login-button")

    # action we have to perform

    def fill_username(self,username:str):
        try:
            self.username_text.fill(username)
        except Exception as e:
            print(f"Username not found: {e}")

    def fill_password(self,password:str):
        try:
            self.password_text.fill(password)
        except Exception as e:
            print(f"Password not found: {e}")

    def login_button_click(self):
        self.login_button.click()