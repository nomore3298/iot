from machine import ADC
import time, network, urequests

#連線wifi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi基地台", "Wifi密碼")
while not sta_if.isconnected():
    pass
print("Wifi已連上")


aio_username = "您的Adafruit IO 帳號"
aio_key = "您的Adafruit IO 金鑰"
aio_feed = "您的Adafruit IO feed 名稱"

#建立A0腳位的ADC物件，並命名為adc
adc = ADC(0)

while True:
    #讀取雨水感測器經過ADC轉換後的數值
    value = adc.read()
    
    if value < 700 : #依照Lab9的測試，低於700表示有下雨
        #雨水越多，ADC值越低，所以用最大值1024減ADC值，
        #以便將資料反轉為雨水越多，數值越高
        data = {"value:" 1024-value}
    else:
        #沒下雨的話就送出0
        data = {"value:" 0}
    #設定Adafruit IO 上傳資料的API網址
    url = ("http://io.adafruit.com/api/v2/" + aio_username +
           "/feeds/" + aio_feed + "/data?X-AIO-Key=" + aio_key)
    
    #用POST上傳JSON資料
    urequests.post(url, json=data)

    #暫停2秒
    time.sleep(2)
