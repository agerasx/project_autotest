from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.locators import GlobalVariables


def test_guest_can_go_to_login_page(browser):
    link = GlobalVariables.LINK
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    page_login = LoginPage(browser, browser.current_url)
    page_login.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = GlobalVariables.LINK
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.click_button_add_to_cart()
    page.solve_quiz_and_get_code()
    page.name_in_cart_matches()
    #page.price_in_cart_matches()



