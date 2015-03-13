from Utils.oopcurl import *
from Utils.GetIp import GetIP
import time
import os


def LifeConekt():
    ThreeG = Post()
    ThreeG.Post('http://192.168.8.1/api/dialup/mobile-dataswitch','<?xml version="1.0" encoding="UTF-8"?><request><dataswitch>1</dataswitch></request>')



def LifeDisconekt():
    ThreeG = Post()
    ThreeG.Post('http://192.168.8.1/api/dialup/mobile-dataswitch','<?xml version="1.0" encoding="UTF-8"?><request><dataswitch>0</dataswitch></request>')

# Функция рекурсия реконект  Лайфа
def LifeConektRecursia(num):
    if num == 0:
        return False
    else:
        LifeConekt()
        time.sleep(0.5)
        Ip = GetIP()
        if "NoIp" == Ip:
            LifeDisconekt()
            return LifeConektRecursia(num - 1)
        elif "NoIp" != Ip:
            return True
    return LifeConektRecursia(num - 1)


def ConnectOther(connection):
    command = r'RASDIAL %s' % connection
    return os.system(command)

def ConnectOtherRecursia(connection, num):
    command = r'RASDIAL %s' % connection
    if num == 0:
        return False
    else:
        os.system(command)
        time.sleep(5)
        Ip = GetIP()
        if "NoIp" == Ip:
            return ConnectOtherRecursia(connection, num - 1)

    return ConnectOtherRecursia(connection, num - 1)

def DisconnectOther(connection):
    command = r'RASDIAL %s /DISCONNECT' % connection
    return os.system(command)




#http://support.microsoft.com/kb/311272/ru
def Other3G():
    os.system()
    pass