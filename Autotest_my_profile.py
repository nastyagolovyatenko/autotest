import time
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

xpath_field_login_name = '//input[@name="login_name"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_field_login_name)))
field_login_name = driver.find_element('xpath', xpath_field_login_name)
field_login_name.send_keys('aaabbbcccee')

xpath_field_password = '//input[@name="login_password"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_field_password)))
field_password = driver.find_element('xpath', xpath_field_password)
field_password.send_keys('123456')
driver.get_screenshot_as_file('2.png')

xpath_button_submit = '//button[@onclick="submit();"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_button_submit)))
button_submit = driver.find_element('xpath', xpath_button_submit)
button_submit.click()
driver.get_screenshot_as_file('3.png')

xpath_my_cabinet = '//i[@class="fa fa-cog"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_my_cabinet)))
my_cabinet = driver.find_element('xpath', xpath_my_cabinet)
my_cabinet.click()
driver.get_screenshot_as_file('4.png')

#  Мій профіль


xpath_my_profile = '//a[@href="https://uakino.club/user/aaabbbcccee/"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_my_profile)))
my_profile = driver.find_element('xpath', xpath_my_profile)
my_profile.click()

driver.execute_script("window.scrollBy(0,1000)")
time.sleep(10)
driver.get_screenshot_as_file('5.png')

xpath_edit_profile = '//div[@class="user-edit"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_edit_profile)))
edit_profile = driver.find_element('xpath', xpath_edit_profile)
edit_profile.click()
driver.execute_script("window.scrollBy(0,2000)")
time.sleep(10)

new_name_user = 'aaabbbccceer'
xpath_change_name = '//input[@type="text"][@name="fullname"]'
WebDriverWait(driver, 130).until(EC.presence_of_element_located(('xpath', xpath_change_name)))
field_change_name = driver.find_element('xpath', xpath_change_name)
field_change_name.click()
field_change_name.clear()
field_change_name.send_keys(new_name_user)

new_email = 'ddkkgfd@gmail.com'
xpath_change_email = '//input[@name="email"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_change_email)))
field_change_email = driver.find_element('xpath', xpath_change_email)
field_change_email.click()
field_change_email.clear()
field_change_email.send_keys(new_email)

xpath_checkbox_allow_mail = '//input[@type="checkbox"][@name="allow_mail"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_checkbox_allow_mail)))
checkbox_allow_mail = driver.find_element('xpath', xpath_checkbox_allow_mail)
checkbox_allow_mail.click()

xpath_checkbox_subscribe = '//input[@type="checkbox"][@name="subscribe"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_checkbox_subscribe)))
checkbox_subscribe = driver.find_element('xpath', xpath_checkbox_subscribe)
checkbox_subscribe.click()

new_land = 'hfjlloirriood'
xpath_change_land = '//input[@name="land"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_change_land)))
field_change_land = driver.find_element('xpath', xpath_change_land)
field_change_land.click()
field_change_land.clear()
field_change_land.send_keys(new_land)
driver.get_screenshot_as_file('6.png')

old_pass = '123456'
xpath_field_old_password = '//input[@name="altpass"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_field_old_password)))
field_old_password = driver.find_element('xpath', xpath_field_old_password)
field_old_password.send_keys(old_pass)

new_pass1 = '123456'
xpath_field_new_password1 = '//input[@name="password1"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_field_new_password1)))
field_new_password1 = driver.find_element('xpath', xpath_field_new_password1)
field_new_password1.send_keys(new_pass1)

new_pass2 = '123456'
xpath_field_new_password2 = '//input[@name="password2"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_field_new_password2)))
field_new_password2 = driver.find_element('xpath', xpath_field_new_password2)
field_new_password2.send_keys(new_pass2)

xpath_checkbox_del_avatar = '//input[@type="checkbox"][@name="del_foto"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_checkbox_del_avatar)))
checkbox_del_avatar = driver.find_element('xpath', xpath_checkbox_del_avatar)
checkbox_del_avatar.click()
driver.get_screenshot_as_file('7.png')

#вибір регіону з випадаючого списку

xpath_select_region = '//select[@class="timezoneselect"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_select_region)))
select_region = driver.find_element('xpath', xpath_select_region)
select_region.click()

xpath_select_region2 = '//select[@class="timezoneselect"]/option[@value="America/Tijuana"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_select_region2)))
select_region2 = driver.find_element('xpath', xpath_select_region2)
select_region2.click()

text = 'uytfdekkkrhhhyyswh'
xpath_change_inf_about_me = '//textarea[@name="info"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_change_inf_about_me)))
change_inf_about_me = driver.find_element('xpath', xpath_change_inf_about_me)
change_inf_about_me.click()
change_inf_about_me.clear()
change_inf_about_me.send_keys(text)
driver.get_screenshot_as_file('8.png')

xpath_send = '//button[@name="submit"][@class="fbutton"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_send)))
button_send = driver.find_element('xpath', xpath_send)
button_send.click()
driver.get_screenshot_as_file('9.png')


#Повідомлення

xpath_my_profile = '//a[@href="https://uakino.club/user/aaabbbccceer/"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_my_profile)))
my_profile = driver.find_element('xpath', xpath_my_profile)
my_profile.click()

xpath_messege ='//a[@href="https://uakino.club/index.php?do=pm"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_messege)))
messege = driver.find_element('xpath', xpath_messege)
messege.click()
driver.get_screenshot_as_file('9.png')

#Мої закладки
xpath_my_profile = '//a[@href="https://uakino.club/user/aaabbbccceer/"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_my_profile)))
my_profile = driver.find_element('xpath', xpath_my_profile)
my_profile.click()

xpath_bookmarks = '//li/a[@href="/favorites/"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_bookmarks)))
bookmarks = driver.find_element('xpath', xpath_bookmarks)
bookmarks.click()
driver.get_screenshot_as_file('10.png')

xpath_out_of_profile = '//a[@href="https://uakino.club/index.php?action=logout"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_out_of_profile)))
out_of_profile = driver.find_element('xpath', xpath_out_of_profile)
out_of_profile.click()
driver.get_screenshot_as_file('11.png')






