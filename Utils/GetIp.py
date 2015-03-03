# -*- coding: utf-8 -*-
import urllib2
import re
def GetIP():
    try:
        response = urllib2.urlopen('http://internet.yandex.ru/').read()
        r = '(?<=\<div class\=\"b-info__item b-info__item_type_ip\"\>)[\w\W]*?(?=\<span id)'
        found = re.findall(r, response)
        return found[0].replace(' ','').replace('МойIPv4:','')
    except:
        return "NoIp"

if __name__ == "__main__":
    print GetIP()
