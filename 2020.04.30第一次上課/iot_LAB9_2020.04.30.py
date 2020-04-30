from machine import ADC
import time

#建立A0腳位的ADC物件，並命名為adc
adc = ADC(0)

while True:
    #用read()方法從A0號腳位讀取ADC轉換後的數值
    #然後將讀到的值用print()輸出
    print(adc.read())
    
    #暫停0.5秒
    time.sleep(0.5)