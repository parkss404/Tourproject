from re import T
from turtle import title
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import openpyxl
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('tour2.xlsx')

browser = webdriver.Chrome("./chromedriver.exe")
browser.get('https://fly.interpark.com/booking/mainFlights.do?tripType=OW&sdate0=20230110&sdate1=&dep0=SEL&arr0=KIX&dep1=KIX&arr1=SEL&adt=1&chd=0&inf=0&val=5D&comp=Y&via=#list') #get()이렇게 해야됨
html = browser.page_source
soup = BeautifulSoup(html,'lxml')
sleep(4)
#print(browser.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div/div[1]/div[3]/div[2]/div[2]/ul/li[1]/div[7]/span[2]/strong').text)
#print(browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[6]/div/div[3]/div[2]/div[1]/div').text)
#print(browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[6]/div/div[3]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/b/i').text)
c = 0
while(c<22):
    key = df.loc[c,'코드']
    browser = webdriver.Chrome("./chromedriver.exe")
    browser.get(f'https://fly.interpark.com/booking/mainFlights.do?tripType=OW&sdate0=20230110&sdate1=&dep0=SEL&arr0={key}&dep1={key}&arr1=SEL&adt=1&chd=0&inf=0&val=5D&comp=Y&via=#list')
    html = browser.page_source
    num = 0
    sum = 0
    while(num < 5):
            #print(browser.find_elements_by_tag_name('strong')[num].text)
            print(browser.find_elements_by_class_name('charge')[num].text.replace("원~","",1).replace(",",""))
            sum += int(browser.find_elements_by_class_name('charge')[num].text.replace("원~","",1).replace(",",""))
            num += 1
        
    mean = sum / 5
    print(mean)
    df.loc[c,'가격'] = mean 
    c += 1
    print(df)
    browser.close()
    df.to_csv('/Users/parksungjun/Library/Mobile Documents/com~apple~CloudDocs/프로젝트/프로젝트 폴라/crawling/tour2.xlsx')
    sleep(2)
    
