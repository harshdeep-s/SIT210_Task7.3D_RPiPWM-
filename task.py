import RPi.GPIO as GPIO # here RPi.GPIO is imported
import time                # time library is imported to use the time in code, like to put delays

GPIO.setmode(GPIO.BOARD)        # It tells the library which pin nunbering system you are going to use

Trigpin = 11                    
echopin = 10
 
GPIO.setup(Trigpin, GPIO.OUT)       # setting pin-11 as an output.
GPIO.setup(echopin, GPIO.IN)           # setting pin-10 as an input.
GPIO.setup(12,GPIO.OUT)         # setting pin-12 as an output for led.

p = GPIO.PWM(12,100)        #create PWM instance with frequency
p.start(0)                    #start PWM of required Duty Cycle


while 1:
    GPIO.output(Trigpin, GPIO.HIGH)     # setting pin-11 high
    time.sleep(0.05)                    # delay of 0.05 seconds is used
    GPIO.output(Trigpin, GPIO.LOW)      # setting pin-11 low after 0.05 seconds

    while GPIO.input(echopin) == 0:        # while echopin doesn't get any input, seconds will be stored in variable starttime
        StartTime = time.time()             

    while GPIO.input(echopin) == 1:        #while echopin is high seconds will be stored in variable stoptime             
        StopTime = time.time()
        
    TimeElapsed = StopTime - StartTime          # total time taken by ultrasonic wave to travel is stored into timeelapsed
    

    distance = (TimeElapsed * 17150)            # distance store the distance travelled by wave, formula, distance = speed*time is used
    distance = round(distance, 0)               # distance is round off to zero decimal
    
    if(distance < 500):                            # this statement is used to filter the values, if distance < 500, value will be considered, else not
        distance2 = distance
    distance = distance2
    x = -1.0309*distance + 103.09               # equation is made to change the value of x, if distance changes, later x will be used for led intensity
    if(x <= 0.5):                               # statement used to restrict x should be greater than 0
        x = 0
    if(x >= 100):                               # statement used to restrict x should be smaller than 100
        x = 100
    p.ChangeDutyCycle(x)                       #provide duty cycle in the range 0-100 as x lies between 0 to 100.
    print(distance)
