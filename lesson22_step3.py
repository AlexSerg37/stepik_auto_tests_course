from selenium import webdriver
import time
import math

from selenium.webdriver.support.ui import Select
link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x1 = browser.find_element_by_id("num1")
y1 = browser.find_element_by_id("num2")
x = x1.text
y = y1.text

s = int(x)+int(y)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(s))

button = browser.find_element_by_class_name("btn.btn-default")
button.click()