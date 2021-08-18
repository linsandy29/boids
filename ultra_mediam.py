#Libraries
import RPi.GPIO as GPIO
import time
from collections import deque

q = deque([0,0,0,0,0])
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 17
GPIO_ECHO = 18
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
#GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()

    GPIO.setup(GPIO_ECHO, GPIO.IN)
    t=0
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
        t = StopTime - StartTime
        if t > 0.0115309038:
            break

    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2

    q.popleft()
    q.append(distance)
    c = q
    c = sorted(c)
    size = len(c)
    median = c[(size-1)//2]
    return median

 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.2f cm" % dist)
            #print (dist)
            time.sleep(0.1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
