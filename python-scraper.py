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

# advanced tips on how to interact 
flag_advanced_tips = False
if flag_advanced_tips:
  
  # maximize window (because some elements must be visible)
  driver.maximize_window()
  
  # find element by class name, loop through multiple elements
  elem_login_option = driver.find_elements_by_class_name('login-option')
  for each_elem in elem_login_option:
    if each_elem.text == "Click here to login":
      each_elem.click()
      time.sleep(5)
      break
  
  # find element by link_text
  elem_text_link = driver.find_element_by_link_text("Click Me")
  elem_text_link.click()
  time.sleep(5)
  
  # find element by html tag
  elem_button = driver.find_elements_by_tag_name('button')
  for each_elem in elem_button:
    if each_elem.text == "Go for it!":
      each_elem.click()
      time.sleep(5)
      break
  
  # find element by CSS
  elem_css = driver.find_element_by_css('#random-css-here')
  elem_css.click()
  time.sleep(5)
  
  # click on attributes and displayed element, 
  # error message whether element is interactable or clickable
  # avoid hidden elements
  elem_displayed = find_elements_by_class_name('blah-link')
  for each_elem in elem_displayed:
    if each_elem.get_attribute('title')=='this is the winner':
      if each_elem.is_displayed():
        each_elem.click()
        time.sleep(5)
        break
      
  # select amongst multiple browser windows
  selenium_window_before = driver.window_handles[0]
  selenium_window_after = driver.window_handles[1]
  driver.switch_to.window(selenium_window_after)
  time.sleep(5)

# close browser
driver.close()

# quit selenium
driver.quit()
