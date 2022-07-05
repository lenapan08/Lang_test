from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# pytest --language=es test_items.py

def test_find_button_add_to_basket(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    button = len(browser.find_elements(By.CSS_SELECTOR, "button[type = 'submit']"))
    assert button > 0,  "Button not found"
