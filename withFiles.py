from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os



try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome("chromedriver.exe")
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[1]")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[2]")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[3]")
    input3.send_keys("email")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    browser.find_element(By.CSS_SELECTOR, "#file").send_keys(file_path)

    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
