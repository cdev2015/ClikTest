import os, sys

import win32api
import win32con
import pywintypes
import random

displayList = [(1920, 1080), (1768, 992), (1680, 1050), (1600, 1200), (1600, 1024), (1600, 900
), (1440, 900), (1400, 1050), (1360, 768), (1280, 1024), (1280, 960), (1280, 800
), (1280, 768), (1280, 720), (1152, 864), (1024, 768), (800, 600), (720, 576), (
720, 480), (640, 480)]

MyMonitor = [(800,600),(1024,768),(1152,864),(1280,1024),(1600,1200)]

def RandomMonitor(WidthHeightList):
    display_modes = {}
    n = 0
    while True:
      try:
        devmode = win32api.EnumDisplaySettings (None, n)
      except pywintypes.error:
        break
      else:
        key = (

          devmode.PelsWidth,
          devmode.PelsHeight

        )
        display_modes[key] = devmode
        n += 1
    ExtensionDiplay = random.choice(WidthHeightList)
    WidthDiplay = ExtensionDiplay[0]
    HeightDiplay = ExtensionDiplay[1]
    mode_required = (WidthDiplay, HeightDiplay)
    devmode = display_modes[mode_required]
    win32api.ChangeDisplaySettings (devmode, 0)
    return ExtensionDiplay

if __name__ == "__main__":
    RandomMonitor(MyMonitor)