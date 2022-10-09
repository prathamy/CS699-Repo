#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def Convert(string):
    li = list(string.split("\n"))
    return li

PATH = "/home/prathamy/Documents/Documents/ACADS/SEM1/SWL/Project/chromedriver_linux64/chromedriver"
driver1 = webdriver.Chrome(PATH)

loc1="DEL-Delhi"
loc2="BOM-Mumbai"
date1="2022-12-10"

site1 = "https://paytm.com/flights/flightSearch/"+loc1+"/"+loc2+"/1/0/0/E/"+date1

driver1.get(site1)

time.sleep(5)

prices1 = driver1.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[3]/div")

print(Convert(prices1.text))

driver1.quit()