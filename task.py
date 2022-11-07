import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

Trigpin = 11
echopin = 10
 
GPIO.setup(Trigpin, GPIO.OUT)
GPIO.setup(echopin, GPIO.IN)
GPIO.setup(12,GPIO.OUT)

p = GPIO.PWM(12,100)
p.start(0)                    


while 1:
    GPIO.output(Trigpin, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(Trigpin, GPIO.LOW)

    while GPIO.input(echopin) == 0:
        StartTime = time.time()

    while GPIO.input(echopin) == 1:
        StopTime = time.time()
        
    TimeElapsed = StopTime - StartTime
    

    distance = (TimeElapsed * 17150)
    distance = round(distance, 0)
    
    if(distance < 500):
        distance2 = distance
    distance = distance2
    x = -1.0309*distance + 103.09
    if(x <= 0.5):
        x = 0
    if(x >= 100):
        x = 100
    p.ChangeDutyCycle(x)
    print(distance)