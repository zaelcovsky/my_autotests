from selenium.webdriver.common.by import By
import allure
import random


class AlertsPageLocators:

    NEW_TAB = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_WINDOW = (By.CSS_SELECTOR, "button[id='windowButton']")
    NEW_WINDOW_MESSAGE = (By.CSS_SELECTOR, "button[id='messageWindowButton']")
    SAMPLE_PAGE_TEXT = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
    TEXT = (By.CSS_SELECTOR, "body")