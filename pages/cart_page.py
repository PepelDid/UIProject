import allure

from base.base import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

cart_page = "https://lavka-coffee-tea.ru/basket/"


class Cart_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    delayed_marker = '//div[@class="basket-items-list-item-warning-container"]//div'
    remove = '//span[@class="basket-item-actions-remove"]'

    # Getters
    def get_delayed_marker(self):
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self.delayed_marker)))

    def get_remove_element(self):
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self.remove)))

    # Actions

    @allure.step("Нажать на иконку удаления товара из корзины")
    def click_remove_item(self):
        self.get_remove_element().click()

    # Methods
    @allure.step("Получить статус отложенного товара в корзине")
    def check_delayed_status(self):
        status = self.get_delayed_marker().text.strip()
        return status
