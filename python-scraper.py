import os
from pathlib import Path
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# register the selenium binaries path in 'bin' folder
path_geckodriver = os.path.join(os.getcwd(), 'bin', 'geckodriver.exe')
path_chromedriver = os.path.join(os.getcwd(), 'bin', 'chromedriver.exe')

# save path to "Downloads" folder
path_downloads = os.path.join(Path.home(), "Downloads")

# instantiate selenium driver object
# driver = webdriver.Firefox()
driver = webdriver.Chrome(path_chromedriver)

# visit website
driver.get('https://www.data.gov/')
time.sleep(5)

# search terms
elem_search_box = driver.find_element_by_id('search-header')
elem_search_box.send_keys('education')
elem_search_box.send_keys(Keys.RETURN)
time.sleep(5)

# close browser
driver.close()

# quit selenium
driver.quit()
