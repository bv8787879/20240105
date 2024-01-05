class Game:
    #遊戲類別的建構子
    def __init__(self,name,type,sell):
        #屬性定義
        self._name=name
        self._type=type
        self._sell=sell
class game_library(Game):
    def __init__(self,name,type,sell):
        super().__init__(name,type,sell)
    #副函式
    #遊戲資訊的函式
    def getGame_information(self):
        print('遊戲名稱:', self._name)
        print('遊戲類別:', self._type)
        print('售價:', self._sell)
    #遊戲打折的函式
    def getDiscount(self,a):
        return self._sell*a
    #修改售價的函式
    def getType(self,newsell):
        self._sell = newsell
#呼叫建構子，建立遊戲物件 
G1=game_library('GTA6','open world',1190)
G2=game_library('party animal','Funny',320)
G3=game_library('Apex','Shooting',0)
G4=game_library('LOL','MOBA',0)
#列印結果
G1.getGame_information()
print('折扣價格',G2.getDiscount(0.75))
G4.getType(1000)
print('遊戲售價',G4._sell)