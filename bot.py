from selenium import webdriver 
import time 
from selenium.webdriver.common.keys import Keys      #Used to press any keys
from selenium.webdriver.common.action_chains import ActionChains #Used to controll states



driver = webdriver.Chrome("C:\chromedriver.exe")


#CDCASSESSMENTS
url = "https://cdcassessments.siet.ac.in/login"
driver.get(url)

action = ActionChains(driver)





time.sleep(3)
# input_bar = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
input_bar = driver.find_element_by_xpath('//*[@id="email"]')

input_bar.send_keys("dineshi2021@srishakthi.ac.in")

next_button = driver.find_element_by_xpath('//*[@id="lgnNext0"]')

next_button.click()
time.sleep(10)
password_input = driver.find_element_by_xpath('//*[@id="password"]')

password_input.send_keys("DINESH VDMI 3")
enter_button = driver.find_element_by_xpath('//*[@id="lgnLogin0"]/div')

enter_button.click()
time.sleep(10)
menu_bar = driver.find_element_by_xpath('/html/body/app-root/div/app-top-header/div/div[1]/div[1]/div/div')

action.move_to_element(menu_bar)
action.perform()
# input_bar.send_keys(Keys.ENTER)



#APIFY
'''
APIFY_url = 'https://apify.com/?utm_source=app'
driver.get(APIFY_url)


# data_list = driver.find_elements_by_class_name("Text__Paragraph-sc-1f839r4-6 kBAtMX")
data = driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div/div/div[1]/p')

print(data.text)


# for data in data_list:
#     print(data.text)'''

