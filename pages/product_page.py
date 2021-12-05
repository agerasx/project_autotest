import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_button_add_to_cart(self):
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        button_add_to_cart.click()

    def name_in_cart_matches(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_CART).text
        assert product_name == product_name_cart, "Product name in cart does not matches"

    def price_in_cart_matches(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_CART).text
        assert product_price == product_price_cart, "Product price in cart does not matches"

