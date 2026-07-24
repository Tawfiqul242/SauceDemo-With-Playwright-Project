from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        # locators
        self.USER_NAME = page.get_by_role('textbox', name= "Username")
        self.PASSWORD = page.get_by_role("textbox", name="Password")
        self.LOGIN_BTN = page.get_by_role("button")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def fill_login_form(self, username, password):
        self.USER_NAME.fill(username)
        self.PASSWORD.fill(password)

    def click_login_btn(self):
        self.LOGIN_BTN.click()

