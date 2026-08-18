from playwright.sync_api import expect
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.read_json import load_json
from pages.checkout_overview_page import CheckoutOverviewPage

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


# TC-016: Verify checkout with valid information
def test_veiry_checkout_with_valid_info(page, logged_in):
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    checkOut_page = CheckoutPage(page)
    check_overview_page = CheckoutOverviewPage(page)
    
    # Cart contains at least one product.
    product_page.click_add_to_cart_btn_by_product_name("Sauce Labs Bolt T-Shirt")
    
    # Open cart.
    product_page.CART_LINK.click()
    
    # Click Checkout.
    cart_page.CHECKOUT_BTN.click()

    # Enter Chekcout Information
    info = load_json("test_data/checkoutInfo.json")["valid_checkout"]

    checkOut_page.fill_chekout_info(info["fname"], info["lname"], info["zipcode"])

    # Click Continue.
    checkOut_page.CONTINUE_BTN.click()

    # Verify checkout Overview page displayed.
    expect(check_overview_page.OVERVIEW_TITLE).to_be_visible()
