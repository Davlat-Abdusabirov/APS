import cardAPS  

class UserAPS(object):
    def __init__(self, userName, avatarImg = "image/icons-user.png"):
        self.userName = userName
        self.cards = []
        self.friends = []
        self.createCard()
        self.avatarImg = str(avatarImg)
    
    def createCard(self, currency = "AniCoin"):
        self.cards.append(cardAPS.CardAPS(currency))

    def addFriend(self, friend):
        self.friends.append(friend)
        
    def deleteFriend(self, friend):
        self.friends.remove(friend)