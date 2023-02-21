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
from selenium.webdriver.support.ui import Select

#from pyvirtualdisplay import Display
#import spintax

WAIT_TIME = 1 #sec

print('initializing client...')
CLIENT        = webdriver.Firefox()
print("Navigating to craigslist")
CLIENT.get("https://miami.craigslist.org/search/pbc/apa#search=1~list~0~0")
element = CLIENT.find_element("css selector", ".cl-goto-post").click()

print(f"waiting... {WAIT_TIME}")
time.sleep(WAIT_TIME)

print("searching for palm beach co '3'")
elements = CLIENT.find_elements(By.NAME, "n")
for i,e in enumerate(elements):
    v = elements[i].get_attribute("value")
    print(f"... found elements[i] value = {v}")
    if v == "3":
        print(f"clicking {v}")
        elements[i].click()
        break
        
print(f"waiting... {WAIT_TIME}")
time.sleep(WAIT_TIME)

print("searching for housing offered 'ho'")
elements = CLIENT.find_elements(By.NAME, "id")
for i,e in enumerate(elements):
    v = elements[i].get_attribute("value")
    print(f"... found elements[i] value = {v}")
    if v == "ho":
        print(f"clicking {v}")
        elements[i].click()
        break
        
print(f"waiting... {WAIT_TIME}")
time.sleep(WAIT_TIME)

print("searching for apartments '1'")
elements = CLIENT.find_elements(By.NAME, "id")
for i,e in enumerate(elements):
    v = elements[i].get_attribute("value")
    print(f"... found elements[i] value = {v}")
    if v == "1":
        print(f"clicking {v}")
        elements[i].click()
        break
        
print(f"waiting... {WAIT_TIME}")
time.sleep(WAIT_TIME)

print(f"filling in text field details...")
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

CLIENT.find_element(By.ID, "PostingTitle").send_keys(str_i_0)
CLIENT.find_element(By.ID, "geographic_area").send_keys(str_i_1)
CLIENT.find_element(By.ID, "postal_code").send_keys(str_i_2)
CLIENT.find_element(By.ID, "PostingBody").send_keys(str_i_3)
CLIENT.find_element(By.NAME, "price").send_keys(str_i_4)
CLIENT.find_element(By.NAME, "surface_area").clear() # delete default 0
CLIENT.find_element(By.NAME, "surface_area").send_keys(str_i_5)

#print(f"waiting... 1 ... for select options to load completely...")
#time.sleep(1)

#CLIENT.find_element(By.NAME, "rent_period").click()

    ## alternate select element picker ##
    #ref: https://stackoverflow.com/a/28613320/2298002
    #select = Select(CLIENT.find_element(By.ID, 'ui-id-1'))
    #select = Select(CLIENT.find_element(By.NAME, 'rent_period'))
    #select = Select(CLIENT.find_element(By.CSS_SELECTOR, ".ui-selectmenu-text"))
    # select by visible text
    #select.select_by_visible_text('month')
    #select.select(By.visible_text, 'month')
    # select by value
    #select.select_by_value('3')
print("searching througha ll ui-selectmenu-text")
sel_menu_els = CLIENT.find_elements(By.CSS_SELECTOR, ".ui-selectmenu-text")
for i,v in enumerate(sel_menu_els):
    sel_menu_els[i].click()
    elements = CLIENT.find_elements(By.CSS_SELECTOR, ".ui-menu-item")
    
    sel_menu_el_par = sel_menu_els[i].find_element(By.XPATH, "..")
    sel_menu_el_par_id = sel_menu_el_par.get_attribute("id")
    if sel_menu_el_par_id == 'ui-id-1-button':
        print("searching for rent per 'month'")
        for i,e in enumerate(elements):
            text = elements[i].text
            print(f"... found elements[i] text = {text}")
            if text == "month":
                print(f"clicking {text}")
                elements[i].click()
                break
    if sel_menu_el_par_id == 'ui-id-2-button':
        pass
    if sel_menu_el_par_id == 'ui-id-3-button':
        print("searching for laundy 'w/d in unit'")
        for i,e in enumerate(elements):
            text = elements[i].text
            print(f"... found elements[i] text = {text}")
            if text == "w/d in unit":
                print(f"clicking {text}")
                elements[i].click()
                break
    if sel_menu_el_par_id == 'ui-id-4-button':
        print("searching for parking 'off-street parking'")
        for i,e in enumerate(elements):
            text = elements[i].text
            print(f"... found elements[i] text = {text}")
            if text == "off-street parking":
                print(f"clicking {text}")
                elements[i].click()
                break
    if sel_menu_el_par_id == 'ui-id-5-button':
        print("searching for bedrooms '2'")
        for i,e in enumerate(elements):
            text = elements[i].text
            print(f"... found elements[i] text = {text}")
            if text == "2":
                print(f"clicking {text}")
                elements[i].click()
                break
    if sel_menu_el_par_id == 'ui-id-6-button':
        print("searching for bathrooms '2'")
        for i,e in enumerate(elements):
            text = elements[i].text
            print(f"... found elements[i] text = {text}")
            if text == "2":
                print(f"clicking {text}")
                elements[i].click()
                break
        
CLIENT.find_element(By.NAME, "no_smoking").click()
CLIENT.find_element(By.NAME, "airconditioning").click()

    ## alternate datepicker solution ##
    #ref: https://stackoverflow.com/a/67611704/2298002
    # click on the date that matches the xpath with the aria-label
    #driver.find_element_by_xpath(
    #    "//button[@aria-label='{}']".format(start_date_calendar)).click()
    #CLIENT.find_element(By.XPATH, "//button[@aria-label='{}']".format(str_i_6)).click()`
print("searching for available on date, march '1'")
CLIENT.find_element(By.CSS_SELECTOR, ".movein_date").click() # click datepicker
CLIENT.find_element(By.CSS_SELECTOR, ".ui-datepicker-next").click() # click next month
elements = CLIENT.find_elements(By.CSS_SELECTOR, ".ui-state-default")
for i,e in enumerate(elements): # loop to find 1st day of month
    text = elements[i].text
    print(f"... found elements[i] text = {text}")
    if text == "1":
        print(f"clicking {text}")
        elements[i].click()
        break

CLIENT.find_element(By.NAME, "FromEMail").send_keys(str_i_7)
CLIENT.find_element(By.NAME, "show_address_ok").click() # check box
CLIENT.find_element(By.NAME, "xstreet0").send_keys(str_i_8)
CLIENT.find_element(By.NAME, "xstreet1").send_keys(str_i_9)
CLIENT.find_element(By.NAME, "city").send_keys(str_i_10)

print(f"waiting 1 before clicking 'continue'")
time.sleep(10) #wait 1 before click 'continue'
print(f"clicking 'continue'...")
#CLIENT.find_element(By.NAME, "go").click()

#CLIENT.
#element = CLIENT.find_element("name", "n")
#if element.value == "1":
#    CLIENT.find_element("name", "n").click()
print('_ DONE')

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


#ref: https://www.geeksforgeeks.org/find_element_by_css_selector-driver-method-selenium-python/?ref=rp
## Python program to demonstrate
## selenium
#
## import webdriver
#from selenium import webdriver
#
## create webdriver object
#driver = webdriver.Firefox()
#
## enter keyword to search
#keyword = "geeksforgeeks"
#
## get geeksforgeeks.org
#driver.get("https://www.geeksforgeeks.org/")
#
## get element
##element = driver.find_element_by_css_selector("input.gsc-i-id2")
#element = driver.find_element("css selector", "input.gsc-i-id2")
#
## print complete element
#print(element)


#ref: https://github.com/notmike101/craigslist-poster
# Developed by Michael Orozco
# iBit IT
# Start dev: 10/16/2015 11:38pm
# End dev: 10/17/2015 1:45am

#import sys, argparse, string, ctypes, os, re
#import urllib, urllib2, cookielib, httplib
#import cookielib, time, base64
#
#from os import path
#from bs4 import BeautifulSoup
#from selenium import webdriver
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException
#
#from pyvirtualdisplay import Display
#import spintax

#class craigslistBot:
#    def debug(self, inString):
#        print (" [LOG] {BOT} - %s" % inString.encode('utf-8').strip())
#
#    def __init__(self, loginEmail = "", loginPass = "", contactNumber = "", contactName = "", postTitle = "", postCode = "", postContentFile = "", waitTime = 10):
#        self.display = ""
#
#        if not os.name == 'nt':
#            self.display = Display(visible=0,size=(800,600))
#            self.display.start()
#
#        self.client        = webdriver.Firefox()
#        self.isLoggedIn    = False
#        self.loginEmail    = loginEmail
#        self.loginPass     = loginPass
#        self.contactNumber = contactNumber
#        self.contactName   = contactName
#        self.postTitle     = postTitle
#        self.postCode      = postCode
#        self.postContent   = postContentFile
#        self.waitTime      = waitTime
#
#    def __del__(self):
#        if not os.name == 'nt':
#            self.display.stop()
#
#        self.client.quit()
#        return 0
#
#    def login(self):
#        self.debug("Navigating to craigslist login")
#        self.client.get("https://accounts.craigslist.org/login")
#        self.debug("Logging in")
#        self.client.find_element_by_css_selector("#inputEmailHandle").send_keys(self.loginEmail)
#        self.client.find_element_by_css_selector("#inputPassword").send_keys(self.loginPass)
#        self.client.find_element_by_css_selector("form[name='login'] .loginBox button").click()
#
#        try:
#            self.client.find_element_by_css_selector('.tab')
#        except NoSuchElementException:
#            self.debug("Not logged in")
#            return
#        self.debug("Logged in")
#        self.isLoggedIn = True
#
#    def createPost(self):
#        if not self.isLoggedIn:
#            return 0
#
#        self.debug("Navigating to post page")
#        self.client.get("http://losangeles.craigslist.org/search/sgv/cps")
#        self.client.find_element_by_css_selector(".post a.no-mobile").click()
#        time.sleep(self.waitTime)
#        self.client.find_element_by_css_selector("input[value='so']").click()
#        time.sleep(self.waitTime)
#        self.client.find_element_by_css_selector("input[value='76']").click()
#        time.sleep(self.waitTime)
#        self.client.find_element_by_css_selector("input[value='4']").click()
#        time.sleep(self.waitTime)
#
#        self.debug("Trying to fill in email")
#        try:
#            self.client.find_element_by_css_selector('#FromEMail').send_keys(self.loginEmail)
#        except NoSuchElementException:
#            self.debug("Not avaliable")
#        try:
#            self.client.find_element_by_css_selector('#FromEMail').send_keys(self.loginEmail)
#        except NoSuchElementException:
#            self.debug("Not avaliable")
#
#        self.debug("Checking 'Okay to contact by phone'")
#        self.client.find_element_by_css_selector("#contact_phone_ok").click()
#        time.sleep(self.waitTime)
#        self.debug("Checking 'Okay to contact by text'")
#        self.client.find_element_by_css_selector("#contact_text_ok").click()
#        time.sleep(self.waitTime)
#        self.debug("Filling in contact phone number")
#        self.client.find_element_by_css_selector("#contact_phone").send_keys(self.contactNumber)
#        time.sleep(self.waitTime)
#        self.debug("Filling in contact name")
#        self.client.find_element_by_css_selector("#contact_name").send_keys(self.contactName)
#        time.sleep(self.waitTime)
#        self.debug("Filling in post title")
#        self.client.find_element_by_css_selector("#PostingTitle").send_keys(spintax.parse(self.postTitle))
#        time.sleep(self.waitTime)
#        self.debug("Filling in zip code")
#        self.client.find_element_by_css_selector("#postal_code").send_keys(self.postCode)
#        time.sleep(self.waitTime)
#
#        self.debug("Getting post content")
#        f = open(self.postContent, "rb")
#        content = f.read()
#        f.close()
#
#        self.debug("Spinning content")
#        spinContent = spintax.parse(content)
#
#        self.debug("Filling in post content")
#        self.client.find_element_by_css_selector("#PostingBody").send_keys(spinContent)
#        time.sleep(self.waitTime)
#        self.debug("Checking 'Okay to contact for other offers'")
#        self.client.find_element_by_css_selector("#oc").click()
#        time.sleep(self.waitTime)
#        self.debug("Unchecking 'Want a map' if checked")
#        try:
#            self.client.find_element_by_css_selector("#wantamap:checked")
#        except NoSuchElementException:
#            self.debug("Not checked")
#        finally:
#            self.client.find_element_by_css_selector("#wantamap:checked").click()
#        time.sleep(self.waitTime)
#        self.debug("Clicking continue")
#        self.client.find_element_by_css_selector('button[value="Continue"]').click()
#        time.sleep(self.waitTime)
#        if "editimage" in self.client.current_url:
#            self.debug("Clicking continue")
#            self.client.find_element_by_css_selector('button.done').click()
#        time.sleep(self.waitTime)
#        self.debug("Clicking publish")
#        self.client.find_element_by_css_selector('.draft_warning button[value="Continue"]').click()
#        time.sleep(10)
#
#def main(loginEmail,loginPass,contactNumber,contactName,postTitle,postCode,postContentFile,waitTime):
#    startExecTime = time.time()
#
#    clBot = craigslistBot(loginEmail,loginPass,contactNumber,contactName,postTitle,postCode,postContentFile,waitTime)
#    clBot.login()
#    clBot.createPost()
#    endExecTime = time.time()
#    clBot.debug("Execution time: %s seconds" % int(endExecTime - startExecTime))
#
#    print("Finished")
#
#    return 0
#
#parser = argparse.ArgumentParser(description="Craigslist Poster Script")
#parser.add_argument('loginEmail',metavar='LOGINEMAIL',type=str,help='Email to use for login')
#parser.add_argument('loginPass',metavar='LOGINPASS',type=str,help='Password to use for login')
#parser.add_argument('contactNumber',metavar='CONTACTNUM',type=str,help='Contact number for post')
#parser.add_argument('contactName',metavar='CONTACTNAME',type=str,help='Contact name for post')
#parser.add_argument('postTitle', metavar='POSTTITLE', type=str, help='Title of the post to be made')
#parser.add_argument('postCode',metavar='POSTCODE',type=str,help='Zip code for post')
#parser.add_argument('postContent',metavar='POSTCONTENT',type=str, help='Path to file for post content')
#parser.add_argument('waitTime',metavar='WAITTIME',type=int,help='Time to wait in between actions (Recommend 3)')
#args = parser.parse_args()
#main(args.loginEmail,args.loginPass,args.contactNumber,args.contactName,args.postTitle,args.postCode,args.postContent,args.waitTime)

# Test Execution
# python {{SCRIPTNAME}} "example@example.com" "password" "123-456-7890" "Bob" "Post Title" "12345" "content.txt" 3
