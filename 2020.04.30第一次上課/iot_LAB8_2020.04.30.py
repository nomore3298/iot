from machine import Pin, PWM
import mfrc522, network, urequests, time

#連線wifi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi基地台", "Wifi密碼")
while not sta_if.isconnected():
    pass
print("Wifi已連上")

while True:
     led.value(0) #搜尋卡片之前先關閉LED
     stat, tag_type = rfid.request(rfid.REQIDL) #搜尋RFID卡片
     
     if stat == rfid.OK: #找到卡片
         stat, raw_uid = rfid.anticoll() #讀取RFID卡號
         if stat == rfid.OK:
             led.value(1) #讀到卡號後點亮LED
             
             #將卡號由2進位格式轉換為16進位的字串
             id = "%02x%02x%02x%02x" %(raw_uid[0], raw_uid[1], 
                                       raw_uid[2], raw_uid[3])
             print("偵測到卡號:", id)
             
             #連線IFTTT服務發送簡訊通知
             ifttt_url = "IFTTT的HTTP請求網址"
             urequests.get(ifttt_url + "?value1=" + id)
             
             time.sleep(0.5) #暫停一下，避免LED太快熄滅看不到
             

