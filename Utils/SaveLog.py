# -*- coding: utf-8 -*-
import os
import datetime
import Confing
from Utils.YaDiskClient import *


def SaveLog(date):
    now_date = datetime.date.today()
    Path = Confing.Options['RootPath'] + '\\' + 'log' + '\\'
    name_file =  Path + str(now_date)+ '_Log' + str('.txt')
    data = '{0}\n'.format(date)
    f3 = open(name_file, "a")
    f3.write (data)
    f3.close()

def UploadLog():
    now_date = datetime.date.today()
    Path = Confing.Options['RootPath'] + '\\' + 'log' + '\\'
    name_file =  Path + str(now_date)+ '_Log' + str('.txt')
    Disk = YaDisk(Confing.YandexDiskLoginPass["Login"],Confing.YandexDiskLoginPass["Pass"])
    Disk.upload(name_file,"/log/" + str(now_date)+ '_Log' + str('.txt'))


def GetConfig():
    PathConfig = Confing.Options['RootPath'] + '\\' + 'Config.cfg'
    Disk = YaDisk(Confing.YandexDiskLoginPass["Login"],Confing.YandexDiskLoginPass["Pass"])
    print Disk.download("/Config.cfg",PathConfig)
    pass

if __name__ == "__main__":
    logData = 'tests'
    SaveLog(logData)
    UploadLog()
    GetConfig()

