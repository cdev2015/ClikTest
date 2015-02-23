import win32api
import pywintypes
# Get Monitor Expansion
def GetMonitorExp():
    display_modes = []
    n = 0
    while True:
      try:
        devmode = win32api.EnumDisplaySettings (None, n)
      except pywintypes.error:
        break
      else:
        key = (
          #devmode.BitsPerPel, #Color
          devmode.PelsWidth,
          devmode.PelsHeight,
          #devmode.DisplayFrequency # KHz
        )
        display_modes.append(key)
        n += 1
    return display_modes


if __name__ == "__main__":
    print GetMonitorExp()
