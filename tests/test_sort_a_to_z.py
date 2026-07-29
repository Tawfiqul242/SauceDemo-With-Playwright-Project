from playwright.sync_api import expect
from pages.product_page import ProductPage

def test_sort_a_to_z(page, logged_in):
    #page class objects
    product_page = ProductPage(page)

    expected_names = sorted(product_page.get_product_names())

    product_page.sort_name_by_ascending()
    actual_names = product_page.get_product_names()

    assert expected_names == actual_names