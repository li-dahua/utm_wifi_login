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

# browser = webdriver.Firefox(executable_path=GeckoDriverManager().install() , service_log_path="O:/log/log")
# browser = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install() , service_log_path="O:/log/log")
# browser = webdriver.Firefox(executable_path=r'X:\geckodriver-v0.29.1-win64\geckodriver.exe' , service_log_path="O:/log/log")
browser.get((login_link))	

try:
	browser.find_element_by_name(id_utmid).send_keys(utmid)		
	browser.find_element_by_name(id_password).send_keys(password)
	browser.execute_script("arguments[0].click();", browser.find_element(By.ID,"tnc"))
	browser.find_element_by_name(id_submit).click()
	
	print("Login Success")
	time.sleep(3)
	browser.quit()

except Exception:
	print("Error")
