import datetime

def PtesentTime():
    return  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    print PtesentTime()