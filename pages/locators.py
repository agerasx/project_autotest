from selenium.webdriver.common.by import By


class GlobalVariables():
    LINK = "http://selenium1py.pythonanywhere.com/"


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = "login"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


