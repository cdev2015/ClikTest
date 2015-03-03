from Utils.oopcurl import *
import os


def LifeConekt():
    ThreeG = Post()
    ThreeG.Post('http://192.168.8.1/api/dialup/mobile-dataswitch','<?xml version="1.0" encoding="UTF-8"?><request><dataswitch>1</dataswitch></request>')



def LifeDisconekt():
    ThreeG = Post()
    ThreeG.Post('http://192.168.8.1/api/dialup/mobile-dataswitch','<?xml version="1.0" encoding="UTF-8"?><request><dataswitch>0</dataswitch></request>')

#http://support.microsoft.com/kb/311272/ru
def Other3G():
    os.system()
    pass