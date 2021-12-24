from .base_page import BasePage
from .locators import *


class LoginPage(BasePage):

    def click_button_login(self, button):
        assert self.click_button_or_link(button), 'Button for login not found'