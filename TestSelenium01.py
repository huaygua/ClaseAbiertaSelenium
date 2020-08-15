from selenium import webdriver
import unittest
import time

tc = unittest.TestCase('__init__')
chromedriver = "/home/monicahuaygua/ProyectoAutomations/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get('http://automationpractice.com/index.php')
driver.find_element_by_id('search_query_top').send_keys('hola')
driver.find_element_by_name('submit_search').click()
driver.find_element_by_xpath('//*[@id="center_column"]/p')
time.sleep(5)
tc.assertEqual('No results were found for your search "hola"',driver.find_element_by_xpath('//*[@id="center_column"]/p').text)

driver.close()
driver.quit()
