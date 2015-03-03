# -*- coding: utf-8 -*-
from distutils.errors import LibError
from Utils.SaveLog import *
from Utils.GetIp import GetIP
from Utils.GetTime import PtesentTime
from Utils.DisplayChange import RandomMonitor
from Utils.GetMonitorExp import GetMonitorExp
from Utils.YaDiskClient import *
from Utils.Convert import StrToDict
import random
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('Config.cfg')


#Dowload Config
#GetConfig()


SaveLog((10 * "=") + "Start" + (10 * "="))
#ToDo Conekt 3G
Ip = GetIP()
if "NoIp" == Ip:
    #ToDo ReConnekt
    SaveLog("ReConnekt " + PtesentTime())
    pass
else:


    SaveLog("Get Ip " + Ip + " " + PtesentTime())
    # Случайная установка Росширенния монитора
    ListMonitorExp = GetMonitorExp()
    MonExpLog = RandomMonitor(ListMonitorExp)
    SaveLog("MonitorExp " + str(MonExpLog))

    BrowserDict = StrToDict(config.get("Browser","Choise"))
    Browser = random.choice(BrowserDict)

    if "Chrome" in Browser:
        pass
    elif "FireFox" in Browser:
        pass
    elif "Opera" in Browser:
        pass
