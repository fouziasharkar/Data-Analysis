#infinite scrolling page

#goal is to load a item page till bottom
#copy the html code for further web scrapping

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
driver.get('https://www.ajio.com/men-backpacks/c/830201001')

# Get the height of the page
#page_height = driver.execute_script("return document.body.scrollHeight;")
#print(f"The height of the page is: {page_height}px")

# Initialize variables to track page height
scroll_pause_time = 2  # Time to pause to allow page to load
old_height = driver.execute_script("return document.body.scrollHeight")

counter = 1
while True:
    # Scroll down to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for the page to load
    time.sleep(scroll_pause_time)

    # Get new page height after scroll
    new_height = driver.execute_script("return document.body.scrollHeight")

    print(counter)
    counter += 1
    print(old_height)
    print(new_height)

    # Check if the page height has increased (i.e., new content has been loaded)
    if new_height == old_height:
        # If the height hasn't changed, we reached the bottom
        break

    # Update old_height to new_height for the next iteration
    old_height = new_height


#to copy the html code of the entire page
html = driver.page_source

#creating html file
with open('ajio.html','w',encoding='utf-8') as f:
    f.write(html)




# Keep the browser window open indefinitely until user input
input()

















