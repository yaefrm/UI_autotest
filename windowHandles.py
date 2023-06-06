from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome("chromedriver.exe")
    browser.get(link)

    button = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    button_submit = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
    button_submit.click()

finally:
    time.sleep(30)
    browser.quit()


