from playwright.sync_api import expect
from pages.product_page import ProductPage
from pages.product_details_page import Product_Details_Page

# TC-003: Verify all products are displayed
def test_all_product_displayed(page, logged_in):
    #class objects
    product_page = ProductPage(page)

    products = product_page.get_products()
    # verify 6 products are displayed
    assert len(products) == 6, f"Expected 6 products but found {len(products)}"

    #verify each product contains required information
    for product in products:
        expect(product["image"]).to_be_visible()
        expect(product["name"]).to_be_visible()
        expect(product["description"]).to_be_visible()
        expect(product["price"]).to_be_visible()
        expect(product["add_to_cart"]).to_be_visible()


# TC-004: Verify product details page
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


#TC-010: Verify adding multiple products
def test_add_multiple_products_in_cart(page, logged_in):

    #page class objects
    product_page = ProductPage(page)

    #Add three different products.
    product_page.click_add_to_cart_btn_by_product_name("Sauce Labs Backpack")
    product_page.click_add_to_cart_btn_by_product_name("Sauce Labs Bike Light")
    product_page.click_add_to_cart_btn_by_product_name("Sauce Labs Bolt T-Shirt")

    # Verify Cart badge shows 3.
    expect(product_page.CART_BADGE).to_have_text("3")