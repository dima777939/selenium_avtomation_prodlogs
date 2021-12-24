from selenium.webdriver.common.by import By


class ManePageLocators:

    MAIN_LINK = 'http://127.0.0.1:8000'
    SELECTOR_LINK_LOGIN = (By.CSS_SELECTOR, "a[data-id='login']")
    SELECTOR_LINC_ADMIN = (By.CSS_SELECTOR, "a[data-id='admin']")


class LoginPageLocators:

    LINK_LOGIN = 'http://127.0.0.1:8000/manufactur/login/'
    SELECTOR_USERNAME = (By.CSS_SELECTOR, "input[type='text']")
    SELECTOR_PASSWORD = (By.CSS_SELECTOR, "input[type='password']")
    SELECTOR_BUTTON_LOGIN = (By.CSS_SELECTOR, "button.btn-primary")
    LOGIN = 'planirovka'
    PASSWORD = 'qwerty'


class AdminPageLocators:

    LINK_ADMIN = 'http://127.0.0.1:8000/admin/'
    SELECTOR_LINK_ORDER = (By.CSS_SELECTOR, 'tr.model-order a')
    SELECTOR_ADD_ORDER = (By.CSS_SELECTOR, 'a.addlink')
    BATCH_NUMBER = (By.ID, 'id_batch_number')
    PLASTIC = (By.ID, 'id_plastic')
    DESIGN = (By.ID, 'id_design')
    PURPOSE = (By.ID, 'id_purpose')
    CORES = (By.ID, 'id_cores')
    CROSSSECTION = (By.ID, 'id_crosssection')
    FOOTAGE = (By.ID, 'id_footage')
    DATE = (By.ID, 'id_completion')
    BUTTON_SAVE = (By.CSS_SELECTOR, 'input[name="_save"]')
    ERROR_CHECK = (By.CSS_SELECTOR, 'ul.errorlist')
    LEN_BATCH_NUMBER = 4
    COUNT_PLASTIC = (0, 1,)
    COUNT_DESIGN = (0, 1,)
    COUNT_PURPOSE = (0, 3,)
    COUNT_CORES = (1, 5,)
    COUNT_CROSSSECTION = (4, 8,)
    FOOTAGE_LIST = {1.5: 20000, 2.5: 15000, 4.0: 10000, 6.0: 6000, 10.0: 3000}




