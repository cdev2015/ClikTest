# -*- coding: utf-8 -*-
import socket
def CheckInet():
    try:
      socket.gethostbyaddr('m.yandex.ru')
    except socket.gaierror:
        return False
    return True
if __name__ == "__main__":
    print CheckInet()