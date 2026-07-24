from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.read_json import load_json

def test_login(page):
    #class objects
    login = LoginPage(page)
    product_page = ProductPage(page)

    # navigate to the website
    login.navigate()

    # fill the login form
    data = load_json()
    login.fill_login_form(data["valid_user"]["username"], data["valid_user"]["password"])

    # click the login button
    login.click_login_btn()

    # verify product page is visible
    expect(product_page.PRODUCTS_TITLE).to_be_visible()

    # verify URL contains /inventory.html
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    # Verify Product list is visible.
    expect(product_page.PRODUCTS.first).to_be_visible()