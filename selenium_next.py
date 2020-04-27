from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import secret as pw

web = webdriver.Chrome('C:\\Users\\nitesh.dudhe\\Downloads\\chromedriver_win32\\chromedriver.exe')
#web = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

web.set_page_load_timeout('10')
web.get('https://jira.onmobile.com/')
web.find_element_by_name('os_username').send_keys('nitesh.dudhe')
web.find_element_by_name('os_password').send_keys(pw)
web.find_element_by_name('login').send_keys(Keys.ENTER)
web.find_element_by_link_text('Create').click()

obj = Select(web.find_element_by_tag_name('input').find_elements_by_id('project-filed'))
obj.select_by_visible_text('OnMobile')


#web.find_element(By.ID, value='project-field').click().send_keys('onmobile').click()

#onmobile-(om)-165
#web.find_element_by_name('q').send_keys('Avengers Endgame')
#web.find_element_by_name('btnK').send_keys(Keys.ENTER)
#web.maximize_window()
#web.find_element_by_partial_link_text('en.wikipedia.org').cli
