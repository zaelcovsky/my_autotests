import random
import time
import allure
from pages.elements_page import *
import pytest


@allure.suite("Main test")
class TestElements:
    @allure.feature("Test textbox")
    class TestTextBox:
        @allure.title("Test textbox")
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_field()
            out_name, out_email, out_current_address, out_permanent_address = text_box_page.check_filled_field()
            time.sleep(2)
            assert full_name == out_name
            assert email == out_email
            assert current_address == out_current_address
            assert permanent_address == out_permanent_address

    @allure.feature("Test checkbox")
    class TestCheckBox:
        @allure.title("Test checkbox")
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            time.sleep(2)
            check_box_page.click_random()
            input_checkbox = check_box_page.get_checked_box()
            output_checkbox = check_box_page.get_output_result()
            time.sleep(2)
            print(input_checkbox)
            print(output_checkbox)
            assert input_checkbox == output_checkbox

    @allure.feature("Test Radio Button")
    class TestRadioButton:
        @allure.title("Check radiobutton")
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            with allure.step("check click on the buttons"):
                # radio_buttons_list = ['yes', 'impressive', 'no']
                # random.shuffle(radio_buttons_list)
                # for i in radio_buttons_list:
                #     radio_button = radio_button_page.click_on_the_radio_button(i)
                #     output = radio_button_page.get_output_result()
                radio_button_page.click_on_the_radio_button('yes')
                output_yes = radio_button_page.get_output_result()
                radio_button_page.click_on_the_radio_button('impressive')
                output_impressive = radio_button_page.get_output_result()
                radio_button_page.click_on_the_radio_button('no')
                output_no = radio_button_page.get_output_result()
            print(output_yes)
            print(output_impressive)
            print(output_no)
            assert output_yes == "Yes", "Yes radiobutton is not clickable"
            assert output_impressive == "Impressive", "Impressive radiobutton is not clickable"
            assert output_no == "No", "No radiobutton is not clickable"

        # в работе
        @allure.title("Check random radiobutton")
        def test_random_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            with allure.step("check click on the buttons"):
                radio_buttons_list = ['yes', 'impressive', 'no']
                random.shuffle(radio_buttons_list)
                print(radio_buttons_list)
                for i in radio_buttons_list:
                    # time.sleep(2)
                    radio_button_page.click_on_the_radio_button(i)
                    time.sleep(1)
                    output = radio_button_page.get_output_result()
                    print(output)
                # radio_button_page.click_on_the_radio_button('yes')
                # output_yes = radio_button_page.get_output_result()
                # radio_button_page.click_on_the_radio_button('impressive')
                # output_impressive = radio_button_page.get_output_result()
                # radio_button_page.click_on_the_radio_button('no')
                # output_no = radio_button_page.get_output_result()

            # print(output_impressive)
            # print(output_no)
            # assert output ==
            # assert output_yes == "Yes", "Yes radiobutton is not clickable"
            # assert output_impressive == "Impressive", "Impressive radiobutton is not clickable"
            # assert output_no == "No", "No radiobutton is not clickable"

    @allure.feature("Check web table")
    class TestWebTable:

        @allure.title("add new person in table")
        def test_add_person_in_the_table(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            count1 = random.randint(3, 5)
            for i in range(count1):
                new_person = web_table_page.add_new_person()
                time.sleep(1)
                result = web_table_page.check_new_added_person()
                print(new_person)
                print(result)
                assert new_person in result


        @allure.title("add new persons in table")
        def test_add_few_persons_in_the_table(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            count = random.randint(1, 10)
            new_person = web_table_page.add_new_person(count)
            time.sleep(2)
            result = web_table_page.check_new_added_person()
            print(new_person)
            print(result)
            assert new_person in result, "New person not in the table"


        @allure.title("check people in table")
        def test_check_people_in_the_table(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            time.sleep(2)
            web_table_page.search_people(key_word)
            time.sleep(2)
            table_result = web_table_page.check_people()
            time.sleep(3)
            assert key_word in table_result, "Person not found in the table"

        @allure.title("check update person info in table")
        def test_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_people(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_people()
            print(age)
            print(row)
            assert age in row, "The person card has not been changed"

        @allure.title("check delete person info in table")
        def test_delete_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_people(email)
            time.sleep(2)
            web_table_page.delete_person()
            time.sleep(2)
            text = web_table_page.check_deleted()
            assert text == "No rows found", "The person card has not been changed"

        @allure.title("check change in numbers of rows in table")
        def test_change_rows(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            # self.driver.switch_to.window(self.driver.window_handles[0])
            count = web_table_page.select_up_to_rows()
            time.sleep(30)
            print(count)
            assert count == [5, 10, 20, 25, 50, 100], "Numbers of rows has not been changed or has changed incorrectly"

    @allure.feature("Check Buttons Page")
    class TestButtonsPage:

        @allure.title('Checking clicks of different types v1')
        def test_different_click_on_the_button(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            double = button_page.click_on_different_button("double")
            right = button_page.click_on_different_button("right")
            click = button_page.click_on_different_button("click")
            assert double == "You have done a double click", "The double click button was not pressed"
            assert right == "You have done a right click", "The right click button was not pressed"
            assert click == "You have done a dynamic click", "The dynamic click button was not pressed"

        # предыдущий тест с помощью pytest.mark.parametrize
        button = ['double', 'right', 'click']

        @allure.title('Checking clicks of different types v2 (with @pytest.mark.parametrize)')
        @pytest.mark.parametrize("item", button)
        def test_different_click_on_the_button(self, driver, item):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            button = button_page.click_on_different_button(item)
            assert button in ["You have done a double click", "You have done a right click", "You have done a dynamic click"], f"Button was not clicked"

    @allure.feature("Check Links Page")
    class TestLinkPage:

        @allure.title("Check simple link")
        def test_check_simple_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            href_link, current_url = links_page.click_on_simple_link()
            assert href_link == current_url, "Link is broken or url is incorrect"

        #######

        @allure.title("Check the broken link")
        def test_broken_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code = links_page.click_on_the_broken_link("https://demoqa.com/bad-request")
            assert response_code == 400, "The link works or the status code is not 400"

        @allure.title("Check the not found link")
        def test_not_found_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code = links_page.click_on_the_broken_link("https://demoqa.com/invalid-url")
            assert response_code == 404, "The link works or the status code is not 404"

    @allure.feature("Check Download and Upload page")
    class TestDownloadAndUploadPage:
        @allure.title("Check download file")
        def test_download_file(self, driver):
            download_page = DownloadPage(driver, 'https://demoqa.com/upload-download')
            download_page.open()
            check = download_page.download_file()
            assert check is True

        @allure.title("Check upload file")
        def test_upload_file(self, driver):
            upload_file = UploadPage(driver, 'https://demoqa.com/upload-download')
            upload_file.open()
            file_name, result = upload_file.upload_file()
            print(file_name, result)
            assert file_name == result, "File not uploaded"

    @allure.feature("Check dynamic buttons")
    class TestDynamicButtons:
        @allure.title("Check enable button")
        def test_enable_button(self, driver):
            enable_button = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            enable_button.open()
            clickable_button = enable_button.check_enable_button()
            assert clickable_button is True, "Button not enable"

        @allure.title("Check changed color")
        def test_check_changed_color(self, driver):
            color_button = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            color_button.open()
            color_before, color_after = color_button.check_changed_of_color()
            print(color_after, color_before)
            assert color_after != color_before, "Button did not change color"

        @allure.title("Check enable button")
        def test_appear_button(self, driver):
            appear_button = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            appear_button.open()
            button = appear_button.check_appear_button()
            assert button is True, "Button don't appear"







