from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# browser open
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# website open
driver.get("https://www.google.com")

# print title
print(driver.title)

# wait 3 second visit browser
import time
time.sleep(3)

# close browser
driver.quit()

