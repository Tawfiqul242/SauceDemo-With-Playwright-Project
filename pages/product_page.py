from playwright.sync_api import Page

class ProductPage:
    def __init__(self, page: Page):
        self.page = page

        #locators
        self.PRODUCTS_TITLE = page.get_by_text("Products", exact=True)
        self.PRODUCTS = page.locator("div.inventory_list").locator("div")
        self.MENU = page.get_by_role("button", name="Open Menu")
        self.LOGOUT_BTN = page.get_by_role("link", name="Logout")

    def click_menu(self):
        self.MENU.click()

    def click_logout_btn(self):
        self.LOGOUT_BTN.click()

    