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

def FireFox(Keyword):

    browser = webdriver.Firefox() # Get local session of firefox
    browser.delete_all_cookies() # Delite Cookies
    browser.get("http://www.google.com.ua") # Load page

    if capcha not in browser.page_source:
        Key = Keyword.decode('utf-8')
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
                try:
                    if SiteName in str(Link.get_attribute("href")):
                        Link = browser.find_element_by_class_name(className).click()

                        NumberStep = random.choice(LinkStep)

                        for i in range(NumberStep):
                            TimeSleep()

                            Links = browser.find_elements_by_tag_name('a')
                            if len(Links) ==0:
                                browser.close()
                                continue

                            Links = random.choice(Links)
                            L = Links.get_attribute("href")
                            browser.get(L)

                        browser.close()
                except AttributeError:
                    pass





if __name__ == "__main__":
    FireFox("кондиционеры киев купить")