class Luggage:
    #行李類別的建構子
    def __init__(self,id,weight,departure,destination,name):
        self._id=id
        self._weight=weight
        self._departure=departure
        self._destination=destination
        self._name=name
    #查詢行李
    def getLuggage(self):
        print('行李ID:',self._id)
        print('行李重量:',self._weight)
        print('出發機場:',self._departure)
        print('目的機場:',self._destination)
        print('旅客姓名:',self._name)
    #修改資訊
    def getnewLuggage(self):
        print('修改資訊')
        print('行李ID:',self._id)
        print('行李重量:',self._weight)
        print('出發機場:',self._departure)
        print('目的機場:',self._destination)
        print('旅客姓名:',self._name)
    #副函式
    #修改ID
    def ModifyId(self, newid):
        self._id = newid
    #修改重量
    def ModifyWeight(self, newweight):
        self._weight = newweight
    #修改出發地
    def ModifyDeparture(self, newdeparture):
        self._departure = newdeparture
    #修改目的地
    def ModifyDestination(self, newdestination):
        self._destination = newdestination
    #修改旅客姓名
    def ModifyName(self, newname):
        self._name = newname
#呼叫建構子，建立遊戲物件 
L1=Luggage(7414,'12kg','高雄國際機場','桃園國際機場','小智')
L2=Luggage(6487,'8kg','桃園國際機場','臺北松山機場','阿明')
L3=Luggage(5943,'20kg','臺北松山機場','臺中國際機場','春嬌')
L4=Luggage(1325,'5kg','臺中國際機場','高雄國際機場','阿強')
#行李資訊
L4.getLuggage()
L4.ModifyId(5521)
L4.ModifyDestination('臺北松山機場')
L4.ModifyWeight('21kg')
#印出修改資訊
L4.getnewLuggage()
print(L4._name)
class Boarding_pass:
    #登機證類別的建構子
    def __init__(self,name,number,time,gatenumber,seat,baggage,id):
        self._name=name
        self._number=number
        self._time=time
        self._gatenumber=gatenumber
        self._seat=seat
        self._baggage=baggage
        self._id=id
    def getBoarding_pass(self):
        print('旅客姓名:',self._id)
        print('登機證編號:',self._number)
        print('登機時間:',self._time)
        print('登機門編號:',self._gatenumber)
        print('座位位置:',self._seat)
        print('行李件數:',self._baggage)
        print('旅客ID:',self._id)
    #修改旅客姓名
    def ModifyName(self, newname):
        self._name = newname
    #修改登機證編號
    def ModifyNumber(self, newnumber):
        self._number = newnumber
    #修改登機時間
    def ModifyTime(self, newtime):
        self._time = newtime
    #修改登機門編號
    def ModifyGatenNmber(self, newgatenumber):
        self._gatenumber = newgatenumber
    #修改座位位置
    def ModifySeat(self, newseat):
        self._seat = newseat
    #修改行李件數
    def ModifyBaggage(self, newbaggage):
        self._baggage = newbaggage
    #修改ID
    def ModifyId(self, newid):
        self._id = newid
#呼叫建構子，建立遊戲物件
B1=Boarding_pass('小智',5334,'10:10',6,'L31',2,7414)
B2=Boarding_pass('阿明',5521,'09:25',5,'R21',1,6487)
B3=Boarding_pass('春嬌',5213,'01:12',3,'R14',2,5943)
B4=Boarding_pass('阿強',6742,'12:12',7,'L15',3,1325)


B4.getBoarding_pass()
B4.ModifyName('娓娓')
B4.ModifyNumber(5487)
B4.ModifyTime('06:11')
B4.ModifyGatenNmber(2)
B4.ModifySeat('L82')
B4.ModifyBaggage(6)
B4.ModifyId(1154)
B4.getBoarding_pass()