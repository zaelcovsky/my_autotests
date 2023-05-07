import pytest
import allure
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service # as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    adblockpath = r'C:\Users\stas\PycharmProjects\1.48.4_55'
    # chrome_options.add_argument('loadextension=' + adblockpath)
    chrome_options.add_argument('--load-extension={}'.format(r'C:\Users\stas\PycharmProjects\1.48.4_55'))
    # chrome_options.add_extension(r'C:\Users\stas\PycharmProjects\1.49.0_0.crx')
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install(), options=chrome_options))
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    # driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
    driver.maximize_window()
    # driver.set_window_size(800, 600)
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f'Screenshot {datetime.today}', attachment_type=allure.attachment_type.PNG)
    driver.quit()
