# -*- coding: utf-8 -*-
from Confing import *
import time
import random
def TimeSleep():
    """
    Пауза
    """
    time.sleep(random.choice(TemeSleep))


if __name__ == "__main__":
    TimeSleep()

