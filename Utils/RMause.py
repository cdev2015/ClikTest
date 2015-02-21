# -*- coding: utf-8 -*-

import win32api
import random

def RandomMause():
    ls = [random.randint(10,250) for i in range(20)]
    Up= random.choice(ls)
    Right= random.choice(ls)
    random.choice([Right,-Right])
    # нажали левую кнопку мыши
    win32api.mouse_event(2,0,0)
    # переместили курсор вправо на 100 и вверх на 50
    win32api.mouse_event(5,random.choice([Up,-Up]),random.choice([Right,-Right]))
    # отжали левую кнопку мыши
    win32api.mouse_event(4,0,0)

if __name__ == "__main__":
    RandomMause()
