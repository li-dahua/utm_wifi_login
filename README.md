Install PYTHON
## install dependencies
          pip3 install -r  requirements.txt          
         
How to use the script.
Open Main.py
1.          Key in your username and password.
  
utmid = "my_name" # username

password = "my_password" # password

2.          Choose the browser you want.
browser_type = "chrome" # edge or firefox

3.          Change the time you want to login.

Normally you will be auto-logged out at 2 am every day.

schedule.every().day.at("02:10").do(login) #time for login
The time scale is at 24-hour format. Here meaning 02:10 am will auto-login.

## If not working after the run, go download the corresponding version of your browser webdriver.
4.          python3 main.py

   imi.py is for direct login.


## build  executable file
          pyinstaller --onefile main.py
          
## License
[![License: MIT](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://github.com/chunkeat99/utm_wifi_login/blob/main/LICENSE)

