from random import randint

class CardAPS(object):
    def __init__(self, currency = "AniCoin", money = 0.0):
        self.generationId()
        self.currency = currency
        self.__money = money

    def generationId(self):
        id = ""
        for i in range(3):
            for j in range(4):
                id += str(randint(0, 9))
            if i != 2:
                id += " "
        self.ID = id

    def addMoney(self, add):
        self.__money += add
    
    def takeMoney(self, take):
        if take < 0:
            raise Exception("Сумма платежа меньше нуля!")
        else:
            if take > self.__money:
                raise Exception("Недостаточно средств!")
            else:
                self.__money -= take


    def printData(self):
        print(self.ID, self.currency, ":", self.__money)
