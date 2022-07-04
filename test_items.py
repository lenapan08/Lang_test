from selenium.webdriver.common.by import By

def test_check_user_lang(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button.[btn.btn-lg.btn-primary.btn-add-to-basket]")
    assert button >0,  "Button not found"