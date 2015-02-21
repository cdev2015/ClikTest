# -*- coding: utf-8 -*-
import os
import datetime
import Confing
def SaveLog(date):
    now_date = datetime.date.today()
    Path = Confing.Options['RootPath'] + '\\' + 'log' + '\\'
    name_file =  Path + str(now_date)+ '_Log' + str('.txt')
    data = '{0}\n'.format(date)
    f3 = open(name_file, "a")
    f3.write (data)
    f3.close()
if __name__ == "__main__":
    logData = 'test'
    SaveLog(logData)

