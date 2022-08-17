import pytest

from tests.conftest import base_url_tme
from tests.page_object_manager import GetPage
from utils.wait import Wait


@pytest.mark.usefixtures("driver")
class TestParkingTme:

    def get_page(self):
        return GetPage(self.driver)

    def waits(self):
        return Wait(self.driver)

    def get_parking_page(self, lang='pl', login=False, username='', password=''):
        self.driver.get(base_url_tme() + lang)

        if login is True:
            self.get_page().home_page_tme().click_header_login_modal()
            self.waits().wait_for_element_one_second()
            self.get_page().login_modal_tme().login_account(username, password)

        self.get_page().home_page_tme().wait_for_footer_element_is_clickable()

        self.get_page().home_page_tme().click_accept_rodo_btn()
        self.get_page().home_page_tme().click_parking_btn()

    def create_folder(self, lang='pl', login=True, username='', password='', name='', description=''):
        self.get_parking_page(lang, login, username, password)
        self.get_page().parking_tme().create_new_folder(name, description)
        self.waits().wait_for_element_two_second()

    def test_get_parking_page(self):
        lang = 'pl'
        username = 'PL-FIR'
        password = 'test12pl'

        self.get_parking_page(lang, True, username, password)
        create_directory_btn = self.get_page().parking_tme().is_displayed_create_folder_btn()

        assert create_directory_btn is True

    def test_create_and_delete_folder(self):
        lang = 'pl'
        username = 'nowy_testowy_polak_fiz'
        password = 'test12pl'
        name = 'nowy folder'
        description = 'opis opis opis'

        self.create_folder(lang, True, username, password, name, description)

        assert self.get_page().parking_tme().is_displayed_folder(name) is True

        self.get_page().parking_tme().delete_first_folder()
        self.waits().wait_for_element_two_second()

        assert self.get_page().parking_tme().is_displayed_folder(name) is False

    def test_add_product_from_cataloque(self):
        lang = 'pl'
        username = 'nowy_testowy_polak_fiz'
        password = 'test12pl'
        name = 'folder najnowszy 2'
        description = 'folder najnowszy 2 opis'
        symbol = '4D-ARD-ADAPSH2'

        self.create_folder(lang, True, username, password, name, description)
        self.get_page().home_page_tme().fill_search_symbol(symbol)
        self.get_page().home_page_tme().click_search_btn()
        self.waits().wait_for_element_two_second()
        self.get_page().parking_tme().add_product_to_parking_from_cataloque()
        self.get_parking_page(lang)
        self.get_page().parking_tme().get_to_folder(name)

        assert self.get_page().parking_tme().is_displayed_product_in_folder(symbol) is True

        self.get_parking_page()
        self.waits().wait_for_element_two_second()
        self.get_page().parking_tme().delete_first_folder()

    def test_merge_folders(self):
        lang = 'pl'
        username = 'nowy_testowy_polak_fiz'
        password = 'test12pl'
        name1 = 'folder1'
        description1 = 'opis opis opis'
        name2 = 'folder2'
        description2 = 'opis opis opis'
        name = 'merged folder'
        description = 'merged opis'

        self.create_folder(lang, True, username, password, name1, description1)
        self.create_folder(lang, False, username, password, name2, description2)

        self.get_page().parking_tme().merge_two_folders(name, description)
        self.waits().wait_for_element_two_second()

        assert self.get_page().parking_tme().is_displayed_folder(name) is True

        self.get_page().parking_tme().delete_first_folder()

    def test_move_product_from_one_folder_to_another(self):
        lang = 'pl'
        username = 'nowy_testowy_polak_fiz'
        password = 'test12pl'
        name1 = 'folder1'
        description1 = 'opis opis opis'
        name2 = 'folder2'
        description2 = 'opis opis opis'
        symbol = '4D-ARD-ADAPSH2'

        self.create_folder(lang, True, username, password, name1, description1)
        self.create_folder(lang, False, username, password, name2, description2)
        self.get_page().parking_tme().get_to_folder(name1)
        self.get_page().parking_tme().add_to_parking_from_empty_folder()
        self.get_page().home_page_tme().fill_search_symbol(symbol)
        self.get_page().home_page_tme().click_search_btn()
        self.waits().wait_for_element_two_second()
        self.get_page().parking_tme().add_product_to_dedicated_folder_in_parking_from_cataloque(name1)
        self.get_parking_page(lang)
        self.get_page().parking_tme().get_to_folder(name1)
        self.get_page().parking_tme().move_product_to_another_folder(name2)
        self.get_parking_page(lang)
        self.get_page().parking_tme().get_to_folder(name2)

        assert self.get_page().parking_tme().is_displayed_product_in_folder(symbol) is True

        self.get_parking_page(lang)
        self.get_page().parking_tme().delete_first_folder()
        self.get_parking_page(lang)
        self.get_page().parking_tme().delete_first_folder()

    def test_copy_product_from_one_folder_to_another(self):
        lang = 'en'
        username = 'nowy_testowy_polak_fiz'
        password = 'test12pl'
        name1 = 'wojtek'
        description1 = 'ozcxxzczxcs'
        name2 = 'bruno'
        description2 = 'osdfsdf24f4f'
        symbol = '4D-ARD-ADAPSH2'

        self.create_folder(lang, True, username, password, name1, description1)
        self.create_folder(lang, False, username, password, name2, description2)
        self.get_page().parking_tme().get_to_folder(name1)
        self.get_page().parking_tme().add_to_parking_from_empty_folder()
        self.get_page().home_page_tme().fill_search_symbol(symbol)
        self.get_page().home_page_tme().click_search_btn()
        self.waits().wait_for_element_two_second()
        self.get_page().parking_tme().add_product_to_dedicated_folder_in_parking_from_cataloque(name1)
        self.get_parking_page(lang)
        self.get_page().parking_tme().get_to_folder(name1)
        self.get_page().parking_tme().copy_product_to_another_folder(name2)

        self.get_parking_page(lang)
        self.get_page().parking_tme().get_to_folder(name2)
        assert self.get_page().parking_tme().is_displayed_product_in_folder(symbol) is True

        self.get_parking_page(lang)
        self.get_page().parking_tme().get_to_folder(name1)
        assert self.get_page().parking_tme().is_displayed_product_in_folder(symbol) is True

        self.get_parking_page(lang)
        self.get_page().parking_tme().delete_first_folder()
        self.get_parking_page(lang)
        self.get_page().parking_tme().delete_first_folder()

    def test_get_prices_and_stocks_for_product_in_folder(self):
        lang = 'fr'
        username = 'nowy_testowy_polak_fiz'
        password = 'test12pl'
        name1 = 'folderek'
        description1 = 'opis w folderku'
        symbol = '4D-ARD-ADAPSH2'

        self.create_folder(lang, True, username, password, name1, description1)
        self.get_page().parking_tme().get_to_folder(name1)
        self.get_page().parking_tme().add_to_parking_from_empty_folder()
        self.get_page().home_page_tme().fill_search_symbol(symbol)
        self.get_page().home_page_tme().click_search_btn()
        self.waits().wait_for_element_two_second()
        self.get_page().parking_tme().add_product_to_dedicated_folder_in_parking_from_cataloque(name1)
        self.get_parking_page(lang)
        self.get_page().parking_tme().get_to_folder(name1)
        self.get_page().parking_tme().select_first_product_from_folder()

        assert self.get_page().parking_tme().is_displayed_price_and_stock() is False
        self.get_page().parking_tme().get_prices_and_stocks()

        assert self.get_page().parking_tme().is_displayed_price_and_stock() is True
        self.get_parking_page(lang)
        self.get_page().parking_tme().delete_first_folder()

