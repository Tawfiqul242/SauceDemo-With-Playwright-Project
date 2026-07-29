from playwright.sync_api import expect
from pages.product_page import ProductPage
from pages.product_details_page import Product_Details_Page

def test_product_details(page, logged_in):
    # page class objects
    product_page = ProductPage(page)
    product_details = Product_Details_Page(page)

    products = product_page.get_products()

    expected_name = products[0]["name"].inner_text()
    expected_description = products[0]["description"].inner_text()
    expected_price = products[0]["price"].inner_text()

    # select product to see product details
    product_page.click_on_product_name_by_index(0)

    # verify Product detail page opens
    expect(product_details.PRODUCT_NAME).to_be_visible()

    # Verify Correct name displayed.
    expect(product_details.PRODUCT_NAME).to_have_text(expected_name)

    # Verify Correct description displayed.
    expect(product_details.PRODUCT_DESCRIPTION).to_have_text(expected_description)

    # Verify Correct price displayed.
    expect(product_details.PRODUCT_PRICE).to_have_text(expected_price)

    # Verify Add to Cart button visible.
    expect(product_details.ADD_TO_CART_BTN).to_be_visible()


