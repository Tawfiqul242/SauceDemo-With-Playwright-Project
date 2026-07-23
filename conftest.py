import pytest
from playwright.sync_api import sync_playwright

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

