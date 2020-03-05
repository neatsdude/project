from selenium import webdriver
from selenium.webdriver.common.keys import Keys
web = webdriver.Chrome('/home/itsneats/pyhome/chromedriver')

web.get('https://www.google.com')
web.find_element_by_name('q').send_keys('Avengers Endgame')
web.find_element_by_name('btnK').send_keys(Keys.ENTER)
web.maximize_window()
web.find_element_by_partial_link_text('en.wikipedia.org').click()
