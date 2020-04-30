from machine import Pin, PWM
import time, network, urequests, ujson 

#連線wifi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi基地台", "Wifi密碼")
while not sta_if.isconnected():
    pass
print("Wifi已連上")

rLED = PWM(Pin(12)) #控制紅燈
gLED = PWM(Pin(13)) #控制綠燈

while True:
    res = urequests.get("政府資料開放平台AQI網址")
    
    j = ujson.loads(res.text); #載入並解析JSON格式資料
    
    print("測站名稱:", j[0]["SiteName"])
    print("發布名稱:", j[0]["PublishTime"])
    print("空污狀態:", j[0]["Status"])
    print("AQI:", j[0]["AQI"])
    print("PM2.5:", j[0]["PM2.5"])
    
    AQI = int(j[0]["AQI"]) #將AQI空污指數轉為整數，以便比較大小
    
    if AQI <= 50 :
        gLED.duty(1023); rLED(0) #顯示綠燈
    elif 51 <= AQI <= 100 :
        gLED.duty(300); rLED(1023) #顯示黃燈
    else:
        gLED.duty(0); rLED(1023) #顯示紅燈
        
    time.sleep(1800) #每半小時更新一次燈號
    
    