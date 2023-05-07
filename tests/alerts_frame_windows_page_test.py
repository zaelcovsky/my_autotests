import random
import time
import allure
from pages.alerts_frame_windows_page import *
import pytest


@allure.suite("Main test")
class TestAlerts:
    @allure.feature("Test Browser windows page")
    class TestBrowserWindowsPage:
        @allure.title("Check new tab button")
        def test_new_tab_button(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            sample_link_text, url = browser_windows_page.click_new_tab_button()
            assert sample_link_text == 'This is a sample page', "The link don't work or text is not correct"
            assert url == 'https://demoqa.com/sample', "The link don't work or link is not correct"

        @allure.title("Check new window button")
        def test_new_window_button(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            sample_link_text, url = browser_windows_page.click_new_window_button()
            assert sample_link_text == 'This is a sample page', "The link don't work or text is not correct"
            assert url == 'https://demoqa.com/sample', "The link don't work or link is not correct"

        @allure.title("Check new window message button")
        def test_new_window_message_button(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            url = browser_windows_page.click_new_window_message_button()
            # assert sample_link_text == 'Knowledge increases by sharing but not by saving. Please share this website with your friends and in your organization.', "The link don't work or text is not correct"
            assert url == 'about:blank', "The link don't work or link is not correct"



