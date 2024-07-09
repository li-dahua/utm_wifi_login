from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
import time
import schedule

login_link="http://1.1.1.5/"
utmid = "" # username
password = "" # password

browser_type = "chrome" # edge or firefox

if browser_type == "edge" :
    driver = "driver/msedgedriver.exe"

elif browser_type =='firefox' : 
    driver = "/snap/bin/firefox.geckodriver"    
    
elif browser_type == "chrome" :
    driver = "driver/chromedriver.exe"

id_utmid = "une"
id_password = "pass"
id_submit = "btlogin"
def login():
    if browser_type == "edge" :
        browser =  webdriver.Edge(service=EdgeService(driver))
    elif browser_type =='firefox' : 
        browser =  webdriver.Firefox(service=FirefoxService(driver))
    elif browser_type =='chrome' : 
        browser =  webdriver.Chrome(service=ChromeService(driver))

    browser.get((login_link))	

    try:
        browser.find_element(by=By.NAME, value=id_utmid).send_keys(utmid)		
        browser.find_element(by=By.NAME, value=id_password).send_keys(password)
        browser.execute_script("arguments[0].click();", browser.find_element(By.ID,"tnc"))
        browser.find_element(by=By.NAME, value=id_submit).click()
        
        print("Login Success")
        time.sleep(3)
        browser.quit()

    except Exception:
        print("Error")
        time.sleep(3)
        browser.quit()
     
login()