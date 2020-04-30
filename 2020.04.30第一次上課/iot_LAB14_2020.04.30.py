from machine import Pin
import dht, BlynkLib, network

sta_if = network.WLAN(network.STA_IF) 
sta_if.active(True)
sta_if.connect("Wifi基地台", "Wifi密碼")
while not sta_if.isconnected():
    pass
print("connect")

token = "這裡要填入剛剛收到的權杖"
blynk = BlynkLib.Blynk(token)

sensor = dht.DHT11(Pin(0))
relay = Pin(14, Pin.OUT,value = 0 )

def v1_handler():
    sensor.measure()
    blynk.virtual_write(1, sensor.temperature())

def v2_handler():
    sensor.measure()
    blynk.virtual_write(2, sensor.humidity())

def v3_handler():
    relay.value(int(value[0]))
    
blynk.on("readV1",v1_handler)
blynk.on("readV2",v2_handler)
blynk.on("V3",v3_handler)

while True:
    blynk.run()