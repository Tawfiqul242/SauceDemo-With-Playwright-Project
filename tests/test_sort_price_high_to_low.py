from pages.product_page import ProductPage

def test_sort_price_high_to_low(page, logged_in):
    # page class object
    product_page = ProductPage(page)

    expected_price = sorted(product_page.get_product_price(), reverse=True)

    product_page.sort_by_price_high_to_low()
    actual_price = product_page.get_product_price()

    assert actual_price == expected_price