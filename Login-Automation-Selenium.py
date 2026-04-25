from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

try:
    # step 1 - open site
    driver.get("https://www.saucedemo.com")
    print("open site successfully")

    # step 2 - enter username
    driver.find_element(By.ID,"User-name").send_keys("standard_user")
    print("Enter Username")

    # step 3 - enter password
    driver.find_element(By.ID,"Password").send_keys("Secret_sauce")
    print("Enter Password")

    # step 4 - Login button click
    driver.find_element(By.CSS_SELECTOR,"login-button").click()
    print("Login button click")

    # step 5 - success message
    wait=WebDriverWait(driver,10)
    message=wait.until(EC.presence_of_element_located((By.CLASS_NAME,"flash")))

    # step 6 - message print
    print("Message:",message.text)

    # step 7 - take screenshot
    driver.save_screenshot("login_success.png")
    print("Screenshot ")

except Exception as e:
    driver.save_screenshot("error.png")
    print("Error:",e)
finally:
    driver.quit()
    print("Browser Quit")



















