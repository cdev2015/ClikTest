# -*- coding: utf-8 -*-

import os

def ProcessKill (process_name):
    try:
        killed = os.system('taskkill /im ' + process_name + " /f")
    except Exception, e:
        killed = 0
    return killed

if __name__ == '__main__':
    print ProcessKill("opera.exe")