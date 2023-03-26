import time

import allure
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base import Base

catalog_page_url = "https://lavka-coffee-tea.ru/catalog/"


class Catalog_Section_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    page_title = '//h1[@id="pagetitle"]'
    block = '//i[@title="плиткой"]'
    list = '//i[@title="списком"]'
    table = '//i[@title="таблицей"]'
    el_20 = '//a[@rel="nofollow"]/span[contains(text(),"20")]'
    el_50 = '//a[@rel="nofollow"]/span[contains(text(),"50")]'
    el_100 = '//a[@rel="nofollow"]/span[contains(text(),"100")]'
    footer = '//div[@class="footer_bottom_inner"]'
    pagination = '//div[@class="module-pagination"]'
    shows = '//i[@title="По популярности"]/following-sibling::span'
    name = '//i[@title="По алфавиту"]/following-sibling::span'
    price = '//i[@title="По цене"]/following-sibling::span'
    sort_link = '//div[contains(@class,"compact_mobile_filter")]/a'
    current_display = '//div[contains(@class,"ajax_load")]'
    current_count = '//div[contains(@class,"ajax_load")]//*[contains(@class,"item_wrapper")]'
    current_sort = '(//a[contains(@class,"current")])[2]'
    product_card = '//table[@class="list_item"]//td[@class="image_block"]'
    first_item = '(//div[contains(@class, " item_wrap")])[1]'
    second_item = '(//div[contains(@class, " item_wrap")])[2]'
    first_to_compare = '(//div[contains(text(),"Сравнить")])[1]'
    first_to_favorite = '(//div[contains(text(),"Отложить")])[1]'
    first_to_cart = '(//span[contains(text(), "В корзину")])[1]'
    second_to_cart = '(//span[contains(text(), "В корзину")])[2]'
    first_item_title = '(//div[@class="item-title"]/a)[1]'
    first_item_price = '(//span[@class="price_value"])[1]'
    first_total_sum = '(//div[@class="total_summ"]//span)[1]'
    second_item_title = '(//div[@class="item-title"]/a)[2]'
    favorite_icon = '//a[@href="/basket/#delayed"]'
    compare_icon = '//a[@href="/catalog/compare.php"]'
    cart_block = '//div[contains(@class, "basket_block")]'
    first_item_quantity_in_the_cart = '(//span[@class="measure"]//span)[1]'

    compare_block = '//div[contains(@class, "wraps_icon_block")]//a[contains(@title, "Список сравниваемых товаров")]'
    favorite_block = '//div[contains(@class, "wraps_icon_block")]//a[contains(@title, "Список отложенных товаров")]'
    items_cart_counter = '//div[@class="items"]/a[@href="/basket/"]'
    items_cart_names = '//table[@class="cart_shell"]//a/span'
    empty_cart_pop_up = '//td[@class="description"]/div[@class="basket_empty_subtitle"]'
    empty_cart_block = '//div[@class="title"]/following-sibling::div[@class="value"]'
    items_favorite_counter = '//div[@class= "items"]/div[@class="text"]'
    items_compare_counter = '//div[@class= "items"]/a[@href="/catalog/compare.php"]'
    remove_item = '(//span[@class="remove"])[1]'
    fast_view = '(//div[@class="fast_view_block"])[1]'
    fast_view_item_title = '//div[contains(@class, "fast_view_frame")]//h2/a'
    minus = '(//span[@class="minus"])[1]'
    plus = '(//span[@class="plus"])[1]'
    quantity = '(//input[@name="quantity"])[1]'
    item_number = '(//input[@name="quantity"])[1]'
    max_quantity = '(//input[@name="quantity"])[1]/following-sibling::span'

    # Getters
    def get_title_page(self):
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self.page_title)))

    @allure.step("Прочитать название раздела на открывшейся странице")
    def get_page_name(self):
        name = self.get_title_page().text
        return name

    def get_block_el(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.block)))

    def get_list_el(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.list)))

    def get_table_el(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.table)))

    def get_20_el(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.el_20)))

    def get_50_el(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.el_50)))

    def get_100_el(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.el_100)))

    # def get_pagination(self):
    #     return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.pagination)))

    def get_shows_sort(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.shows)))

    def get_name_sort(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_price_sort(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_sort_link(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.sort_link)))

    def get_current_display(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.current_display)))

    def get_current_count(self):
        return len(self.driver.find_elements(By.XPATH, self.current_count))

    def get_current_sort(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.current_sort)))

    def get_first_item(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.first_item)))

    def get_second_item(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.second_item)))

    def get_first_item_title(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.first_item_title)))

    def get_second_item_title(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.second_item_title)))

    def get_first_favorite_icon(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, self.first_to_favorite)))

    def get_first_compare_icon(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.first_to_compare)))

    def get_first_to_cart_icon(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.first_to_cart)))

    def get_second_to_cart_icon(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.second_to_cart)))

    @allure.step("Посмотреть счетчик отложенных товаров в верхнем меню")
    def get_favorite_counter(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.items_favorite_counter)))

    @allure.step("Посмотреть счетчик товаров,находящихся в сравнении в верхнем меню")
    def get_compare_counter(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.items_compare_counter)))

    def get_compare_block(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.compare_block)))

    def get_favorite_block(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.favorite_block)))

    def get_cart_counter(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.items_cart_counter)))

    def get_cart_items_names(self):
        self.move_to_cart_block()
        arr = self.driver.find_elements(By.XPATH, self.items_cart_names)
        return arr

    def get_empty_cart_block(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.empty_cart_block)))

    def get_cart_item_name(self):
        self.move_to_cart_block()
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.items_cart_names)))

    def get_remove_item(self):
        try:
            remover = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.remove_item)))
        except TimeoutException:
            self.move_to_cart_block()
            remover = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.remove_item)))
        finally:
            return remover

    def get_fast_view(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.fast_view)))

    @allure.step("Прочитать название товара в карточке быстрого просмотра")
    def get_fast_view_item_title(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.fast_view_item_title)))

    def get_minus(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.minus)))

    def get_plus(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.plus)))

    def get_quantity(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.quantity)))

    def get_input_quantity(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.item_number)))

    def get_max_quantity(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.max_quantity)))

    def get_first_item_price(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.first_item_price)))

    def get_first_item_total_sum(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.first_total_sum)))

    def get_first_item_number_in_the_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.first_item_quantity_in_the_cart)))



    # Actions
    def click_block(self):
        self.get_block_el().click()

    def click_list(self):
        self.get_list_el().click()

    def click_table(self):
        self.get_table_el().click()

    def click_el_20(self):
        self.get_20_el().click()

    def click_el_50(self):
        self.get_50_el().click()

    def click_el_100(self):
        self.get_100_el().click()

    def click_shows_sort(self):
        self.get_shows_sort().click()

    def click_name_sort(self):
        self.get_name_sort().click()

    def click_price_sort(self):
        self.get_price_sort().click()

    def click_first_favorite(self):
        self.get_first_favorite_icon().click()

    def click_first_compare(self):
        self.get_first_compare_icon().click()

    @allure.step("Нажать на кнопку 'В корзину' в карточке первого товара")
    def click_first_to_cart(self):
        self.get_first_to_cart_icon().click()

    @allure.step("Нажать на иконку 'В корзину' в карточке второго товара")
    def click_second_to_cart(self):
        self.get_second_to_cart_icon().click()

    @allure.step("Удалить товар во всплывающем окне корзины")
    def click_remove_item(self):
        self.get_remove_item().click()
        time.sleep(3)

    @allure.step("Нажать карточку товара")
    def click_first_item_name(self):
        self.get_first_item_title().click()

    @allure.step("Нажать на иконку 'Список сравниваемых товаров' верхнего меню и перейти к корзине")
    def click_compare_block(self):
        self.get_compare_block().click()

    @allure.step("Нажать на иконку 'Список отложенных товаров' верхнего меню и перейти к корзине")
    def click_favorite_block(self):
        self.get_favorite_block().click()

    @allure.step("Проверить, что счетчик отложенных товаров пуст")
    def check_empty_favorite(self):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element((By.XPATH, self.items_favorite_counter)))

    def move_to_cart_block(self):
        time.sleep(4)
        action = ActionChains(self.driver)
        elem = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_block)))
        action.move_to_element(elem).perform()

    def move_to_footer(self):
        action = ActionChains(self.driver)
        footer = self.driver.find_element(By.XPATH, self.footer)
        action.scroll_to_element(footer).perform()

    def check_pagination_block(self):
        try:
            self.driver.find_element(By.XPATH, self.pagination)
        except NoSuchElementException:
            return False
        return True

    @allure.step("Навести курсор на карточку первого товара")
    def move_to_first_product_card(self):
        action = ActionChains(self.driver)
        first_prod_cart = f'({self.product_card})[1]'
        prod_cart = self.driver.find_element(By.XPATH, first_prod_cart)
        action.move_to_element(prod_cart).perform()

    @allure.step("Нажать на кнопку '+' в карточке товара")
    def click_plus(self):
        self.get_plus().click()

    @allure.step("Нажать на кнопку '-' в карточке товара")
    def click_minus(self):
        self.get_minus().click()

    @allure.step("Прочитать, сколько товара есть в наличии")
    def read_max_quantity(self):
        max_q = float(self.get_max_quantity().get_attribute('data-max'))
        return max_q

    @allure.step("Ввести в поле ввода количество товара")
    def input_item_number(self, number):
        action = ActionChains(self.driver)
        number_field = self.get_quantity()
        action.click(number_field).perform()
        action.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).key_down(Keys.BACKSPACE).perform()
        time.sleep(3)
        action.send_keys(number).perform()




    # Methods
    @allure.step("Отсортировать, отобразить, настроить количество выдачи на странице всех товаров раздела")
    def sort_display_show_by(self, data_set):
        if data_set['sort'] == 'shows':
            if data_set['sort_order'] == 'asc':
                self.click_shows_sort()
                self.click_shows_sort()
            else:
                self.click_shows_sort()
        elif data_set['sort'] == 'name':
            if data_set['sort_order'] == 'asc':
                self.click_name_sort()
                self.click_name_sort()
            else:
                self.click_name_sort()
        elif data_set['sort'] == 'price':
            if data_set['sort_order'] == 'asc':
                self.click_price_sort()
                self.click_price_sort()
            else:
                self.click_price_sort()

        if data_set['display'] == 'block':
            self.click_block()
        elif data_set['display'] == 'list':
            self.click_list()
        elif data_set['display'] == 'table':
            self.click_table()

        if data_set['showBy'] == 20:
            self.click_el_20()
        elif data_set['showBy'] == 50:
            self.click_el_50()
        elif data_set['showBy'] == 100:
            self.click_el_100()

    @allure.step("Сравнить ожидаемые результаты с фактическими")
    def check_sort_display_show_by_result(self):
        display = self.get_current_display()
        sort = self.get_current_sort()
        sort_link = self.get_sort_link()

        current_display = display.get_attribute('data-code')
        current_sort = (sort.get_attribute('class').split(' '))[-1]
        current_count = int([x[7:] for x in sort_link.get_attribute('href').split('&') if 'showBy=' in x][0])
        current_sort_order = str([x[6:] for x in sort_link.get_attribute('href').split('&') if 'order=' in x][0])

        return current_display, current_count, current_sort, current_sort_order

    @allure.step("Нажать на иконку 'Отложить' в карточке товара")
    def add_to_favorite(self):
        self.click_first_favorite()

    @allure.step("Нажать на иконку 'Сравнить' в карточке товара")
    def add_to_compare(self):
        self.click_first_compare()
        self.driver.refresh()

    @allure.step("Посмотреть количество и название товаров во всплывающем окне корзины")
    def check_items_in_the_cart(self):
        items_array = self.get_cart_items_names()
        items = [x.text for x in items_array]
        count = self.get_cart_counter().text
        return count, items

    @allure.step("Проверить надпись во всплывающем окне корзины о том, что она пуста")
    def check_empty_cart_pop_up(self):
        return WebDriverWait(self.driver, 10).until\
            (EC.text_to_be_present_in_element((By.XPATH,  self.empty_cart_pop_up), 'К сожалению, ваша корзина пуста.'))

    @allure.step("Проверить надпись в верхнем меню, что корзина пуста")
    def check_empty_cart_block(self):
        content = self.get_empty_cart_block().text.strip()
        return content

    @allure.step("Прочитать название первого товара")
    def read_first_item_name(self):
        name = self.get_first_item_title().text
        return name

    @allure.step("Прочитать название второго товара")
    def read_second_item_name(self):
        name = self.get_second_item_title().text
        return name

    @allure.step("Нажать на иконку 'Быстрый просмотр' в карточке товара")
    def see_fast_view_window(self):
        self.move_to_first_product_card()
        self.get_fast_view().click()
        title = self.get_fast_view_item_title().text
        return title

    @allure.step("Прочитать в карточке товара, сколько единиц товара указано и какова общая цена за них")
    def check_first_item_quantity(self):
        summ = float(self.get_first_item_total_sum().text[:-5].replace(',', '.').replace(' ', ''))
        price = float(self.get_first_item_price().text.replace(',', '.').replace(' ', ''))
        quantity = round(summ / price, 1)
        return quantity

    @allure.step("Прочитать во всплывающем окне корзины, сколько единиц первого товара добавлено в корзину")
    def check_first_item_quantity_in_the_cart(self):
        number = float(self.get_first_item_number_in_the_cart().text)
        return number




