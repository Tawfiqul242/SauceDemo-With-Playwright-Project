from playwright.sync_api import expect
from pages.product_page import ProductPage
from pages.login_page import LoginPage

def test_logout(page,logged_in):
    # class objects
    login = LoginPage(page)
    product_page = ProductPage(page)

    #click menu bar 
    product_page.click_menu()

    #click logout button
    product_page.click_logout_btn()

    #verify user is redirected to the login page
    expect(page).to_have_url("https://www.saucedemo.com/")

    # verify login button is visible
    expect(login.LOGIN_BTN).to_be_visible()

    # verify URL no longer contains inventory page
    expect(page).not_to_have_url("https://www.saucedemo.com/inventory.html")