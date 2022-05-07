login_link="http://1.1.1.2/"
utmid = "" # username
password = "" # password

browser_type = "edge" # edge or firefox

if browser_type == "edge" :
    driver = "driver/msedgedriver.exe"

elif browser_type =='firefox' : 
    driver = "driver/geckodriver.exe"    
