#залишити усі пусті поля і спробувати зареєструватись
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get('https://uakino.club')
driver.maximize_window()

xpath_button_authorisation = '//i[@class="fa fa-user"]'
WebDriverWait(driver, 50).until(EC.presence_of_element_located(('xpath', xpath_button_authorisation)))
button_authorisation = driver.find_element('xpath', xpath_button_authorisation)
button_authorisation.click()
driver.get_screenshot_as_file('1.png')

xpath_registration ='//a[@class="log-register"]'
WebDriverWait(driver, 50).until(EC.presence_of_element_located(('xpath', xpath_registration)))
button_registration = driver.find_element('xpath', xpath_registration)
button_registration.click()

xpath_field_login_reg = '//input[@name="name"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_field_login_reg)))
field_login_reg = driver.find_element('xpath', xpath_field_login_reg)
field_login_reg.send_keys('')
driver.get_screenshot_as_file('2.png')
xpath_button_login_check = '//input[@class="register-check"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_button_login_check)))
button_login_check = driver.find_element('xpath', xpath_button_login_check)
button_login_check.click()
driver.get_screenshot_as_file('3.png')
xpath_field_password_reg1 = '//input[@name="password1"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_field_password_reg1)))
field_password_reg1 = driver.find_element('xpath', xpath_field_password_reg1)
field_password_reg1.send_keys('')
driver.get_screenshot_as_file('4.png')
xpath_field_password_reg2 = '//input[@name="password2"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_field_password_reg2)))
field_password_reg2 = driver.find_element('xpath', xpath_field_password_reg2)
field_password_reg2.send_keys('')

xpath_field_email_reg = '//input[@name="email"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_field_email_reg)))
field_email_reg = driver.find_element('xpath', xpath_field_email_reg)
field_email_reg.send_keys('')
driver.get_screenshot_as_file('5.png')

xpath_button_send_reg = '//button[@name="submit"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_button_send_reg)))
button_send_reg = driver.find_element('xpath', xpath_button_send_reg)
button_send_reg.click()
driver.get_screenshot_as_file('6.png')