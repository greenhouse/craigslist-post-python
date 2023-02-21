#!/usr/bin/env python

import sys, argparse, string, ctypes, os, re
#import urllib, urllib2, cookielib, httplib
#import cookielib, time, base64
import time

from os import path
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
#from selenium.webdriver.support.ui import Select

#from pyvirtualdisplay import Display
#import spintax

#------------------------------------------------------------#
WAIT_TIME = 1 #sec
str_i_0 = "2br/2ba - East Boca Condo for Rent"
str_i_1 = "Boca Raton"
str_i_2 = "33487"
str_i_3 = """
Condo for rent in Banyan Park Boca Raton, 33487
$2,200/month; 1018sqft (2 bed / 2 bath)

Ideal location in east Boca Raton.
Close to beaches, dining, collages and transportation.

Second floor unit with assigned parking.
Spacious rooms with tile and engineered wood flooring.
Washer and dryer in unit.
Newly renovated kitchen w/ new appliances.
Screened in balcony, overlooking private garden.

Tenant responsible for electric and cable/internet.
First, last and security required to move in.
Credit score 700+ and background check screening required.

Agents welcome!
"""
str_i_4 = "2200"
str_i_5 = "1018"
str_i_6 = "Wed, 1 Mar 2023"
str_i_7 = "temp37373737@gmail.com"
str_i_8 = "160 nw 70th Street"
str_i_9 = "70th Street and 2nd Ave"
str_i_10 = "Boca Raton"
#------------------------------------------------------------#

print('\n\nInitializing client...')
CLIENT = webdriver.Firefox()

print('Navigating to craigslist')
CLIENT.get("https://miami.craigslist.org/search/pbc/apa#search=1~list~0~0")

print('clicking "post"')
CLIENT.find_element(By.CSS_SELECTOR, ".cl-goto-post").click()

print(f'waiting... {WAIT_TIME}')
time.sleep(WAIT_TIME)

print('searching for palm beach co "3"')
elements = CLIENT.find_elements(By.NAME, "n")
for i,e in enumerate(elements):
    v = elements[i].get_attribute("value")
    print(f"... found elements[i] value = {v}")
    if v == "3":
        print(f"clicking {v}")
        elements[i].click()
        break
        
print(f'waiting... {WAIT_TIME}')
time.sleep(WAIT_TIME)

print('searching for housing offered "ho"')
elements = CLIENT.find_elements(By.NAME, "id")
for i,e in enumerate(elements):
    v = elements[i].get_attribute("value")
    print(f"... found elements[i] value = {v}")
    if v == "ho":
        print(f"clicking {v}")
        elements[i].click()
        break
        
print(f'waiting... {WAIT_TIME}')
time.sleep(WAIT_TIME)

print('searching for apartments "1"')
elements = CLIENT.find_elements(By.NAME, "id")
for i,e in enumerate(elements):
    v = elements[i].get_attribute("value")
    print(f'... found elements[i] value = {v}')
    if v == "1":
        print(f'clicking {v}')
        elements[i].click()
        break
        
print(f'waiting... {WAIT_TIME}')
time.sleep(WAIT_TIME)

print(f'filling in text field details...')
CLIENT.find_element(By.ID, "PostingTitle").send_keys(str_i_0)
CLIENT.find_element(By.ID, "geographic_area").send_keys(str_i_1)
CLIENT.find_element(By.ID, "postal_code").send_keys(str_i_2)
CLIENT.find_element(By.ID, "PostingBody").send_keys(str_i_3)
CLIENT.find_element(By.NAME, "price").send_keys(str_i_4)
CLIENT.find_element(By.NAME, "surface_area").clear() # delete default 0
CLIENT.find_element(By.NAME, "surface_area").send_keys(str_i_5)

print('searching through 9 ui-selectmenu-text')
sel_menu_els = CLIENT.find_elements(By.CSS_SELECTOR, ".ui-selectmenu-text")
for i,v in enumerate(sel_menu_els):
    sel_menu_els[i].click()
    elements = CLIENT.find_elements(By.CSS_SELECTOR, ".ui-menu-item")
    
    sel_menu_el_par = sel_menu_els[i].find_element(By.XPATH, "..")
    sel_menu_el_par_id = sel_menu_el_par.get_attribute("id")
    if sel_menu_el_par_id == 'ui-id-1-button':
        print('searching for rent per "month"')
        for i,e in enumerate(elements):
            text = elements[i].text
            print(f'... found elements[i] text = {text}')
            if text == "month":
                print(f'clicking {text}')
                elements[i].click()
                break
    if sel_menu_el_par_id == 'ui-id-2-button':
        pass
    if sel_menu_el_par_id == 'ui-id-3-button':
        print("searching for laundy 'w/d in unit'")
        for i,e in enumerate(elements):
            text = elements[i].text
            print(f'... found elements[i] text = {text}')
            if text == "w/d in unit":
                print(f'clicking {text}')
                elements[i].click()
                break
    if sel_menu_el_par_id == 'ui-id-4-button':
        print("searching for parking 'off-street parking'")
        for i,e in enumerate(elements):
            text = elements[i].text
            print(f'... found elements[i] text = {text}')
            if text == "off-street parking":
                print(f'clicking {text}')
                elements[i].click()
                break
    if sel_menu_el_par_id == 'ui-id-5-button':
        print("searching for bedrooms '2'")
        for i,e in enumerate(elements):
            text = elements[i].text
            print(f'... found elements[i] text = {text}')
            if text == "2":
                print(f'clicking {text}')
                elements[i].click()
                break
    if sel_menu_el_par_id == 'ui-id-6-button':
        print("searching for bathrooms '2'")
        for i,e in enumerate(elements):
            text = elements[i].text
            print(f'... found elements[i] text = {text}')
            if text == "2":
                print(f'clicking {text}')
                elements[i].click()
                break

print('selecting right side checkboxes...')
CLIENT.find_element(By.NAME, "no_smoking").click()
CLIENT.find_element(By.NAME, "airconditioning").click()
print('selecting right side checkboxes... DONE')

print('searching for available on date, march "1"')
CLIENT.find_element(By.CSS_SELECTOR, ".movein_date").click() # click datepicker
CLIENT.find_element(By.CSS_SELECTOR, ".ui-datepicker-next").click() # click next month
elements = CLIENT.find_elements(By.CSS_SELECTOR, ".ui-state-default")
for i,e in enumerate(elements): # loop to find 1st day of month
    text = elements[i].text
    print(f'... found elements[i] text = {text}')
    if text == "1": # month date
        print(f'clicking {text}')
        elements[i].click()
        break

CLIENT.find_element(By.NAME, "FromEMail").send_keys(str_i_7)
CLIENT.find_element(By.NAME, "show_address_ok").click() # check box
CLIENT.find_element(By.NAME, "xstreet0").send_keys(str_i_8)
CLIENT.find_element(By.NAME, "xstreet1").send_keys(str_i_9)
CLIENT.find_element(By.NAME, "city").send_keys(str_i_10)

print(f'waiting 3 before clicking "continue"')
time.sleep(3) #wait 1 before click 'continue'
print(f'clicking "continue"...')
CLIENT.find_element(By.NAME, "go").click()

print('_ DONE\n\n')

#ref: https://www.selenium.dev/selenium/docs/api/py/_modules/selenium/webdriver/common/by.html#By
#ref: https://github.com/SeleniumHQ/selenium/blob/a4995e2c096239b42c373f26498a6c9bb4f2b3e7/py/CHANGES
#ref: https://stackoverflow.com/a/72773269/2298002
"""Set of supported locator strategies."""
#ID = "id"
#XPATH = "xpath"
#LINK_TEXT = "link text"
#PARTIAL_LINK_TEXT = "partial link text"
#NAME = "name"
#TAG_NAME = "tag name"
#CLASS_NAME = "class name"
#CSS_SELECTOR = "css selector"



