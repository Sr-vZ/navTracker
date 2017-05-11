from selenium import webdriver
from tqdm import tqdm
import os

import csv

url="http://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?mf=22&frmdt=01-Apr-2017&todt=30-Apr-2017"

driver = webdriver.PhantomJS(executable_path='C:/Users/608619925/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe') # or add to your PATH
#driver.set_window_size(1024, 768) # optional
driver.get(url)
preTextEl = driver.find_element_by_css_selector("pre")
data=preTextEl.text.split(";")
#print (preTextEl.text)
#driver.save_screenshot('screen.png') # save a screenshot to disk
#sbtn = driver.find_element_by_css_selector('button.gbqfba')
#sbtn.click()
#csvFile = open('example.csv', 'w', newline='')
with open('some.csv', 'w',newline="\n",encoding="utf-8") as f:
    writer = csv.writer(f,delimiter=";")
    writer.writerows([data])
    for r in tqdm(range(os.path.getsize("some.csv"))):
        pass
    
    
#writer.close
driver.close
#print (len(data))
