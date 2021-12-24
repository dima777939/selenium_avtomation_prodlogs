import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    print('\nstart browser')
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser")
    browser.quit()


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(5)

    def open_link(self):
        self.browser.get(self.url)

    def send_text_form_field(self, field, text):
        self.browser.find_element(*field).clear()
        self.browser.find_element(*field).send_keys(text)

    def click_button_or_link(self, button_form):
        try:
            self.browser.find_element(*button_form).click()
        except NoSuchElementException:
            return False
        return True

    def is_item_present(self, link):
        try:
            self.browser.find_element(*link)
        except NoSuchElementException:
            return False
        return True

    def select_value_select_field(self, field, index):
        select = Select(self.browser.find_element(*field))
        select.select_by_index(index)

    def get_select_text(self, selector_select):
        select = Select(self.browser.find_element(*selector_select))
        return select.first_selected_option



