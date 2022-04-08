import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://twitter.com/login")
driver.find_element_by_xpath('//*[@id ="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input').send_keys('motopaedia@gmail.com')
driver.find_element_by_xpath('//*[@id ="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input').send_keys('aaaaaaaa89')

send_keys(Keys.RETURN)
