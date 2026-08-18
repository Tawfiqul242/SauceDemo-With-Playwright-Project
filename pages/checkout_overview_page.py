from playwright.sync_api import Page

class CheckoutOverviewPage:
    def __init__(self, page:Page):
        self.page = page

        self.OVERVIEW_TITLE =  page.locator(".title")