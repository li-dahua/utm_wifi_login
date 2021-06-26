## in main.py :
1. edit utmid and password (line 11 & 12 )
2. change sevive_log_path (line 16/17)
3.                 if (browser == 'Firefox'):
                        uncomment line 16
                        comment line 17
                    elif (browser='Edge'):
                        uncomment line 17
                        comment line 16
                    else:
                        develop the code urself

## install dependencies
          pip install -r  requirments.txt          
         
## build  executable file
          pyinstaller --onefile main.py

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/chunkeat99/utm_wifi_login/blob/main/LICENSE)
