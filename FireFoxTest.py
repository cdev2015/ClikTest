# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import random
from ConfigFindId import ListId
from ConfigPrioritet import ListPrioritetUrl
from Utils.TimeSleep import TimeSleep
from Confing import LinkStep

capcha = 'sorry/image'
#Todo На даном коде проверить работоспособность всех броузеров

browser = webdriver.Firefox() # Get local session of firefox
browser.get("http://www.google.com.ua") # Load page

if capcha not in browser.page_source:
    print "GeT"
    Key = "кондиционеры киев купить".decode('utf-8')
    search_box = browser.find_element_by_name('q')
    search_box.send_keys(Key)
    search_box.submit()
    for className in ListId():
        pass
        print className
        try:
            Link = browser.find_element_by_class_name(className)
        except:
            continue

        for SiteName in ListPrioritetUrl().values():
            print SiteName
            if SiteName in str(Link.get_attribute("href")):
                first_link = Link
                Link = browser.find_element_by_class_name(className).click()


                # for i in range(LinkStep):
                #     TimeSleep()
                Links = browser.find_elements_by_tag_name('a')
                Links = random.choice(Links)
                L = Links.get_attribute("href")
                browser.get(L)


browser.close()