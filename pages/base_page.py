import allure
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


@allure.suite("Basepage")
class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.title("Open")
    def open(self):
        self.driver.get(self.url)

    @allure.title("Element is visible")
    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.title("Elements are visible")
    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.title("Element is present")
    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.title("Elements are present")
    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.title("Element is not visible")
    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.title("Element is clickable")
    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.title("Go to element")
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Remove footer')
    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")

    @allure.step('Double click')
    def action_double_click(self, elem):
        action = ActionChains(self.driver)
        action.double_click(elem)
        action.perform()

    @allure.step('Right click')
    def action_right_click(self, elem):
        action = ActionChains(self.driver)
        action.context_click(elem)
        action.perform()




