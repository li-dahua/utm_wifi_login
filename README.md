## in main.py :
1. edit utmid and password (line 8 & 9 )
2. change sevive_log_path (line 15/16/17)
3.                 if (browser == 'Firefox'):
                        uncomment line 15
                        comment line 16
                        comment line 17
                    elif (browser='Edge'):
                        uncomment line 16
                        comment line 15
                        comment line 17
                    elif (downloaded geckodriver https://github.com/mozilla/geckodriver ):
                        uncomment line 17, set the geckodriver path
                        comment line 15
                        comment line 16
                    else:
                        develop the code urself

## install dependencies
          pip install -r  requirements.txt          
         
## build  executable file
          pyinstaller --onefile main.py

## License
[![License: MIT](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://github.com/chunkeat99/utm_wifi_login/blob/main/LICENSE)


[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fchunkeat99%2Futm_wifi_login&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)]
