from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page:Page):
        self.page = page

        self.CHECKOUT_PAGE_TITLE = page.locator(".title")
        self.FNAME = page.get_by_role("textbox", name="First Name")
        self.LNAME = page.get_by_role("textbox", name="Last Name")
        self.ZIPCODE = page.get_by_role("textbox", name="Zip/Postal Code")
        self.CONTINUE_BTN = page.locator("[data-test='continue']")

    
    def fill_chekout_info(self, fname, lname, zipcode):
        self.FNAME.fill(fname)
        self.LNAME.fill(lname)
        self.ZIPCODE.fill(str(zipcode))