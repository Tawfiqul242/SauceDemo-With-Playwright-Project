from pages.product_page import ProductPage


# TC-005: Verify sorting by Name (A to Z)
def test_sort_a_to_z(page, logged_in):
    #page class objects
    product_page = ProductPage(page)

    expected_names = sorted(product_page.get_product_names())

    product_page.sort_name_by_ascending()
    actual_names = product_page.get_product_names()

    assert expected_names == actual_names



# TC-006: Verify sorting by Name (Z to A)
def test_sort_z_to_a(page, logged_in):
    # page class object
    product_page = ProductPage(page)

    expected_names = sorted(product_page.get_product_names(), reverse=True)

    product_page.sort_name_by_decending()
    actual_names = product_page.get_product_names()

    assert actual_names == expected_names



# TC-007: Verify sorting by Price (Low to High)
def test_sort_price_low_to_high(page, logged_in):
    # page class object
    product_page = ProductPage(page)

    expected_price = sorted(product_page.get_product_price())

    product_page.sort_by_price_low_to_high()
    actual_price = product_page.get_product_price()

    assert actual_price == expected_price




# TC-008: Verify sorting by Price (High to Low)
def test_sort_price_high_to_low(page, logged_in):
    # page class object
    product_page = ProductPage(page)

    expected_price = sorted(product_page.get_product_price(), reverse=True)

    product_page.sort_by_price_high_to_low()
    actual_price = product_page.get_product_price()

    assert actual_price == expected_price
