# -*- coding: utf-8 -*-
import Confing
from Utils.Stack import Stack




class Keyword(Stack): # Наследует реализцию стека


    def load(self): #Загрузка Ключей
        KeyList = open(Confing.Options["RootPath"] + "\\Keyword\\Keyword.txt").readlines()
        for i in KeyList:
            self.push(i)





if __name__ == "__main__":
    s = Keyword()
    s.load()
    print s.is_empty()
    print s.pop()
    print s.is_empty()
