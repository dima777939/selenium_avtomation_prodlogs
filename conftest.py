import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    print('\nstart browser')
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 1080)
    yield browser
    print("\nquit browser")
    browser.quit()

