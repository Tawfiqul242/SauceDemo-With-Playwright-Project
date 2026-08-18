import pytest
from playwright.sync_api import sync_playwright
from utils.read_json import load_json
from pages.login_page import LoginPage

@pytest.fixture(scope="session")  # browser fixture for opennign browser
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        yield browser

        browser.close()

@pytest.fixture  # page fixture for new page
def page(browser):
    page = browser.new_page()

    yield page

    page.close()

@pytest.fixture
def logged_in(page):
    login = LoginPage(page)

    data = load_json("test_data/login_data.json")["valid_user"]

    login.navigate()
    login.fill_login_form(data["username"], data["password"])
    login.click_login_btn()

