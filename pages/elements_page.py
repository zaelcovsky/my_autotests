from pages.base_page import BasePage
from locators.elements_page_locators import *
from generator.generator import *
import allure
import requests
import time
import os
import base64
import random
from selenium.common import TimeoutException


@allure.suite("TextBox page")
class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    @allure.title("fill all field")
    def fill_all_field(self):
        info = next(get_person())
        full_name = info.full_name
        email = info.email
        current_address = info.current_address
        permanent_address = info.permanent_address
        with allure.step("Filled all fields and click"):
            self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
            # self.driver.execute_script("window.scrollBy(0, 200);")
            self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    @allure.title("Check filled field")
    def check_filled_field(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


@allure.suite("CheckBox page")
class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    @allure.title("open full list")
    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_BUTTON).click()

    @allure.title("click random checkboxes")
    def click_random(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 5
        while count !=0:
            item = item_list[random.randint(1, 16)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    @allure.title("get checked box")
    def get_checked_box(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        lst = []
        for i in checked_list:
            item = i.find_element('xpath', self.locators.TITLE_ITEM)
            lst.append(item.text)
        return str(lst).replace(' ', '').replace('doc', '').replace('.', '').lower()

    @allure.title("get output result")
    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT)
        lst = []
        for i in result_list:
            lst.append(i.text)
        return str(lst).replace(' ', '').lower()


@allure.suite("Radio button page")
class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.title("check click on the radio button")
    def click_on_the_radio_button(self, choice):
        choices = {
            'yes': self.locators.YES_BUTTON,
            'impressive': self.locators.IMPRESSIVE_BUTTON,
            'no': self.locators.NO_BUTTON
        }
        click_button = self.element_is_visible(choices[choice]).click()

    @allure.title("check get output result")
    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


@allure.suite("Web table page")
class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    @allure.title("add new person")
    def add_new_person(self, count=1):
        while count != 0:
            info = next(get_person())
            first_name = info.first_name
            last_name = info.last_name
            email = info.email
            age = info.age
            salary = info.salary
            department = info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()
            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]

    @allure.title("check new added person")
    def check_new_added_person(self):
        people = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for i in people:
            data.append(i.text.splitlines())
        return data

    @allure.title("search people")
    def search_people(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    @allure.title("check found person")
    def check_people(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element("xpath", self.locators.ROW_PARENT)
        return row.text.splitlines()

    @allure.title("update person info")
    def update_person_info(self):
        info = next(get_person())
        age = info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)

    @allure.title("delete person")
    def delete_person(self):
        self.element_is_present(self.locators.DELETE_BUTTON).click()

    @allure.title("check deleted person")
    def check_deleted(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    @allure.title("select up to rows")
    def select_up_to_rows(self):
        self.remove_footer()
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for i in count:
            count_row_button = self.element_is_present(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            time.sleep(1)
            self.element_is_visible((By.CSS_SELECTOR, f"""option[value="{i}"]""")).click()
            data.append(self.check_count_row())
            time.sleep(1)
        return data

    @allure.title("check count rows")
    def check_count_row(self):
        list_row = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_row)


@allure.suite("Web buttons page")
class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    @allure.step("click on different buttons")
    def click_on_different_button(self, type_click):
        if type_click == "double":
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_DOUBLE)
        if type_click == "right":
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_RIGHT)
        if type_click == "click":
            self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_the_button(self.locators.SUCCESS_CLICK_ME)

    @allure.title("check clicked on the button")
    def check_clicked_on_the_button(self, elem):
        return self.element_is_present(elem).text


@allure.suite("Links page")
class LinksPage(BasePage):
    locators = LinksPageLocators

    @allure.title("Click on simple link")
    def click_on_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        print(link_href)
        response = requests.get(link_href)
        if response.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            print(url)
            return link_href, url, response.status_code, response.reason
        else:
            return link_href, link_href, response.status_code, response.reason

        ###### def click_on_simple_link_v2
    @allure.title("Click on simple link v2")
    def click_on_simple_link_v2(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        print(link_href)
        simple_link.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        url = self.driver.current_url
        print(url)
        return link_href, url

    @allure.title("Click on dynamic link")
    def click_on_dynamic_link(self):
        simple_link = self.element_is_visible(self.locators.DYNAMIC_LINK)
        link_href = simple_link.get_attribute('href')
        # Разные варианты доставания текста из тега
        text = simple_link.text
        text1 = self.driver.find_element(By.CSS_SELECTOR, "a[id='dynamicLink']").text
        text2 = self.driver.find_element(By.CSS_SELECTOR, "a[id='dynamicLink']").get_attribute("textContent")
        text3 = self.driver.find_element(By.CSS_SELECTOR, "a[id='dynamicLink']").get_attribute("innerHTML")
        print(link_href)
        print(text)
        print(text1)
        print(text2)
        print(text3)
        response = requests.get(link_href)
        if response.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            print(url)
            return text, link_href, url, response.status_code, response.reason
        else:
            return text, link_href, link_href, response.status_code, response.reason

    @allure.title("click on broken link")
    def click_on_the_broken_link(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST_LINK).click()
        else:
            return response.status_code

    # !!!!!!!!!!!!!!!! тест Дениса на страницу /links
    @allure.step('check all links')
    def click_on_the_all_links(self, item):
        self.element_is_visible(self.locators.ALL_LINKS[item[0]]).click()
        text = self.element_is_visible(self.locators.TEXT_AFTER_CLICK).text
        print(text)
        response = requests.get(item[1])
        status_reason = response.reason
        status_code = str(response.status_code)
        return text, status_reason, status_code

    # !!!!!!!!!!!!!!!! мои тесты на страницу /links
    @allure.title("click on created link")
    def click_on_the_created_link(self):
        self.element_is_visible(self.locators.CREATED_LINK).click()
        response_code = self.element_is_present(self.locators.RESPONSE_CODE).text
        response_reason = self.element_is_present(self.locators.RESPONSE_REASON).text
        response = requests.get("https://demoqa.com/created")
        return response_code, response_reason, response.status_code, response.reason

    @allure.title("click on no-content link")
    def click_on_the_no_content_link(self):
        self.element_is_visible(self.locators.NO_CONTENT_LINK).click()
        response_code = self.element_is_present(self.locators.RESPONSE_CODE).text
        response_reason = self.element_is_present(self.locators.RESPONSE_REASON).text
        response = requests.get("https://demoqa.com/no-content")
        return response_code, response_reason, response.status_code, response.reason

    @allure.title("click on moved link")
    def click_on_the_moved_link(self):
        self.element_is_visible(self.locators.MOVED_LINK).click()
        response_code = self.element_is_present(self.locators.RESPONSE_CODE).text
        response_reason = self.element_is_present(self.locators.RESPONSE_REASON).text
        response = requests.get("https://demoqa.com/moved")
        return response_code, response_reason, response.status_code, response.reason

    @allure.title("click on bad request link")
    def click_on_the_bad_request_link(self):
        self.element_is_visible(self.locators.BAD_REQUEST_LINK).click()
        response_code = self.element_is_present(self.locators.RESPONSE_CODE).text
        response_reason = self.element_is_present(self.locators.RESPONSE_REASON).text
        response = requests.get("https://demoqa.com/bad-request")
        return response_code, response_reason, response.status_code, response.reason

    @allure.title("click on unauthorized link")
    def click_on_the_unauthorized_link(self):
        self.element_is_visible(self.locators.UNAUTHORIZED_LINK).click()
        response_code = self.element_is_present(self.locators.RESPONSE_CODE).text
        response_reason = self.element_is_present(self.locators.RESPONSE_REASON).text
        response = requests.get("https://demoqa.com/unauthorized")
        return response_code, response_reason, response.status_code, response.reason

    @allure.title("click on forbidden link")
    def click_on_the_forbidden_link(self):
        self.element_is_visible(self.locators.FORBIDDEN_LINK).click()
        response_code = self.element_is_present(self.locators.RESPONSE_CODE).text
        response_reason = self.element_is_present(self.locators.RESPONSE_REASON).text
        response = requests.get("https://demoqa.com/forbidden")
        return response_code, response_reason, response.status_code, response.reason

    @allure.title("click on not found link")
    def click_on_the_not_found_link(self):
        self.element_is_visible(self.locators.NOT_FOUND_LINK).click()
        response_code = self.element_is_present(self.locators.RESPONSE_CODE).text
        response_reason = self.element_is_present(self.locators.RESPONSE_REASON).text
        response = requests.get("https://demoqa.com/invalid-url")
        return response_code, response_reason, response.status_code, response.reason

    # PARAMETRIZE (было 49 строк стало 44 строки)
    @allure.title("click on different link")
    def click_on_the_different_link(self, selector):
        if selector == 'NOT_FOUND_LINK':
            self.element_is_visible(self.locators.NOT_FOUND_LINK).click()
            response_code = self.element_is_present(self.locators.RESPONSE_CODE).text
            response_reason = self.element_is_present(self.locators.RESPONSE_REASON).text
            response = requests.get("https://demoqa.com/invalid-url")
            return response_code, response_reason, response.status_code, response.reason
        if selector == "FORBIDDEN_LINK":
            self.element_is_visible(self.locators.FORBIDDEN_LINK).click()
            response_code = self.element_is_present(self.locators.RESPONSE_CODE).text
            response_reason = self.element_is_present(self.locators.RESPONSE_REASON).text
            response = requests.get("https://demoqa.com/forbidden")
            return response_code, response_reason, response.status_code, response.reason
        if selector == "UNAUTHORIZED_LINK":
            self.element_is_visible(self.locators.UNAUTHORIZED_LINK).click()
            response_code = self.element_is_present(self.locators.RESPONSE_CODE).text
            response_reason = self.element_is_present(self.locators.RESPONSE_REASON).text
            response = requests.get("https://demoqa.com/unauthorized")
            return response_code, response_reason, response.status_code, response.reason
        if selector == "BAD_REQUEST_LINK":
            self.element_is_visible(self.locators.BAD_REQUEST_LINK).click()
            response_code = self.element_is_present(self.locators.RESPONSE_CODE).text
            response_reason = self.element_is_present(self.locators.RESPONSE_REASON).text
            response = requests.get("https://demoqa.com/bad-request")
            return response_code, response_reason, response.status_code, response.reason
        if selector == "MOVED_LINK":
            self.element_is_visible(self.locators.MOVED_LINK).click()
            response_code = self.element_is_present(self.locators.RESPONSE_CODE).text
            response_reason = self.element_is_present(self.locators.RESPONSE_REASON).text
            response = requests.get("https://demoqa.com/moved")
            return response_code, response_reason, response.status_code, response.reason
        if selector == "NO_CONTENT_LINK":
            self.element_is_visible(self.locators.NO_CONTENT_LINK).click()
            response_code = self.element_is_present(self.locators.RESPONSE_CODE).text
            response_reason = self.element_is_present(self.locators.RESPONSE_REASON).text
            response = requests.get("https://demoqa.com/no-content")
            return response_code, response_reason, response.status_code, response.reason
        if selector == "CREATED_LINK":
            self.element_is_visible(self.locators.CREATED_LINK).click()
            response_code = self.element_is_present(self.locators.RESPONSE_CODE).text
            response_reason = self.element_is_present(self.locators.RESPONSE_REASON).text
            response = requests.get("https://demoqa.com/created")
            return response_code, response_reason, response.status_code, response.reason

        # мой улучшенный вариант PARAMETRIZE (было 44 строки стало 44 строки)
    @allure.title("click on different link v2")
    def click_on_the_different_link_v2(self, item1, item2):
        self.element_is_visible(self.locators.ALL_LINKS[item1]).click()
        response_code = self.element_is_present(self.locators.RESPONSE_CODE).text
        response_reason = self.element_is_present(self.locators.RESPONSE_REASON).text
        response = requests.get(item2)
        return response_code, response_reason, response.status_code, response.reason


@allure.suite("Download page")
class DownloadPage(BasePage):
    locators = DownLoadPageLocators

    @allure.title("download file")
    def download_file(self):
        link = self.element_is_present(self.locators.DOWNLOAD_FILE).get_attribute('href')
        link_b = base64.b64decode(link)
        print(link_b)
        path_name_file = rf'C:\Users\stas\PycharmProjects\my_autotests\test{random.randint(0, 999)}.jpg'
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            print(offset)
            print(link_b[offset:])
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
        os.remove(path_name_file)
        return check_file


@allure.suite("Upload page")
class UploadPage(BasePage):
    locators = UploadPageLocators

    @allure.step('upload file')
    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        text = self.element_is_present(self.locators.UPLOADED_FILE).text
        return file_name.split("\\")[-1], text.split('\\')[-1]


@allure.suite("Dynamic Properties Page")
class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators

    @allure.step('check enable button')
    def check_enable_button(self):
        try:
            self.element_is_clickable(self.locators.ENABLE_AFTER_FIVE_SECOND, 5)
        except TimeoutException:
            return "Timeout"
        return True

    @allure.step('check change of color')
    def check_changed_of_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property("color")
        time.sleep(6)
        color_button_after = color_button.value_of_css_property("color")
        return color_button_before, color_button_after

    @allure.step('check appear button')
    def check_appear_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_FIVE_SECOND)
        except TimeoutException:
            return "Timeout"
        return True












