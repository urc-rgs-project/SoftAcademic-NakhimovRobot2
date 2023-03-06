from machine import Pin, PWM
from time import sleep

servoPin = PWM(Pin(19))
servoPin.freq(50)

def servo(degrees):
    if degrees > 110:
        degrees=110
    if degrees < 40:
        degrees=40
    
    maxDuty=8000
    minDuty=1500
    
    newDuty=minDuty+(maxDuty-minDuty)*(degrees/180)
    servoPin.duty_u16(int(newDuty))
    
while True:
    servo(180)
    print("increasing -- 180")
    sleep(2)
    
    servo(90)
    print("increasing -- 90")
    sleep(2)
    
    servo(0)
    print("increasing -- 0")
    sleep(2)


# протестированно 