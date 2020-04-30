from machine import Pin
import time
import network
from umqtt.robus import MQTTClient
import dht

sensor = dht.DHT11(Pin(0)) #使用D3腳位取得溫濕度物件
relay = Pin(14, Pin.OUT, value = 0) #使用D5腳位控制繼電器

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
print("connect")

def get_cmd(topic, msg): #處理新資料的函式
    if msg == b"on":  #收到on指令
        relay.value(1) #打開繼電器
    elif msg == b"off": #收到off指令
        relay.value(0) 
    print(msg)
    
client.connect()
client.set_callback(get_cmd) #註冊處理函式
client.subscribe(b"帳戶名稱/feeds/fan"); #訂閱頻道
last_time = 0  #紀錄前次發送資料的時間點

while True:
    if time.time() - last_time >= 3: #若上次發送已超過3秒
        sensor.measure()
        temp_humi = "%2d °C/%2d%%" %(
            sensor.temperature(), #置入溫濕度值
            sensor.humidity()) #置入溫濕度值
        client.publish(
            b"帳戶名稱/feeds/temp_humi",
            temp_humi.encode())
        last_time = time.time() #紀錄本次發送時間點
    client.check_msg()  #檢查新訊息
