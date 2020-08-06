from selenium import webdriver
import unittest
import time

tc = unittest.TestCase('__init__')
chromedriver = "/home/monicahuaygua/ProyectoAutomations/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get('http://automationpractice.com/index.php')
search_box = driver.find_element_by_id("search_query_top")
search_box.send_keys("hola mundo")
search_box_button = driver.find_element_by_tag_name("submit_search")
search_box_button.click()

time.sleep(6)
#tc.assertEqual('No results were found for your search "hola"', driver.find_element_by_xpath('//*[@id="center_column"]/p')).text

driver.close()
driver.quit()

