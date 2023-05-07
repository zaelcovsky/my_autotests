from selenium.webdriver.common.by import By
import allure
import random


# class FormPageLocators:

    # FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
    # LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    # EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    # GENDER_MALE = (By.CSS_SELECTOR, "input[id='gender-radio-1']")
    # GENDER_FEMALE = (By.CSS_SELECTOR, "input[id='gender-radio-2']")
    # GENDER_OTHER = (By.CSS_SELECTOR, "input[id='gender-radio-3']")
    # GENDER = (By.CSS_SELECTOR, "input[id='gender-radio-3']")
    # MOBILE = (By.CSS_SELECTOR, "input[id='userNumber']")
    # DATE_OF_BIRTH = (By.CSS_SELECTOR, "input[id='dateOfBirthInput']")
    # SUBJECTS = (By.CSS_SELECTOR, "input[id='subjectsInput']")
    # HOBBIES_SPORTS = (By.CSS_SELECTOR, "input[id='hobbies-checkbox-1']")
    # HOBBIES_READING = (By.CSS_SELECTOR, "input[id='hobbies-checkbox-2']")
    # HOBBIES_MUSIC = (By.CSS_SELECTOR, "input[id='hobbies-checkbox-3']")
    # PICTURE = (By.CSS_SELECTOR, "input[id='uploadPicture']")
    # CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    # STATE = (By.CSS_SELECTOR, "input[id='react-select-3-input']")
    # CITY = (By.CSS_SELECTOR, "input[id='react-select-4-input']")
    # SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")


class FormPageLocators:
    FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    GENDER = (By.CSS_SELECTOR, f"label[for='gender-radio-{random.randint(1, 3)}']")
    PHONE_NUMBER = (By.CSS_SELECTOR, "input[id='userNumber']")
    BIRTH_DAY = (By.CSS_SELECTOR, "input[id='dateOfBirthInput']")
    MONTHS_CHANGE = (By.CSS_SELECTOR, f"select[class='react-datepicker__month-select']")
    MONTHS = (By.CSS_SELECTOR, f"select[class='react-datepicker__month-select'] option[value='{random.randint(1, 12)}']")
    YEARS_CHANGE = (By.CSS_SELECTOR, f"select[class='react-datepicker__year-select']")
    YEARS = (By.CSS_SELECTOR, f"select[class='react-datepicker__year-select'] option[value='{random.randint(1900, 2100)}']")
    SUBJECT = (By.CSS_SELECTOR, "input[id='subjectsInput']")
    HOBBIES = (By.CSS_SELECTOR, f"label[for='hobbies-checkbox-{random.randint(1, 3)}']")
    FILE_INPUT = (By.CSS_SELECTOR, "input[id='uploadPicture']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    SELECT_STATE = (By.CSS_SELECTOR, "div[id ='state']")
    STATE_INPUT = (By.CSS_SELECTOR, "input[id='react-select-3-input']")
    SELECT_CITY = (By.CSS_SELECTOR, "div[id ='city']")
    CITY_INPUT = (By.CSS_SELECTOR, "input[id='react-select-4-input']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")
    ALL_TABLE = (By.XPATH, "//div[@class='table-responsive']")


