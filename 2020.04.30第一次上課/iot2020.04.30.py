#從machine匯入Pin物件
from machine import Pin
#匯入時間模組
import time

#建立2號腳位的Pin物件，設定為輸出腳位，並命名為led
led = Pin(2, Pin.OUT)

led.value(0) #設定為低電位，點亮led
time.sleep(3) #暫停3秒
led.value(1) #設定為高電位，熄滅led
