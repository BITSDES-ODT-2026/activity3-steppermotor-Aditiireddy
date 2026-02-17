from machine import Pin
import time
list = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
in1=Pin(13,Pin.OUT)
in2=Pin(12,Pin.OUT)
in3=Pin(14,Pin.OUT)
in4=Pin(27,Pin.OUT)

while True:
    for l in range(500):
        for i in list:
            in1.value(i[0])
            in2.value(i[1])
            in3.value(i[2])
            in4.value(i[3])
            time.sleep_ms(5)
            print("anti")
    for p in range(500):
        for x in list:
            in4.value(x[0])
            in3.value(x[1])
            in2.value(x[2])
            in1.value(x[3])
            time.sleep_ms(5)
            print("clock")
      
