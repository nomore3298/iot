#從machine匯入Pin物件
from machine import Pin
#匯入時間模組,網路模組,連線模組
import time,network,urequests
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi基地台", "Wifi密碼")
while not sta_if.isconnected():
    pass
print("Wifi已連上")

username = "簡訊服務帳號"
passwd = "簡訊服務密碼"
phone = "接收簡訊的手機號碼"
message = "有人打開保險箱在翻找東西，趕快去抓小偷!" # 請勿輸入空格

#建立16號腳位的Pin物件，設定為輸入腳位，並命名為shock
shock = Pin(16,Pin.IN)

while True:
    if shock.value() == 1:
        print("感應到震動")
        
        #連線簡訊服務發送簡訊通知
        urequests.get("http://api.message.net.tw/send.php?mtype=G&id="
                      +username + "&encoding=utf8&password="+passwd
                      +"&tel="+phone +"&msg="+message)
        #暫停60秒
        time.sleep(60)
