from playwright.sync_api import expect
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

# TC-015: Verify checkout page opens
def test_verify_checkout_page_opens(page, logged_in):
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    checkOut_page = CheckoutPage(page)

    # Cart contains at least one product.
    product_page.click_add_to_cart_btn_by_product_name("Sauce Labs Bolt T-Shirt")

    # Open cart.
    product_page.CART_LINK.click()

    # Click Checkout.
    cart_page.CHECKOUT_BTN.click()

    # Verify Checkout information page displayed.
    expect(checkOut_page.CHECKOUT_PAGE_TITLE).to_be_visible()
