from playwright.sync_api import Page

class Product_Details_Page:
    def __init__(self, page: Page):
        self.page = page

        self.BACK_TO_PRODUCT_BTN = page.get_by_role("button", name="Back to products")
        self.PRODUCT_NAME = page.locator("[data-test='inventory-item-name']")
        self.PRODUCT_DESCRIPTION = page.locator("[data-test='inventory-item-desc']")
        self.PRODUCT_PRICE = page.locator(".inventory_details_price")
        self.ADD_TO_CART_BTN = page.get_by_role("button", name="Add to cart")

    def click_back_to_product_btn(self):
        self.BACK_TO_PRODUCT_BTN.click()

    def get_product_name(self):
        return self.PRODUCT_NAME.inner_text()

    def get_product_description(self):
            return self.PRODUCT_DESCRIPTION.inner_text()

    def get_product_price(self):
        return self.PRODUCT_PRICE.inner_text()

    