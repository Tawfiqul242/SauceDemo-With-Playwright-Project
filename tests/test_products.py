from playwright.sync_api import expect
from pages.product_page import ProductPage

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


