#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
trig_two = 17
echo_two = 27
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(trig_two, GPIO.OUT)
GPIO.setup(echo_two, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def distance_two():
    # set Trigger to HIGH
    GPIO.output(trig_two, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(trig_two, False)
 
    StartTime_two = time.time()
    StopTime_two = time.time()

    # save StartTime
    while GPIO.input(echo_two) == 0:
        StartTime_two = time.time()
 
    # save time of arrival
    while GPIO.input(echo_two) == 1:
        StopTime_two = time.time()

    # time difference between start and arrival
    TimeElapsed_two = StopTime_two - StartTime_two
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance_two = (TimeElapsed_two * 34300) / 2
 
    return distance_two
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            dist_two = distance_two()
            print ("D_one = %.2f cm  " "D_two = %.2f cm"% (dist, dist_two))
            time.sleep(0.1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
