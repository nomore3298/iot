#從machine匯入Pin物件
from machine import Pin
#匯入時間模組
import time

#建立16號腳位的Pin物件，設定為輸入腳位，並命名為shock
shock = Pin(16,Pin.IN)

while True:
    #用value()方法從16號腳位讀取按鈕輸出的高低電位
    #然後將讀到值用print()輸出
    print(shock.value())
    time.sleep(0.5)#暫停0.5秒
    