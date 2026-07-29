from pages.product_page import ProductPage

def test_sort_z_to_a(page, logged_in):
    # page class object
    product_page = ProductPage(page)

    expected_names = sorted(product_page.get_product_names(), reverse=True)

    product_page.sort_name_by_decending()
    actual_names = product_page.get_product_names()

    assert actual_names == expected_names