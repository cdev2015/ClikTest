# -*- coding: utf-8 -*-
from distutils.errors import LibError
from Utils.SaveLog import *
from Utils.GetIp import GetIP
from Utils.GetTime import PtesentTime
from Utils.DisplayChange import RandomMonitor
from Utils.GetMonitorExp import GetMonitorExp
from Utils.YaDiskClient import *
from Utils.Convert import StrToDict
from Utils.Keyword import Keyword
from Utils.Conekt3G import *
from Utils.Reboot import RebootServer
from browsers.Chrome import Chrome
from browsers.FireFox import FireFox
from browsers.Opera import Opera
from browsers import Chrome
import random
import ConfigParser
import time

SaveLog((10 * "=") + "Start" + (10 * "="))
# Загрузка Конфигурации

#GetConfig()



config = ConfigParser.ConfigParser()
config.read(Confing.Options["RootPath"] + "//" +  "Config.cfg")
IfLife =  config.get("ThreeGLife","ISP") #Чек на лайф

KeywordData = Keyword() # Создаем клас для работи с ключами
KeywordData.load() #Загружаем ключи в стек

# Получене ИП для Лайфа
if IfLife == "Yes":
    SaveLog("ConnektLife " + PtesentTime())
    LifeConekt() #Подключаем лайф
    Ip = GetIP()
    if "NoIp" == Ip:
        SaveLog("ReConnekt " + PtesentTime())
        SteatusConekta = LifeConektRecursia(3)
        if SteatusConekta == False:
            # Reboot
            #RebootServer()
            pass
    elif "NoIp" != Ip:
        SaveLog("Get Ip " + Ip.rstrip() + " " + PtesentTime())

elif IfLife == "No":
    #Конект Оругих операторов
    ModemNameInPci = StrToDict(config.get("IPS","Modem"))
    ConnectOther(ModemNameInPci[0])
    time.sleep(10)
    Ip = GetIP()
    if "NoIp" == Ip:
        SaveLog("ReConnekt " + PtesentTime())
        SteatusConekta =  ConnectOtherRecursia(ModemNameInPci[0],3)
        if SteatusConekta == False:
            # Reboot
            #RebootServer()
            pass
    elif "NoIp" != Ip:
        SaveLog("Get Ip " + Ip.rstrip() + " " + PtesentTime())


    pass



# Случайная установка Росширенния монитора
ListMonitorExp = GetMonitorExp()
MonExpLog = RandomMonitor(ListMonitorExp)
SaveLog("MonitorExp " + str(MonExpLog))



BrowserList =  StrToDict(config.get("Browser","Choise")) # Грузим список броузеров из конфига
BrowserChoise = random.choice(BrowserList)# Вибераем случайний

if IfLife == "Yes":
    SaveLog("Life Start " + PtesentTime()) #Старт  Лайф
    if KeywordData.is_empty(): KeywordData.load() #роверка не опустел ли стек если да грузим Ключи

    if "Chrome" == BrowserChoise:
        SaveLog("Start Chrome " + PtesentTime())
        Chrome(KeywordData.pop())
        SaveLog("Stop Chrome " + PtesentTime())
    elif "FireFox" == BrowserChoise:
        SaveLog("Start FireFox " + PtesentTime())
        FireFox(KeywordData.pop())
        SaveLog("Stop FireFox " + PtesentTime())
    elif "Opera" == BrowserChoise:
        SaveLog("Start Opera " + PtesentTime())
        Opera(KeywordData.pop())
        SaveLog("Stop Opera " + PtesentTime())



    pass
elif IfLife == "No":
    SaveLog("Othet Start " + PtesentTime()) #Старт  Другие Свистки


    if KeywordData.is_empty(): KeywordData.load() #роверка не опустел ли стек если да грузим Ключи

    if "Chrome" == BrowserChoise:
        SaveLog("Start Chrome " + PtesentTime())
        Chrome(KeywordData.pop())
        SaveLog("Stop Chrome " + PtesentTime())
    elif "FireFox" == BrowserChoise:
        SaveLog("Start FireFox " + PtesentTime())
        FireFox(KeywordData.pop())
        SaveLog("Stop FireFox " + PtesentTime())
    elif "Opera" == BrowserChoise:
        SaveLog("Start Opera " + PtesentTime())
        Opera(KeywordData.pop())
        SaveLog("Stop Opera " + PtesentTime())


