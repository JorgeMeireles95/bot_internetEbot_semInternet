#bot internet com Selenium
import time

from selenium import webdriver



navegador = webdriver.Chrome()
navegador.get("https://login.live.com")
navegador.find_element_by_xpath('//*[@id="i0116"]').send_keys("email@hotmail.com")
navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="i0118"]').send_keys("password")
navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="KmsiCheckboxField"]').click()
navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()