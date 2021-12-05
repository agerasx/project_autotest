import time
import math
from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(4)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        x_start = alert_text.find('= ')
        x_end = alert_text.find(' \n')
        x = alert_text[x_start+2:x_end]
        answer = str(math.log(abs(12*math.sin(int(x)))))
        alert.send_keys(answer)
        alert.accept()
        alert.accept()




