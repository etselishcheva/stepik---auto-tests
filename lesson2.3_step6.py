from selenium import webdriver
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_class_name("btn")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


x = browser.find_element_by_id("input_value").text
print ("x= ", x)
result = calc(x)
print ("result= ", result)

answer = browser.find_element_by_id("answer")
answer.send_keys(result)

button = browser.find_element_by_class_name("btn")
button.click()
