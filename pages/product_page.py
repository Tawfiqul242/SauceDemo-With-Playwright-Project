from playwright.sync_api import Page

class ProductPage:
    def __init__(self, page: Page):
        self.page = page

        #locators
        self.PRODUCTS_TITLE = page.get_by_text("Products", exact=True)
        self.PRODUCTS = page.locator(".inventory_item")
        self.MENU = page.get_by_role("button", name="Open Menu")
        self.LOGOUT_BTN = page.get_by_role("link", name="Logout")
        self.IMAGE = page.locator("img.inventory_item_img")
        self.ITEM_NAME = page.locator(".inventory_item_name")
        self.ITEM_DESCRIPTION = page.locator("[data-test='inventory-item-desc']")
        self.ITEM_PRICE = page.locator(".inventory_item_price")
        self.ADD_TO_CART_BTN = page.get_by_role("button", name="Add to cart")
        self.SORT_DROPDOWN = page.locator("[data-test='product-sort-container']")
        self.CART_BADGE = page.locator(".shopping_cart_badge")
        self.CART_LINK = page.locator("a.shopping_cart_link")

    def click_menu(self):
        self.MENU.click()

    def click_logout_btn(self):
        self.LOGOUT_BTN.click()

    def click_on_product_name_by_index(self, index):
        self.PRODUCTS.nth(index).locator(".inventory_item_name").click()


    def get_products(self):
        products = []

        for item in self.PRODUCTS.all():
            products.append({
                "image": item.get_by_role("img"),
                "name": item.locator(".inventory_item_name"),
                "description": item.locator("[data-test='inventory-item-desc']"),
                "price": item.locator(".inventory_item_price"),
                "add_to_cart": item.get_by_role("button", name="Add to cart")
                })
        return products

    def sort_name_by_ascending(self):
        self.SORT_DROPDOWN.select_option("az")

    def get_product_names(self):
        return self.ITEM_NAME.all_inner_texts()

    def sort_name_by_decending(self):
        self.SORT_DROPDOWN.select_option("za")

    def sort_by_price_low_to_high(self):
        self.SORT_DROPDOWN.select_option("lohi")

    def get_product_price(self):
        prices = self.ITEM_PRICE.all_inner_texts()
        return [float(price.replace("$", "")) for price in prices]

    def sort_by_price_high_to_low(self):
        self.SORT_DROPDOWN.select_option("hilo")

    def get_add_to_add_btn_by_product_name(self, product_name):
        return self.PRODUCTS.filter(
            has = self.page.locator(".inventory_item_name" , has_text=product_name)
        ).get_by_role("button", name="Add to cart")

    def click_add_to_cart_btn_by_product_name(self, product_name):
        self.get_add_to_add_btn_by_product_name(product_name).click()

    def remove_btn_by_product_name(self, product_name):
        return self.PRODUCTS.filter(
            has= self.page.locator(".inventory_item_name" , has_text=product_name)
        ).get_by_role("button", name="Remove")