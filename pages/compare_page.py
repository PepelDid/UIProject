import allure

from base.base import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

compare_page = "https://lavka-coffee-tea.ru/catalog/compare.php"


class Compare_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    item_title = '//td//div[@class="item_block"]/a'
    remove = '//div[@class="item_block"]//span[@class="remove"]'
    empty_marker = '//div[@class="bx_compare"]//font'

    # Getters
    def get_item_tile(self):
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self.item_title)))

    def get_remove_item(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, self.remove)))

    def get_empty_marker(self):
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self.empty_marker)))

    # Actions
    @allure.step("Нажать на иконку удаления товара из сравнения")
    def click_remove_item(self):
        self.get_remove_item().click()

    # Methods
    def check_item_in_compare(self):
        title = self.get_item_tile().text
        return title

    @allure.step("Посмотреть на счетчик товаров, находящихся в сравнении в верхнем меню")
    def check_empty_compare(self):
        title = self.get_empty_marker().text
        return title
