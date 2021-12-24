import random
from .base_page import BasePage
from .locators import *
from datetime import datetime, timedelta


class AdminPage(BasePage):

    @staticmethod
    def random_value_field(first=1, last=9, len_number=1):
        random.seed()
        num = random.randint(int(str(first) * len_number), int(str(last) * len_number))
        return num

    @staticmethod
    def footage(crosssection, footage_list):
        return footage_list.get(crosssection, 10000)

    @staticmethod
    def date_finish():
        date = datetime.today().date() + timedelta(days=14)
        return datetime.strftime(date, '%d.%m.%Y')

    def select_value_in_field(self, field, values):
        return self.select_value_select_field(field, self.random_value_field(values[0], values[1]))

    def check_link(self, link):
        assert self.is_item_present(link), f'Link for selector({link}) not found'

    def error_check(self, error_locator, num, iteration=1):
        if self.is_item_present(error_locator):
            self.send_text_form_field(AdminPageLocators.BATCH_NUMBER,
                                      self.random_value_field(1, 9, AdminPageLocators.LEN_BATCH_NUMBER))
            self.click_button_or_link(AdminPageLocators.BUTTON_SAVE)
            assert 50 > iteration, 'Batch number is full'
            iteration += 1
            return self.error_check(error_locator, num, iteration)
        else:
            return print(f'Order №{num} add')

    def add_order(self, count_order):
        for i in range(count_order):
            self.click_button_or_link(AdminPageLocators.SELECTOR_ADD_ORDER)
            self.send_text_form_field(AdminPageLocators.BATCH_NUMBER,
                                      self.random_value_field(1, 9, AdminPageLocators.LEN_BATCH_NUMBER))
            self.select_value_in_field(AdminPageLocators.PLASTIC, AdminPageLocators.COUNT_PLASTIC)
            self.select_value_in_field(AdminPageLocators.DESIGN, AdminPageLocators.COUNT_DESIGN)
            self.select_value_in_field(AdminPageLocators.PURPOSE, AdminPageLocators.COUNT_PURPOSE)
            self.select_value_in_field(AdminPageLocators.CORES, AdminPageLocators.COUNT_CORES)
            self.select_value_in_field(AdminPageLocators.CROSSSECTION, AdminPageLocators.COUNT_CROSSSECTION)
            self.send_text_form_field(AdminPageLocators.FOOTAGE,
                                      self.footage(self.get_select_text(AdminPageLocators.CROSSSECTION),
                                      AdminPageLocators.FOOTAGE_LIST))
            self.send_text_form_field(AdminPageLocators.DATE, self.date_finish())
            self.click_button_or_link(AdminPageLocators.BUTTON_SAVE)
            self.error_check(AdminPageLocators.ERROR_CHECK, i)