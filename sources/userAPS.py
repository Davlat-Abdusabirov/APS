import cardAPS as cardAPS 

class UserAPS(object):
    def __init__(self, userName, avatarImg = "image/standart_user_icon.png"):
        self.userName = userName
        self.cards = []
        self.createCard()
        self.avatarImg = avatarImg

    def createCard(self):
        c = cardAPS.CardAPS()
        self.cards.append(c)

