import random
import time

import allure
import pytest

from data.data_test import multi_view_data
from pages.catalog_section_page import Catalog_Section_page
from pages.main_page import Main_page


@allure.epic("Действия с боковым меню")
@allure.story("Действия с Каталогом")
@allure.title("Переход в раздел со всеми товарами")
def test_chosen_catalog_section(web_driver, choose_random_section):
    mp = Main_page(web_driver)
    mp.click_main_menu()
    mp.click_menu_section(choose_random_section)
    name_chosen_section = mp.find_section_name(choose_random_section)
    with allure.step("Перейти к разделу товаров"):
        sp = Catalog_Section_page(web_driver)
    name_section = sp.get_page_name()
    assert name_chosen_section in name_section, f"Название раздела {name_section} на открывшейся странице " \
                                                f"не соответствует выбранному разделу {name_chosen_section} Каталога"


@allure.epic("Действия со списком товаров")
@allure.story("Настройка выдачи товаров раздела")
@allure.title("Параметризированный тест в соответствии с комбинаторикой сортировки, выдачи, типа отображения")
@pytest.mark.parametrize("data", multi_view_data)
def test_multi_sort(go_to_section_page, data):
    with allure.step("Перейти к разделу товаров"):
        sp = go_to_section_page
    sp.sort_display_show_by(data['params'])
    result = list(sp.check_sort_display_show_by_result())
    assert data['expected'] == result, f"Ожидаемый результат: {data['expected']} не совпадает с фактическим: {result}"


@allure.epic("Действия со списком товаров")
@allure.title("Проверка отсутствия пагинации")
@pytest.mark.skip
def test_go_to_paging(go_to_section_page):
    go_to_section_page.move_to_footer()
    pagination = go_to_section_page.check_pagination_block()
    assert pagination == False
