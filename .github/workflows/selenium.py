print('selenium file started')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import sys
import re

sys.dont_write_bytecode = True

sys.path.append('./code/global_code/')
import global_function as af

chromedriver = './data/#global_rf/selenium/chromedriver.exe'

# options = webdriver.ChromeOptions()
# out_path = './data/asia/japan/raw/month/'
# prefs = {'download.default_directory': out_path}
# options.add_experimental_option('prefs', prefs)


# file_name = af.search_file(out_path)

# name = re.compile(r'month/(?P<name>.*?)_', re.S) 
# date = [name.findall(f)[0] for f in file_name]
# date = max(date)
# date = '%s年%s月' % (date[:4], int(date[-2:]))
# print(date)


# wd = webdriver.Chrome(chromedriver, chrome_options=options)  
# wd.get('https://occtonet3.occto.or.jp/public/dfw/RP11/OCCTO/SD/LOGIN_login#')  

# handles = wd.window_handles
# wd.switch_to.window(handles[1])
# wd.close()  
# wd.switch_to.window(handles[0])  
# wd.implicitly_wait(60)
# wd.find_element(By.ID, 'menu1-6').click()
# wd.find_element(By.ID, 'menu1-6-3-1').click()
# handles = wd.window_handles
# wd.switch_to.window(handles[1])  

# select = Select(wd.find_element(By.ID, 'ktgr'))
# select.select_by_value('7')  
# wd.find_element(By.ID, 'searchBtn').click()


# test = wd.find_element(By.ID, 'table3_rows_0__infNm')
# if date in test.text:
#     print('not update yet')
# else:
#     wd.find_element(By.ID, 'table3_rows_0__pdfCsvBtn').click()
#     time.sleep(10)
#     confirm_text = 'ui-button-text'
#     wd.find_elements(By.CLASS_NAME, confirm_text)[2].click()
#     print('downloading...')
#     time.sleep(30)
# # wd.quit()
