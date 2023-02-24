#!/usr/bin/env python

import sys, argparse, string, ctypes, os, re
#import urllib, urllib2, cookielib, httplib
#import cookielib, time, base64
import time
from datetime import datetime

#from os import path
#from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
#from selenium.webdriver.support.ui import Select

#from pyvirtualdisplay import Display
#import spintax

#------------------------------------------------------------#
#   GLOBALS                                                  #
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
12 month lease minimum.

HOA requires $150 application fee
- includes background check & credit check (700+ required)

Agents welcome!
"""
str_i_4 = "2200"
str_i_5 = "1018"
str_i_6 = "15" # march 15th
str_i_7 = "temp37373737@gmail.com"
str_i_8 = "160 nw 70th Street"
str_i_9 = "70th Street and 2nd Ave"
str_i_10 = "Boca Raton"
#------------------------------------------------------------#
img_path_folder = "_env/boca_ad"
img_path_0 = "0__image0.jpg"
img_path_1 = "0_00E0E_Mx7XY9fIg8z_0CI0pg_600x450.jpg"
img_path_2 = "00d0d_6cU9WQsRd9Mz_0t20CI_600x450.jpg"
img_path_3 = "00D0D_e6xjBgy8IVGz_0CI0t2_600x450.jpg"
img_path_4 = "00L0L_8mOOAj2CaLoz_0t20CI_600x450.jpg"
img_path_5 = "00U0U_9akydFNSLPNz_0t20CI_600x450.jpg"
img_path_6 = "00v0v_lT7n4oWvmPEz_0sP0CI_600x450.jpg"
img_path_7 = "00505_3HncxQXU7VRz_0t20CI_600x450.jpg"
img_path_8 = "00505_4WlwB71yzMwz_0t20CI_600x450.jpg"
img_path_9 = "00606_eOO5SR0Xh56z_0t20CI_600x450.jpg"
img_path_10 = "01616_MVrjnqJqQqz_0t20CI_600x450.jpg"
#------------------------------------------------------------#
#------------------------------------------------------------#
GO_TIME_START = datetime.now().strftime("%H:%M:%S.%f")[0:-4]
print(f'\n\nGO_TIME_START: {GO_TIME_START}')

iPost_cnt = 4
x = 1
while x <= iPost_cnt:
    print(f'\n\n creating CL post # {x}')
    
    cl_time_start = datetime.now().strftime("%H:%M:%S.%f")[0:-4]
    print(f'\n\nInitializing client... start: {cl_time_start}')
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
        
        #ref: https://stackoverflow.com/a/18079918/2298002
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

    print('searching for available on date, march "15"')
    CLIENT.find_element(By.CSS_SELECTOR, ".movein_date").click() # click datepicker
    CLIENT.find_element(By.CSS_SELECTOR, ".ui-datepicker-next").click() # click next month once (to march)
    elements = CLIENT.find_elements(By.CSS_SELECTOR, ".ui-state-default")
    for i,e in enumerate(elements): # loop to find 1st day of month
        text = elements[i].text
        print(f'... found elements[i] text = {text}')
        if text == str_i_6: # month date
            print(f'clicking {text}')
            elements[i].click()
            break

    print('setting email & street address')
    CLIENT.find_element(By.NAME, "FromEMail").send_keys(str_i_7)
    CLIENT.find_element(By.NAME, "show_address_ok").click() # check box
    CLIENT.find_element(By.NAME, "xstreet0").send_keys(str_i_8)
    CLIENT.find_element(By.NAME, "xstreet1").send_keys(str_i_9)
    CLIENT.find_element(By.NAME, "city").send_keys(str_i_10)

    print(f'waiting... {WAIT_TIME} before clicking "continue"')
    time.sleep(WAIT_TIME)
    print(f'clicking "continue"...')
    CLIENT.find_element(By.NAME, "go").click()

    print(f'waiting {WAIT_TIME} before clicking "continue" from map screen')
    time.sleep(WAIT_TIME)
    print(f'clicking "continue"... from map screen')
    CLIENT.find_element(By.CSS_SELECTOR, ".continue").click()

    c_time_start = datetime.now().strftime("%H:%M:%S.%f")
    print(f'selecting images... -> {c_time_start[0:-4]}')
    #ref: https://stackoverflow.com/a/70547723/2298002
    #ref: https://stackoverflow.com/a/10472542/2298002
    #ref: https://stackoverflow.com/a/74014300/2298002
        #choose_image=driver.find_element(By.ID, 'id')
        #choose_image.send_keys(os.path.join(os.getcwd(), 'image.jpg'))
        #choose_img.send_keys(os.path.join(os.getcwd(), 'image.jpg'))
    input_el_par = CLIENT.find_element(By.CSS_SELECTOR, ".moxie-shim")
    input_el_child = input_el_par.find_element(By.TAG_NAME, "input")
    input_el_child.send_keys(os.getcwd() + '/' + img_path_folder + '/' + img_path_0)
    input_el_child.send_keys(os.getcwd() + '/' + img_path_folder + '/' + img_path_1)
    input_el_child.send_keys(os.getcwd() + '/' + img_path_folder + '/' + img_path_2)
    input_el_child.send_keys(os.getcwd() + '/' + img_path_folder + '/' + img_path_3)
    input_el_child.send_keys(os.getcwd() + '/' + img_path_folder + '/' + img_path_4)
    input_el_child.send_keys(os.getcwd() + '/' + img_path_folder + '/' + img_path_5)
    input_el_child.send_keys(os.getcwd() + '/' + img_path_folder + '/' + img_path_6)
    input_el_child.send_keys(os.getcwd() + '/' + img_path_folder + '/' + img_path_7)
    input_el_child.send_keys(os.getcwd() + '/' + img_path_folder + '/' + img_path_8)
    input_el_child.send_keys(os.getcwd() + '/' + img_path_folder + '/' + img_path_9)
    input_el_child.send_keys(os.getcwd() + '/' + img_path_folder + '/' + img_path_10)
    figure_el_par = CLIENT.find_element(By.ID, "uploader")
    figure_el_child = figure_el_par.find_elements(By.TAG_NAME, "figure")
    print(f'len(figure_el_child) = {len(figure_el_child)}')
    print('... uploading images ...')
    while len(figure_el_child) > 0:
        figure_el_child = figure_el_par.find_elements(By.TAG_NAME, "figure")
        #print(f'len(figure_el_child) = {len(figure_el_child)}')
    print('... uploading images ... DONE')
    print(f'len(figure_el_child) = {len(figure_el_child)}')
    c_time_end = datetime.now().strftime("%H:%M:%S.%f")
    print(f'selecting images... DONE -> \n   start: {c_time_start[0:-4]}\n   end:   {c_time_end[0:-4]}')

    print(f'waiting {WAIT_TIME} before clicking "done with images"...')
    time.sleep(WAIT_TIME)
    print(f'clicking "done with images"... ')
    CLIENT.find_element(By.CSS_SELECTOR, ".done").click()

    print(f'waiting {WAIT_TIME} before clicking "publish"...')
    time.sleep(WAIT_TIME)
    print(f'clicking "publish"... ')
    CLIENT.find_element(By.NAME, "go").click()

    print(f'\n\nDONE creating post\n check email verifation: {str_i_7}\n')

    cl_time_end = datetime.now().strftime("%H:%M:%S.%f")[0:-4]
    print(f'start: {cl_time_start}')
    print(f'end:   {cl_time_end}')
    
    print(f'\n\n creating CL post # {x} _ DONE _')
    x += 1
    
GO_TIME_END = datetime.now().strftime("%H:%M:%S.%f")[0:-4]
print(f'\n\nGO_TIME_START: {GO_TIME_START}')
print(f'GO_TIME_END:   {GO_TIME_END}')


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



