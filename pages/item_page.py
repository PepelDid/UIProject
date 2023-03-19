import allure

from base.base import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Item_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    item_title = '//h1[@id="pagetitle"]'

    # Getters
    @allure.step("Прочитать наименование товара на странице")
    def get_item_tile(self):
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self.item_title)))

    # Actions
    # Methods
