from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user = ""
pwd = ""
driver = webdriver.Firefox()
# navigate to the application home page
driver.get("http://www.google.com")

# get the search textbox
search_field = driver.find_element_by_id("lst-ib")
search_field.clear()
#driver.close()