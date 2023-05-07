from pages.base_page import BasePage
from locators.alerts_frame_windows_page_locators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from generator.generator import *
import allure
import requests
import time
import os
import base64
import random
from selenium.common import TimeoutException


@allure.suite("Browser windows page")
class BrowserWindowsPage(BasePage):
    locators = AlertsPageLocators()

    @allure.title("new tab button")
    def click_new_tab_button(self):
        sample_link = self.element_is_visible(self.locators.NEW_TAB)
        sample_link.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        url = self.driver.current_url
        sample_link_text = self.element_is_visible(self.locators.SAMPLE_PAGE_TEXT).text
        print(url)
        print(sample_link_text)
        return sample_link_text, url

    # код написан как в доке селениума про windows и tabs https://www.selenium.dev/documentation/webdriver/interactions/windows/
    @allure.title("new window button")
    def click_new_window_button(self):
        # Store the ID of the original window
        original_window = self.driver.current_window_handle
        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1
        # Click the link which opens in a new window
        sample_link = self.element_is_visible(self.locators.NEW_WINDOW)
        sample_link.click()
        # Wait for the new window or tab
        wait(self.driver, 5).until(EC.number_of_windows_to_be(2))
        # Loop through until we find a new window handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        # self.driver.switch_to.window(self.driver.window_handles[1])
        url = self.driver.current_url
        sample_link_text = self.element_is_visible(self.locators.SAMPLE_PAGE_TEXT).text
        print(url)
        print(sample_link_text)
        return sample_link_text, url

    @allure.title("new window message button")
    def click_new_window_message_button(self):
        original_window = self.driver.current_window_handle
        sample_link = self.element_is_visible(self.locators.NEW_WINDOW_MESSAGE)
        sample_link.click()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(1)
        # url = 'about:blank'
        # sample_link_text = "fff"
        # url = self.driver.current_url
        # sample_link_text = self.driver.find_element(By.TAG_NAME, 'body').text
        # sample_link_text = self.element_is_visible(By.XPATH, "//body").text
        sample_link_text = self.element_is_present(self.locators.TEXT).get_attribute("innerHTML")
        self.driver.close()
        self.driver.switch_to.window(original_window)
        # print(url)
        print(sample_link_text)
        return sample_link_text
