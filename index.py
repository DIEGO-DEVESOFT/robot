from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui


driver = webdriver.Chrome()
driver.get("https://rad.sdis.gov.co/")
source = driver.page_source
time.sleep(4)
pyautogui.click(705,372)
action = ActionChains(driver) 
x_coord = 705
y_coord = 372
action.move_by_offset(x_coord, y_coord)
action.click()
action.perform()
time.sleep(15)

# pyautogui.click(753,233)
# action = ActionChains(driver) 
# x_coords = 753
# y_coords = 233
# action.move_by_offset(x_coords, y_coords)
# action.click()
# action.perform()
# time.sleep(15)




# user = driver.find_element(By,id("ip_login"))
# user.send_Keys('6573.113426')
# print(pa.position())
# driver=driver.find_element_by_id('ip_login')
# driver.send_keys('6573.113426')
# input_nombre = driver.find_element_by_id('ip_login')
# input_nombre.send_Keys('6573.113426')









