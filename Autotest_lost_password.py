from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://uakino.club')
driver.maximize_window()

xpath_button_authorisation = '//i[@class="fa fa-user"]'
WebDriverWait(driver, 50).until(EC.presence_of_element_located(('xpath', xpath_button_authorisation)))
button_authorisation = driver.find_element('xpath', xpath_button_authorisation)
button_authorisation.click()
driver.get_screenshot_as_file('1.png')
xpath_lost_password = '//a[@href="https://uakino.club/index.php?do=lostpassword"]'
WebDriverWait(driver, 50).until(EC.presence_of_element_located(('xpath', xpath_lost_password)))
button_lost_password = driver.find_element('xpath', xpath_lost_password)
button_lost_password.click()
driver.get_screenshot_as_file('2.png')
xpath_login_or_email ='//div/input[@name="lostname"]'
WebDriverWait(driver, 50).until(EC.presence_of_element_located(('xpath', xpath_login_or_email)))
field_login_or_email = driver.find_element('xpath', xpath_login_or_email)
field_login_or_email.send_keys('hhgfdddffg@gmail.com')
driver.get_screenshot_as_file('3.png')
xpath_recaptcha = '//div[@class="recaptcha-checkbox-border"]'
WebDriverWait(driver, 50).until(EC.presence_of_element_located(('xpath', xpath_recaptcha)))
recaptcha = driver.find_element('xpath', xpath_recaptcha)
recaptcha.click()
driver.get_screenshot_as_file('4.png')
xpath_submit = '//button[@name="submit"]'
WebDriverWait(driver, 130).until(EC.presence_of_element_located(('xpath', xpath_submit)))
submit = driver.find_element('xpath', xpath_submit)
submit.click()

#на recaptcha автотест посипався, не знаю як її обійти((