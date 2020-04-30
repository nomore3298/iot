from machine import Pin
import time
import network
from umqtt.robus import MQTTClient
import dht

sensor = dht.DHT11(Pin(0)) #使用D3腳位取得溫濕度物件

client = MQTTClient(  #建立物件
    client_id = "weather", #用戶端識別名稱
    server = "io.adafruit.com", #主機網址
    user = "帳戶名稱" #請填入帳戶名稱
    password = "填入你得金鑰"　#請填入你的金鑰
    ssl = False 
    )
#連線wifi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi基地台", "Wifi密碼")
while not sta_if.isconnected():
    pass
print("Wifi已連上")

client.connect()


while True:
    sensor.measure() # 讀取溫濕度值
    temp_humi = "%2d °C/%2d%%" % (#格式化字串
        sensor.temperature(), #置入溫濕度值
        sensor.humidity()) #置入溫濕度值
    client.publish(
        b"帳戶名稱/feeds/temp_humi",
        temp_humi.encode())    
    time.sleep(3)  #暫停3秒
