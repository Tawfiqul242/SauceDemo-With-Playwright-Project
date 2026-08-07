from playwright.sync_api import expect
from pages.product_page import ProductPage


# TC-009: Verify adding one product to cart
def test_add_one_product_to_cart(page, logged_in):
    # page class objects
    product_page = ProductPage(page)

    # Click Add to Cart on first product
    product_page.click_add_to_cart_btn_by_product_name("Sauce Labs Backpack")

    # Verify cart badge becomes 1.
    expect(product_page.CART_BADGE).to_have_text("1")

    # Button changes to Remove.
    expect(product_page.remove_btn_by_product_name("Sauce Labs Backpack")).to_be_visible()