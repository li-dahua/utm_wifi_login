from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


login_link="http://1.1.1.2/"
utmid = "" # username
password = "" # password

id_utmid = "une"
id_password ="pass"
id_submit="btlogin"

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install() , service_log_path="O:/log/log")
# browser = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install() , service_log_path="O:/log/log")
browser.get((login_link))	

try:
	username_name = browser.find_element_by_name(id_utmid)
	username_name.send_keys(utmid)		
	password_name  = browser.find_element_by_name(id_password)
	password_name.send_keys(password)
	browser.execute_script("arguments[0].click();", browser.find_element(By.ID,"tnc"))
	signInButton = browser.find_element_by_name(id_submit)
	signInButton.click()
	
	print("Login Success")
	time.sleep(3)
	browser.quit()

except Exception:
	print("Error")
