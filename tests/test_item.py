import allure


@allure.epic("Действия с товаром")
@allure.title("Добавить товар в отложенные")
def test_add_to_favorite(go_to_section_page, cart_page):
    with allure.step("Перейти к разделу товаров"):
        sp = go_to_section_page
    sp.add_to_favorite()
    count = sp.get_favorite_counter().text
    assert count == '1', f"Количество товаров в списке отложенных не равняется 1"
    sp.click_favorite_block()
    cp = cart_page
    delayed_status = cp.check_delayed_status()
    assert delayed_status == 'Товар отложен. Добавить к заказу?', f"Нет записи о том, что товар отложен"


@allure.epic("Действия с товаром")
@allure.title("Удалить товар из отложенных")
def test_remove_from_favorite(go_to_section_page, cart_page):
    with allure.step("Перейти к разделу товаров"):
        sp = go_to_section_page
    sp.add_to_favorite()
    sp.click_favorite_block()
    cp = cart_page
    cp.click_remove_item()
    with allure.step("Вернуться к разделу товаров"):
        cp.driver.back()
    assert sp.check_empty_favorite(), f"В списке отложенных остались товары"


@allure.epic("Действия с товаром")
@allure.title("Добавить товар в сравнение")
def test_add_to_compare(go_to_section_page):
    with allure.step("Перейти к разделу товаров"):
        sp = go_to_section_page
    sp.add_to_compare()
    count = sp.get_compare_counter().text
    assert count == '1', f"В сравнении {count} товаров"


@allure.epic("Действия с товаром")
@allure.title("Удалить товар из сравнения")
def test_remove_from_compare(go_to_section_page, compare_page):
    with allure.step("Перейти к разделу товаров"):
        sp = go_to_section_page
    sp.add_to_compare()
    sp.click_compare_block()
    with allure.step("Перейти на страницу сравнения"):
        cp = compare_page
    cp.click_remove_item()
    empty_compare_box = cp.check_empty_compare()
    assert empty_compare_box == 'Список сравниваемых элементов пуст.', f"Список сравниваемых товаров не пуст"


@allure.epic("Действия с товаром")
@allure.title("Добавить один товар в корзину")
def test_add_to_cart_one_item(go_to_section_page):
    with allure.step("Перейти к разделу товаров"):
        sp = go_to_section_page
    sp.click_first_to_cart()
    item_name = sp.read_first_item_name()
    count, item_names_in_the_cart = sp.check_items_in_the_cart()
    assert count == '1', f"В корзине {count} товаров"
    assert item_name in item_names_in_the_cart, f"В корзине нет товара с названием {item_name}"


@allure.epic("Действия с товаром")
@allure.title("Добавить два товара в корзину")
def test_add_to_cart_two_items(go_to_section_page):
    with allure.step("Перейти к разделу товаров"):
        sp = go_to_section_page
    sp.click_first_to_cart()
    sp.click_second_to_cart()
    first_item_name = sp.read_first_item_name()
    second_item_name = sp.read_second_item_name()
    count, item_names_in_the_cart = sp.check_items_in_the_cart()
    assert count == '2', f"В корзине {count} товар(ов)"
    assert item_names_in_the_cart[1] == first_item_name, f"В корзине нет товара с названием {first_item_name} "
    assert item_names_in_the_cart[0] == second_item_name, f"В корзине нет товара с названием {second_item_name} "


@allure.epic("Действия с товаром")
@allure.title("Добавить два товара в корзину и удалить один из них")
def test_remove_item_from_cart(go_to_section_page):
    with allure.step("Перейти к разделу товаров"):
        sp = go_to_section_page
    sp.click_first_to_cart()
    sp.click_second_to_cart()
    first_item_name = sp.read_first_item_name()
    sp.click_remove_item()
    count, item_names_in_the_cart = sp.check_items_in_the_cart()
    assert count == '1', f"В корзине осталось {count} товар(ов)"
    assert first_item_name in item_names_in_the_cart, f"В корзине нет товара с названием {first_item_name}"


@allure.epic("Действия с товаром")
@allure.title("Добавить два товара в корзину и удалить оба")
def test_remove_two_items_from_cart(go_to_section_page):
    with allure.step("Перейти к разделу товаров"):
        sp = go_to_section_page
    sp.click_first_to_cart()
    sp.click_second_to_cart()
    sp.click_remove_item()
    sp.click_remove_item()
    assert sp.check_empty_cart_pop_up()
    sp.driver.refresh()
    assert sp.check_empty_cart_block() == 'пуста', f"Надписи о пустой корзине нет"


@allure.epic("Действия с товаром")
@allure.title("Вызвать окно быстрого просмотра карточки товара")
def test_see_fast_view(go_to_section_page):
    with allure.step("Перейти к разделу товаров"):
        sp = go_to_section_page
    title_item = sp.read_first_item_name()
    title_in_the_view = sp.see_fast_view_window()
    assert title_item == title_in_the_view, f"Наименование товара в карточке быстрого просмотра {title_in_the_view} " \
                                            f"не совпадает с наименованием товара в основной карточке {title_item}"


@allure.epic("Действия с товаром")
@allure.title("Просмотреть полную карточку /страницу товара")
def test_see_item_page(go_to_section_page, item_page):
    with allure.step("Перейти к разделу товаров"):
        sp = go_to_section_page
    title_item = sp.read_first_item_name()
    sp.click_first_item_name()
    with allure.step("Перейти к полной карочке /странице товара"):
        ip = item_page
    item_card = ip.get_item_tile().text
    assert title_item == item_card, f"Наименование товара на его странице {item_card} " \
                                    f"не совпадает с наименованием товара в карточке на странице раздела {title_item}"


@allure.epic("Действия с товаром")
@allure.story("Изменение количества товара, добавляемого в корзину")
@allure.title("Увеличить количество 1 товара до 2 шт кнопкой плюс и положить в корзину")
def test_increase_item_quantity_by_plus_button(go_to_section_page):
    with allure.step("Перейти к разделу товаров"):
        sp = go_to_section_page
    sp.click_plus()
    sp.click_first_to_cart()
    selected_item_quantity = sp.check_first_item_quantity()
    sp.move_to_cart_block()
    quantity_in_the_cart = sp.check_first_item_quantity_in_the_cart()
    assert selected_item_quantity == quantity_in_the_cart, f"В карточке товара указано {selected_item_quantity} " \
                                                           f"единиц товара, а в корзине {quantity_in_the_cart}"


@allure.epic("Действия с товаром")
@allure.story("Изменение количества товара, добавляемого в корзину")
@allure.title("Увеличить количество 1 товара до 3 шт кнопкой плюс, положить в корзину, "
              "проверить наличие в корзине 3 шт.Затем удалить товар из корзины,"
              "уменьшить количество товара до 2 шт. кнопкой минус и положить товар в корзину")
def test_decrease_item_quantity_by_minus_button(go_to_section_page):
    with allure.step("Перейти к разделу товаров"):
        sp = go_to_section_page
    sp.click_plus()
    sp.click_plus()
    sp.click_first_to_cart()
    selected_item_quantity = sp.check_first_item_quantity()
    sp.move_to_cart_block()
    quantity_in_the_cart = sp.check_first_item_quantity_in_the_cart()
    assert selected_item_quantity == quantity_in_the_cart, f"В карточке товара указано {selected_item_quantity} " \
                                                           f"единиц товара, а в корзине {quantity_in_the_cart}"

    sp.click_remove_item()
    sp.click_minus()
    selected_item_quantity = sp.check_first_item_quantity()
    sp.click_first_to_cart()
    sp.move_to_cart_block()
    quantity_in_the_cart = sp.check_first_item_quantity_in_the_cart()
    assert selected_item_quantity == quantity_in_the_cart, f"В карточке товара указано {selected_item_quantity} " \
                                                           f"единиц товара, а в корзине {quantity_in_the_cart}"


@allure.epic("Действия с товаром")
@allure.story("Изменение количества товара, добавляемого в корзину")
@allure.title("Увеличить количество 1 товара до 2 шт путем ввода числа и положить в корзину")
def test_input_item_quantity_between_1_and_max(go_to_section_page):
    with allure.step("Перейти к разделу товаров"):
        sp = go_to_section_page
    number = '2'
    sp.input_item_number(number)
    sp.click_first_to_cart()
    sp.move_to_cart_block()
    quantity_in_the_cart = sp.check_first_item_quantity_in_the_cart()
    assert quantity_in_the_cart == float(number), f"Введено {number} товара(ов), но в корзине " \
                                                  f"{quantity_in_the_cart} товар(ов)"


@allure.epic("Действия с товаром")
@allure.story("Изменение количества товара, добавляемого в корзину")
@allure.title("Увеличить количество 1 товара до максимально доступного путем ввода числа и положить в корзину")
def test_input_max_item_quantity(go_to_section_page):
    with allure.step("Перейти к разделу товаров"):
        sp = go_to_section_page
    max_q = sp.read_max_quantity()
    sp.input_item_number(str(max_q))
    sp.click_first_to_cart()
    sp.move_to_cart_block()
    quantity_in_the_cart = sp.check_first_item_quantity_in_the_cart()
    assert quantity_in_the_cart == max_q, f"В наличии {max_q} товара(ов),но в корзине {quantity_in_the_cart} товара(ов)"


@allure.epic("Действия с товаром")
@allure.story("Изменение количества товара, добавляемого в корзину")
@allure.title("Увеличить количество 1 товара сверх доступного путем ввода числа и положить в корзину."
              "Производится автоисправление количества и в корзине окажется только доступное количество товара")
def test_input_over_max_item_quantity_negative(go_to_section_page):
    with allure.step("Перейти к разделу товаров"):
        sp = go_to_section_page
    max_q = sp.read_max_quantity()
    input_q = str(max_q + 1.0)
    sp.input_item_number(input_q)
    sp.click_first_to_cart()
    sp.move_to_cart_block()
    quantity_in_the_cart = sp.check_first_item_quantity_in_the_cart()
    assert quantity_in_the_cart == max_q, f"В наличии {max_q} товара(ов),но в корзине {quantity_in_the_cart} товара(ов)"


@allure.epic("Действия с товаром")
@allure.story("Изменение количества товара, добавляемого в корзину")
@allure.title("Ввести в поле количества товара кириллические символы и положить в корзину."
              "Производится автоисправление количества и в корзине окажется 1 шт. товара")
def test_input_cyrillic_symbols_to_item_quantity_negative(go_to_section_page):
    with allure.step("Перейти к разделу товаров"):
        sp = go_to_section_page
    text_for_input = 'Фрг'
    sp.input_item_number(text_for_input)
    sp.click_first_to_cart()
    sp.move_to_cart_block()
    quantity_in_the_cart = sp.check_first_item_quantity_in_the_cart()
    assert quantity_in_the_cart == float('1'), f"Количество товаров в корзине {quantity_in_the_cart} не равно 1"


@allure.epic("Действия с товаром")
@allure.story("Изменение количества товара, добавляемого в корзину")
@allure.title("Ввести в поле количества товара латинские символы и положить в корзину."
              "Производится автоисправление количества и в корзине окажется 1 шт. товара")
def test_input_latin_and_special_symbols_to_item_quantity_negative(go_to_section_page):
    with allure.step("Перейти к разделу товаров"):
        sp = go_to_section_page
    text_for_input = 'Usa@&'
    sp.input_item_number(text_for_input)
    sp.click_first_to_cart()
    sp.move_to_cart_block()
    quantity_in_the_cart = sp.check_first_item_quantity_in_the_cart()
    assert quantity_in_the_cart == float('1'), f"Количество товаров в корзине {quantity_in_the_cart} не равно 1"


@allure.epic("Действия с товаром")
@allure.story("Изменение количества товара, добавляемого в корзину")
@allure.title("Ввести в поле количества товара ноль и положить в корзину."
              "Производится автоисправление количества и в корзине окажется 1 шт. товара")
def test_input_null_to_item_quantity_negative(go_to_section_page):
    with allure.step("Перейти к разделу товаров"):
        sp = go_to_section_page
    text_for_input = '0'
    sp.input_item_number(text_for_input)
    sp.click_first_to_cart()
    sp.move_to_cart_block()
    quantity_in_the_cart = sp.check_first_item_quantity_in_the_cart()
    assert quantity_in_the_cart == float('1'), f"Количество товаров в корзине {quantity_in_the_cart} не равно 1"
