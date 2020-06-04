import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "book"))).click()

    x = browser.find_element_by_css_selector("span#input_value.nowrap")
    browser.execute_script("return arguments[0].scrollIntoView(true);", x)
    x = calc(int(x.text))
    browser.find_element_by_css_selector("input#answer.form-control").send_keys(x)
    browser.find_element_by_css_selector("button#solve.btn.btn-primary").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
