from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")


price = WebDriverWait(browser, 12).until(
		EC.text_to_be_present_in_element((By. ID, "price"),"10000")
		)

button = browser.find_element_by_id("book")
button.click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


x = browser.find_element_by_id("input_value").text
print ("x= ", x)
result = calc(x)
print ("result= ", result)

answer = browser.find_element_by_id("answer")
answer.send_keys(result)

button = browser.find_element_by_id("solve")
button.click()

