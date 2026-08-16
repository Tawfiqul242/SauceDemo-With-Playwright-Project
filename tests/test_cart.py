from playwright.sync_api import expect
from pages.product_page import ProductPage
from pages.cart_page import CartPage


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



# TC-012: Verify cart page displays selected products
def test_cart_page_displays_selected_products(page, logged_in):
        
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    # Add two products
    product_page.click_add_to_cart_btn_by_product_name("Sauce Labs Bolt T-Shirt")
    product_page.click_add_to_cart_btn_by_product_name("Sauce Labs Fleece Jacket")

    # Open cart
    product_page.CART_LINK.click()

    # Verify both products displayed
    expect(cart_page.get_cart_product_by_name("Sauce Labs Bolt T-Shirt")).to_be_visible()
    expect(cart_page.get_cart_product_by_name("Sauce Labs Fleece Jacket")).to_be_visible()

    # Verify Name matches
    expect(cart_page.get_cart_product_by_name("Sauce Labs Bolt T-Shirt")).to_have_text("Sauce Labs Bolt T-Shirt")
    expect(cart_page.get_cart_product_by_name("Sauce Labs Fleece Jacket")).to_have_text("Sauce Labs Fleece Jacket")

    # Verify Price matches
    expect(cart_page.get_cart_product_price_by_name("Sauce Labs Bolt T-Shirt")).to_have_text("$15.99")
    expect(cart_page.get_cart_product_price_by_name("Sauce Labs Fleece Jacket")).to_have_text("$49.99")

    # Quantity = 1
    expect(cart_page.get_cart_product_qty_by_name("Sauce Labs Bolt T-Shirt")).to_have_text("1")
    expect(cart_page.get_cart_product_qty_by_name("Sauce Labs Fleece Jacket")).to_have_text("1")



# TC-013: Verify removing product from cart page
def test_verify_romoving_product_from_cart_page(page, logged_in):

    product_page = ProductPage(page)
    cart_page = CartPage(page)

    # Add product
    product_page.click_add_to_cart_btn_by_product_name("Sauce Labs Bike Light")

    # Go to cart
    product_page.CART_LINK.click()

    # Remove product
    cart_page.click_remove_btn_by_product_name("Sauce Labs Bike Light")

    # Verify Product removed
    expect(cart_page.get_cart_product_by_name("Sauce Labs Bike Light")).not_to_be_visible()

    # Verify Cart becomes empty.
    expect(cart_page.CART_ITEM).to_have_count(0)



# TC-014: Verify Continue Shopping button
def test_verify_continue_shopping_button(page, logged_in):

    product_page = ProductPage(page)
    cart_page = CartPage(page)

    # Open cart
    product_page.CART_LINK.click()

    # Click Continue Shopping.
    cart_page.CONTINUE_BTN.click()

    # User returns to Products page.
    expect(product_page.PRODUCTS_TITLE).to_be_visible()