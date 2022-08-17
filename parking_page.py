from selenium.webdriver.common.by import By
from utils.wait import Wait
from selenium.webdriver.support.ui import Select


class ParkingPageTME:

    def __init__(self, driver) -> None:
        """
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.create_new_directory_btn_xpath = "//span[@data-action='create-directory']"
        self.directory_name_input_xpath = "//input[@name='parking-directory-name']"
        self.directory_description_textarea_xpath = "//textarea[@name='parking-directory-description']"
        self.create_directory_save_btn_xpath = "//a[@class='button'][2]"
        self.sort_directories_by_create_data_xpath = "//*[@id='directories-list']/thead/tr/th[6]"
        self.directory_link_xpath = "//span[@class='name-inline']"
        self.sort_directories_by_data_xpath = "//th[@data-column='5']"
        self.remove_directory_btn_xpath = "//button[@data-action='remove']"
        self.move_directory_btn_xpath = "//button[@data-action='move-to']"
        self.copy_directory_btn_xpath = "//button[@data-action='copy-to']"
        self.get_prices_and_stocks_btn_xpath = "//button[@data-action='get-prices-and-stocks']"
        self.remove_confirming_directory_save_btn_xpath = "//div[@class='popup_panel']/a[@class='button'][2]"
        self.add_to_parking_from_cataloque_xpath = "//span[@data-gtm-event-category='parking'][1]"
        self.add_confirming_to_parking_from_cataloque_xpath = "//a[@class='button'][2]"
        self.merge_directories_btn_xpath = "//button[@data-action='merge']"
        self.add_to_parking_from_empty_folder_btn_xpath = "//a[@class='parking__option-button parking__option-button--add']"
        self.choose_folder_in_creating_modal_select_xpath = "//select[@name='parking-directory-id']"
        self.is_displayed_price_and_stock_xpath = "//tr[@has-price-and-stock='true']"


    def waits(self):
        return Wait(self.driver)

    def is_displayed_create_folder_btn(self):
        return self.driver.find_element_by_xpath(self.create_new_directory_btn_xpath).is_displayed()

    def create_new_folder(self, name, description):
        self.driver.find_element_by_xpath(self.create_new_directory_btn_xpath).click()
        self.driver.find_element_by_xpath(self.directory_name_input_xpath).send_keys(name)
        self.waits().wait_for_element_one_second()
        self.driver.find_element_by_xpath(self.directory_description_textarea_xpath).send_keys(description)
        self.waits().wait_for_element_one_second()
        self.driver.find_element_by_xpath(self.create_directory_save_btn_xpath).click()

    def is_displayed_folder(self, name):
        self.driver.find_element_by_xpath(self.sort_directories_by_data_xpath).click()
        self.driver.find_element_by_xpath(self.sort_directories_by_data_xpath).click()
        directory_name_webelement = self.driver.find_element_by_xpath("//span[text()='" + name + "']")
        return directory_name_webelement.is_displayed()

    def delete_first_folder(self):
        self.driver.find_element_by_xpath(self.sort_directories_by_data_xpath).click()
        self.driver.find_element_by_xpath(self.sort_directories_by_data_xpath).click()
        self.driver.find_elements_by_xpath("//span[@class='rd-checkmark']").pop(1).click()
        self.driver.find_element_by_xpath(self.remove_directory_btn_xpath).click()
        self.waits().wait_for_element_one_second()
        self.driver.find_element_by_xpath(self.remove_confirming_directory_save_btn_xpath).click()
        self.waits().wait_for_element_one_second()

    def select_first_product_from_folder(self):
        self.driver.find_elements_by_xpath("//span[@class='rd-checkmark']").pop(1).click()

    def merge_two_folders(self, name, description):
        self.driver.find_element_by_xpath(self.sort_directories_by_data_xpath).click()
        self.driver.find_element_by_xpath(self.sort_directories_by_data_xpath).click()
        self.driver.find_elements_by_xpath("//span[@class='rd-checkmark']").pop(1).click()
        self.driver.find_elements_by_xpath("//span[@class='rd-checkmark']").pop(2).click()
        self.driver.find_element_by_xpath(self.merge_directories_btn_xpath).click()
        self.waits().wait_for_element_one_second()
        self.driver.find_element_by_xpath(self.directory_name_input_xpath).send_keys(name)
        self.waits().wait_for_element_one_second()
        self.driver.find_element_by_xpath(self.directory_description_textarea_xpath).send_keys(description)
        self.waits().wait_for_element_one_second()
        self.driver.find_element_by_xpath(self.create_directory_save_btn_xpath).click()

    def add_product_to_parking_from_cataloque(self):
        self.driver.find_element_by_xpath(self.add_to_parking_from_cataloque_xpath).click()
        self.driver.find_element_by_xpath(self.add_confirming_to_parking_from_cataloque_xpath).click()

    def add_to_parking_from_empty_folder(self):
        self.driver.find_element_by_xpath(self.add_to_parking_from_empty_folder_btn_xpath).click()

    def add_product_to_dedicated_folder_in_parking_from_cataloque(self, name):
        self.driver.find_element_by_xpath(self.add_to_parking_from_cataloque_xpath).click()

        i = 0
        option_selected = Select(self.driver.find_element_by_xpath(self.choose_folder_in_creating_modal_select_xpath)).first_selected_option.text
        while(option_selected[22:]!=name):
            Select(self.driver.find_element_by_xpath(self.choose_folder_in_creating_modal_select_xpath)).select_by_index(i)
            option_selected = Select(self.driver.find_element_by_xpath(
                self.choose_folder_in_creating_modal_select_xpath)).first_selected_option.text
            i=i+1

        self.driver.find_element_by_xpath(self.add_confirming_to_parking_from_cataloque_xpath).click()

    def get_to_folder(self, name):
        self.driver.find_element_by_xpath("//span[text()='" + name + "']").click()

    def is_displayed_product_in_folder(self, symbol):
        return self.driver.find_element_by_xpath("//span[text()='" + symbol + "']").is_displayed()

    def move_product_to_another_folder(self, name):
        self.select_first_product_from_folder()
        self.driver.find_element_by_xpath(self.move_directory_btn_xpath).click()

        i = 0
        option_selected = Select(self.driver.find_element_by_xpath(self.choose_folder_in_creating_modal_select_xpath)).first_selected_option.text
        while(option_selected[22:]!=name):
            Select(self.driver.find_element_by_xpath(self.choose_folder_in_creating_modal_select_xpath)).select_by_index(i)
            option_selected = Select(self.driver.find_element_by_xpath(
                self.choose_folder_in_creating_modal_select_xpath)).first_selected_option.text
            i=i+1

        self.driver.find_element_by_xpath(self.add_confirming_to_parking_from_cataloque_xpath).click()

    def copy_product_to_another_folder(self, name):
        self.select_first_product_from_folder()
        self.driver.find_element_by_xpath(self.copy_directory_btn_xpath).click()

        i = 0
        option_selected = Select(self.driver.find_element_by_xpath(self.choose_folder_in_creating_modal_select_xpath)).first_selected_option.text
        while(option_selected[22:]!=name):
            Select(self.driver.find_element_by_xpath(self.choose_folder_in_creating_modal_select_xpath)).select_by_index(i)
            option_selected = Select(self.driver.find_element_by_xpath(
                self.choose_folder_in_creating_modal_select_xpath)).first_selected_option.text
            i=i+1

        self.driver.find_element_by_xpath(self.add_confirming_to_parking_from_cataloque_xpath).click()

    def get_prices_and_stocks(self):
        self.driver.find_element_by_xpath(self.get_prices_and_stocks_btn_xpath).click()

    def is_displayed_price_and_stock(self):
        try:
            x = self.driver.find_element_by_xpath(self.is_displayed_price_and_stock_xpath).is_enabled()
            return x
        except:
            return False
