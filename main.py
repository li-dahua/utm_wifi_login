from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time
import datetime
import schedule
from selenium.webdriver.firefox.options import Options

login_link="https://wifikl.utm.my/"
utmid = "" # username
password = "" # password

browser_type = "chrome" # edge or firefox

if browser_type == "edge" :
    driver = "driver/msedgedriver.exe"

elif browser_type =='firefox' : 
    driver = "/snap/bin/firefox.geckodriver"    


elif browser_type == "chrome" :
    driver = "/snap/bin/chromium.chromedriver"

id_utmid = "username"
id_password = "password"
id_submit = "btn-login"



def login():
    browser = None

    try:
        options = Options()
        # options.headless = True  # Uncomment for headless mode
        if browser_type == "edge":
            browser = webdriver.Edge(service=EdgeService(driver))
        elif browser_type == 'firefox':
            browser = webdriver.Firefox(service=FirefoxService(driver), options=options)
        
        elif browser_type == 'chrome':
            browser = webdriver.Chrome(service=ChromeService(driver))


        browser.get(login_link)

        # Wait for the username field to be present
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.NAME, id_utmid))).send_keys(utmid)
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.NAME, id_password))).send_keys(password)

        # Wait for the login button to be clickable
        login_button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, id_submit)))
        browser.execute_script("arguments[0].scrollIntoView();", login_button)
        login_button.click()

        print("Login Success")
        time.sleep(3)

    except Exception as e:
        print(f"Error: {e}")
        if browser:
            print("Current URL:", browser.current_url)
            print("Page Source:", browser.page_source)  # For debugging

    finally:
        if browser:
            browser.quit()

# Uncomment to schedule
#login()
schedule.every().day.at("02:10").do(login) 
while True:
    schedule.run_pending()
    time.sleep(60)
    schedule.run_pending()
    time.sleep(60)


