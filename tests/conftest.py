import pytest
import random

from pages.cart_page import Cart_page
from pages.item_page import Item_page
from pages.main_page import Main_page
from pages.compare_page import Compare_page
from pages.catalog_section_page import Catalog_Section_page
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from data.urls import main_page_url


@pytest.fixture()
def web_driver():
    """Переход на главную страницу магазина"""
    options = Options()
    # options.add_argument('--start-maximized')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # driver.get('chrome://settings/')
    # driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.8)')
    driver.get(main_page_url)
    yield driver
    driver.close()


@pytest.fixture()
def choose_random_section():
    x = random.randint(1, 10)
    yield x



@pytest.fixture(scope="function")
def go_to_section_page(web_driver):
    """Рандомный раздел товаров"""
    main_page = Main_page(web_driver)
    section_page = Catalog_Section_page(web_driver)
    x = random.randint(1, 10)
    main_page.click_main_menu()
    main_page.click_menu_section(x)
    yield section_page


@pytest.fixture(scope="function")
def item_page(web_driver):
    """Страница выбранного товара"""
    item_page = Item_page(web_driver)
    yield item_page


@pytest.fixture(scope="function")
def compare_page(web_driver):
    """Страница сравнения"""
    compare_page = Compare_page(web_driver)
    yield compare_page


@pytest.fixture(scope="function")
def cart_page(web_driver):
    """Страница корзины"""
    cart_page = Cart_page(web_driver)
    yield cart_page
