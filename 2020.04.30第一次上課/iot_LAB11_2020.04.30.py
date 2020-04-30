from machine import Pin
import time
import dht

sensor = dht.DHT11(Pin(0)) #使用D3腳位取得溫濕度物件
while True:
    sensor.measure() # 讀取溫濕度值
    temp_humi = "%2d °C/%2d%%" % (#格式化字串
    sensor.temperature(), #置入溫濕度值
    sensor.humidity()) #置入溫濕度值
    print(temp_humi) #顯示溫濕度值
    time.sleep(3)  #暫停3秒