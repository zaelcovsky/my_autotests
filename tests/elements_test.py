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
        def test_different_click_on_the_button_v2(self, driver, item):
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
            href_link, current_url, status_code, reason = links_page.click_on_simple_link()
            assert href_link == current_url, "Link is broken or url is incorrect"
            assert status_code == 200, f"response status is {status_code} {reason}"

        @allure.title("Check simple link v2")
        def test_check_simple_link_v2(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            href_link, current_url = links_page.click_on_simple_link_v2()
            assert href_link == current_url, "The link is broken or url is incorrect"

        @allure.title("Check dynamic link")
        def test_check_dynamic_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            text, href_link, current_url, status_code, reason = links_page.click_on_dynamic_link()
            assert text[:4] == "Home"
            assert href_link == current_url, "Link is broken or url is incorrect"
            assert status_code == 200, f"response status is {status_code} {reason}"


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

        # !!!!!!!!!!!!!!!!   Вариант Дениса
        links = [(0, "https://demoqa.com/created"),
                 (1, "https://demoqa.com/no-content"),
                 (2, "https://demoqa.com/moved"),
                 (3, "https://demoqa.com/bad-request"),
                 (4, "https://demoqa.com/unauthorized"),
                 (5, "https://demoqa.com/forbidden"),
                 (6, "https://demoqa.com/invalid-url")]

        @pytest.mark.parametrize("item", links)
        @allure.title("Check all links")
        def test_check_all_links(self, driver, item):
            link_page = LinksPage(driver, "https://demoqa.com/links")
            link_page.open()
            text, status_reason, status_code = link_page.click_on_the_all_links(item)
            assert status_code in text, "Wrong status code"
            assert status_reason in text, "Wrong status reason"

        # !!!!!!!!!!!!!!!!!!  мои тесты на страницу /links
        @allure.title("Check the created link")
        def test_created_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code, response_reason, status_code, reason = links_page.click_on_the_created_link()
            print(response_reason)
            print(reason)
            assert int(response_code) == status_code, "The link don't work or the status code is not 201"
            assert response_reason == reason, "The link don't work or the status reason is not 'CREATED'"

        @allure.title("Check the no-content link")
        def test_no_content_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code, response_reason, status_code, reason = links_page.click_on_the_no_content_link()
            print(response_reason)
            print(reason)
            assert int(response_code) == status_code, "The link don't work or the status code is not 204"
            assert response_reason == reason, "The link don't work or the status reason is not 'NO CONTENT'"

        @allure.title("Check the moved link")
        def test_moved_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code, response_reason, status_code, reason = links_page.click_on_the_moved_link()
            print(response_reason)
            print(reason)
            assert int(response_code) == status_code, "The link don't work or the status code is not 301"
            assert response_reason == reason, "The link don't work or the status reason is not 'MOVED PERMANENTLY'"

        @allure.title("Check the bad request link")
        def test_bad_request_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code, response_reason, status_code, reason = links_page.click_on_the_bad_request_link()
            print(response_reason)
            print(reason)
            assert int(response_code) == status_code, "The link don't work or the status code is not 400"
            assert response_reason == reason, "The link don't work or the status reason is not 'BAD REQUEST'"

        @allure.title("Check the unauthorized link")
        def test_unauthorized_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code, response_reason, status_code, reason = links_page.click_on_the_unauthorized_link()
            print(response_reason)
            print(reason)
            assert int(response_code) == status_code, "The link don't work or the status code is not 401"
            assert response_reason == reason, "The link don't work or the status reason is not 'UNAUTHORIZED'"

        @allure.title("Check the forbidden link")
        def test_forbidden_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code, response_reason, status_code, reason = links_page.click_on_the_forbidden_link()
            print(response_reason)
            print(reason)
            assert int(response_code) == status_code, "The link don't work or the status code is not 403"
            assert response_reason == reason, "The link don't work or the status reason is not 'FORBIDDEN'"

        @allure.title("Check the not found link")
        def test_not_found_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code, response_reason, status_code, reason = links_page.click_on_the_not_found_link()
            print(response_reason)
            print(reason)
            assert int(response_code) == status_code, "The link don't work or the status code is not 404"
            assert response_reason == reason, "The link don't work or the status reason is not 'NOT FOUND'"

        # PARAMETRIZE (было 63 строки стало 11 строк)
        # selectors = [('NOT_FOUND_LINK', '500'), 'FORBIDDEN_LINK', 'UNAUTHORIZED_LINK', 'BAD_REQUEST_LINK', 'MOVED_LINK', 'NO_CONTENT_LINK', 'CREATED_LINK']
        selectors = [('NOT_FOUND_LINK', '404', 'Not Found'), ('FORBIDDEN_LINK', '403', 'Forbidden'), ('UNAUTHORIZED_LINK', '401', 'Unauthorized'), ('BAD_REQUEST_LINK', '400', 'Bad Request'), ('MOVED_LINK', '301', 'Moved Permanently'), ('NO_CONTENT_LINK', '204', 'No Content'), ('CREATED_LINK', '201', 'Created')]
        @allure.title("Check the different links")
        @pytest.mark.parametrize("item1, item2, item3", selectors)
        def test_different_links(self, driver, item1, item2, item3):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code, response_reason, status_code, reason = links_page.click_on_the_different_link(item1)
            print(f'{response_code} = {status_code}')
            print(f'{response_reason} = {reason}')
            assert int(response_code) == status_code, f"The link don't work or the status code is not {item2}"
            assert response_reason == reason, f"The link don't work or the status reason is not '{item3}'"


        # мой улучшенный вариант PARAMETRIZE (было 44 строки стало 17 строк)
        links_codes = [(0, "https://demoqa.com/created", '201', 'Created'),
                 (1, "https://demoqa.com/no-content", '403', 'Forbidden'),
                 (2, "https://demoqa.com/moved", '401', 'Unauthorized'),
                 (3, "https://demoqa.com/bad-request", '400', 'Bad Request'),
                 (4, "https://demoqa.com/unauthorized", '301', 'Moved Permanently'),
                 (5, "https://demoqa.com/forbidden", '204', 'No Content'),
                 (6, "https://demoqa.com/invalid-url", '404', 'Not Found')]

        @allure.title("Check the different links v2")
        @pytest.mark.parametrize("item1, item2, item3, item4", links_codes)
        def test_different_links_v2(self, driver, item1, item2, item3, item4):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code, response_reason, status_code, reason = links_page.click_on_the_different_link_v2(item1, item2)
            print(f'{response_code} = {status_code}')
            print(f'{response_reason} = {reason}')
            assert int(response_code) == status_code, f"The link don't work or the status code is not {item3}"
            assert response_reason == reason, f"The link don't work or the status reason is not '{item4}'"

    @allure.feature("Check Download and Upload page")
    class TestDownloadAndUploadPage:
        @allure.title("Check download file")
        def test_download_file(self, driver):
            download_page = DownloadPage(driver, 'https://demoqa.com/upload-download')
            download_page.open()
            check = download_page.download_file()
            assert check is True, "File was not downloaded"

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

        @allure.title("Check appear button")
        def test_appear_button(self, driver):
            appear_button = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            appear_button.open()
            button = appear_button.check_appear_button()
            assert button is True, "Button don't appear"










