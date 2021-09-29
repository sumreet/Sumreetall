
#open new URL
from selenium import webdriver
driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
driver.get('https://gmail.com')
driver.find_element_by_name("identifier").send_keys('sumreet.kaur@crochetech.com')
driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/span").click()
driver.implicitly_wait(4)
driver.find_element_by_name("password").send_keys("Reet789@....")
driver.find_element_by_xpath("//*[@id='passwordNext']/div/button/span").click()



