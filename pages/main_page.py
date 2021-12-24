from .base_page import BasePage
from .locators import *


class MainPage(BasePage):

    def open_field(self, field):
        self.browser.find_element(*field).click()

    def check_link_field(self, text_link):
        assert self.is_item_present(text_link), f'Link {text_link} not found'