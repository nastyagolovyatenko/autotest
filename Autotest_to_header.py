from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://uakino.club')
driver.maximize_window()

xpath_movies = '//span[@itemprop="name"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_movies)))
movies = driver.find_element('xpath', xpath_movies)
movies.click()
xpath_all_movies = '//div/ul//li/a[@href="/filmy/"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_all_movies)))
all_movies = driver.find_element('xpath', xpath_all_movies)
all_movies.click()
driver.get_screenshot_as_file('1.png')

xpath_serials = '//a[@itemprop="url"][@href="/seriesss/"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_serials)))
serials = driver.find_element('xpath', xpath_serials)
serials.click()
driver.get_screenshot_as_file('2.png')

xpath_cartoons = '//a[@itemprop="url"][@href="/cartoon/"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_cartoons)))
cartoons = driver.find_element('xpath', xpath_cartoons)
cartoons.click()
driver.get_screenshot_as_file('3.png')

xpath_collections = '//a[@itemprop="url"][@href="/colections/"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_collections)))
collections = driver.find_element('xpath', xpath_collections)
collections.click()
driver.get_screenshot_as_file('4.png')
xpath_community = '//a[@class="nolink-menu"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_community)))
community = driver.find_element('xpath', xpath_community)
community.click()
driver.get_screenshot_as_file('5.png')
xpath_announcements= '//a[@href="/anonsi/"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_announcements)))
announcements = driver.find_element('xpath', xpath_announcements)
announcements.click()
driver.get_screenshot_as_file('6.png')
xpath_year_2022 = '//a[@href="/find/year/2022/"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_year_2022)))
year_2022 = driver.find_element('xpath', xpath_year_2022)
year_2022.click()
driver.get_screenshot_as_file('7.png')
xpath_top_100 = '//a[@href="/top100all.html"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_top_100)))
top_100 = driver.find_element('xpath', xpath_top_100)
top_100.click()
driver.get_screenshot_as_file('8.png')
xpath_emoji_range = '//a[@href="/emoticon"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_emoji_range)))
emoji_range = driver.find_element('xpath', xpath_emoji_range)
emoji_range.click()
driver.get_screenshot_as_file('9.png')
xpath_my_list = '//a[@class="show-fav"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_my_list)))
my_list = driver.find_element('xpath', xpath_my_list)
my_list.click()
driver.get_screenshot_as_file('10.png')
xpath_search = '//i[@class="fa fa-search show-search"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_search)))
search = driver.find_element('xpath', xpath_search)
search.click()
driver.get_screenshot_as_file('11.png')
xpath_search_field = '//input[@placeholder="Введіть слово для пошуку..."]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_search_field)))
search_field = driver.find_element('xpath', xpath_search_field)
search_field.send_keys('Witcher')
driver.get_screenshot_as_file('12.png')
xpath_button_search_submit = '//button[@type="submit"][@title="Шукати"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_button_search_submit)))
search_submit = driver.find_element('xpath', xpath_button_search_submit)
search_submit.click()

driver.get_screenshot_as_file('13.png')
xpath_ret_to_main_page = '//a[@class="logo-box"]'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(('xpath', xpath_ret_to_main_page)))
ret_to_main_page = driver.find_element('xpath', xpath_ret_to_main_page)
ret_to_main_page.click()
driver.get_screenshot_as_file('14.png')







