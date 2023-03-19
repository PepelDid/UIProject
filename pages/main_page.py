import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


from base.base import Base


class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    catalog_locator = '//a[@class="parent"]'
    catalog_section = '//div[contains(@class,"catalog_block")]/ul[contains(@class,"dropdown")]/li'
    section_name = '//span[@class="name"]'

    # Getters
    def get_catalog_main_menu(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog_locator)))

    def get_catalog_main_menu_section(self, x):
        random_section = f'({self.catalog_section})[{x}]'
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, random_section)))

    def get_section_name(self, x):
        name_section = f'({self.catalog_section})[{x}]{self.section_name}'
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, name_section)))

    # Actions
    @allure.step("Нажать на Каталог основного меню")
    def click_main_menu(self):
        self.get_catalog_main_menu().click()

    @allure.step("Нажать на раздел с товарами в открывшемся Каталоге основного меню")
    def click_menu_section(self, x):
        self.get_catalog_main_menu_section(x).click()

    @allure.step("Прочитать имя выбранного раздела в меню Каталога")
    def find_section_name(self, x):
        el = self.get_section_name(x)
        return el.text


# Methods
