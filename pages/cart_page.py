from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page

        self.CART_ITEM = page.locator(".cart_item")
        self.ITEM_QTY = page.locator(".cart_quantity")
        self.ITEM_NAME = page.locator(".inventory_item_name")
        self.ITEM_PRICE = page.locator(".inventory_item_price")
        self.CONTINUE_BTN = page.get_by_role("button", name="Continue Shopping")

    def get_cart_product_by_name(self, product_name):
        return self.ITEM_NAME.filter(
            has_text= product_name             
        )
    
    def get_cart_product_price_by_name(self, product_name):
        return self.CART_ITEM.filter(
            has_text= product_name
        ).locator(".inventory_item_price")

    def get_cart_product_qty_by_name(self, product_name):
        return self.CART_ITEM.filter(
            has_text= product_name
        ).locator(".cart_quantity")

    def click_remove_btn_by_product_name(self, product_name):
        self.CART_ITEM.filter(
            has_text= product_name
        ).get_by_role("button", name="Remove").click()