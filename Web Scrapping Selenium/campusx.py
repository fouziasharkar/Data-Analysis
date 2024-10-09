#install selenium
#Automate Chrome Driver(url:chrome driver -> older version from current chrome version -> download zip file)


# open google.com
#search campusx
#learnwith.campusx.in
#dsmp course page

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Driver path -> Make sure to replace backward slashes with forward slashes
s = Service("C:/Users/hp/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")

# Open a Chrome window automatically
driver = webdriver.Chrome(service=s)

# Open Google
driver.get('http://google.com')

# Wait until the search input box is present (maximum wait time is 10 seconds)

#WebDriverWait is a Selenium class that allows you to wait for a certain
#condition to occur before proceeding with the code.

user_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="APjFqb"]'))
)

# Send search query 'Campusx'
user_input.send_keys('Campusx')
user_input.send_keys(Keys.RETURN)  # Simulate hitting ENTER to start search

# Wait for search results to load (maximum wait time is 10 seconds)
search_results = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="rso"]'))
)

# Wait for the link to be clickable and then click it
link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a'))
)
link.click()

# Keep the browser window open indefinitely until user input
input()

# Close the driver
driver.quit()




