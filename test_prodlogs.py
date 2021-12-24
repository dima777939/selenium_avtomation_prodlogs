from .pages.main_page import *
from .pages.login_page import *
from .pages.admin_page import *
from .pages.locators import *


def login(browser, ):
    main_page = MainPage(browser, ManePageLocators.MAIN_LINK)
    main_page.open_link()
    main_page.check_link_field(ManePageLocators.SELECTOR_LINK_LOGIN)
    login_page = LoginPage(browser, LoginPageLocators.LINK_LOGIN)
    login_page.open_link()
    login_page.send_text_form_field(LoginPageLocators.SELECTOR_USERNAME, LoginPageLocators.LOGIN)
    login_page.send_text_form_field(LoginPageLocators.SELECTOR_PASSWORD, LoginPageLocators.PASSWORD)
    login_page.click_button_login(LoginPageLocators.SELECTOR_BUTTON_LOGIN)


def test_bot_planirovka(browser):
    login(browser)
    main_page = MainPage(browser, ManePageLocators.MAIN_LINK)
    main_page.open_link()
    main_page.check_link_field(ManePageLocators.SELECTOR_LINC_ADMIN)
    admin_page = AdminPage(browser, AdminPageLocators.LINK_ADMIN)
    admin_page.open_link()
    admin_page.check_link(AdminPageLocators.SELECTOR_LINK_ORDER)
    admin_page.click_button_or_link(AdminPageLocators.SELECTOR_LINK_ORDER)
    admin_page.add_order(100)






