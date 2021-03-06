#!/usr/bin/env python2
#Libraries
import rospy
from std_msgs.msg import Float32MultiArray
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
trig_one = 17
echo_one = 18
trig_two = 23
echo_two = 24
trig_three = 27
echo_three = 22
trig_four = 19
echo_four = 26
trig_five = 20
echo_five = 21
 
#set GPIO direction (IN / OUT)
GPIO.setup(trig_one, GPIO.OUT)
GPIO.setup(echo_one, GPIO.IN)
GPIO.setup(trig_two, GPIO.OUT)
GPIO.setup(echo_two, GPIO.IN)
GPIO.setup(trig_three, GPIO.OUT)
GPIO.setup(echo_three, GPIO.IN)
GPIO.setup(trig_four, GPIO.OUT)
GPIO.setup(echo_four, GPIO.IN)
GPIO.setup(trig_five, GPIO.OUT)
GPIO.setup(echo_five, GPIO.IN)
 
def distance_one():

    # set Trigger to HIGH , after 0.01ms to LOW
    GPIO.output(trig_one, True)
    time.sleep(0.00001)
    GPIO.output(trig_one, False)
 
    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(echo_one) == 0:
        StartTime = time.time()
 
    while GPIO.input(echo_one) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def distance_two():

    GPIO.output(trig_two, True)
    time.sleep(0.00001)
    GPIO.output(trig_two, False)
 
    StartTime_two = time.time()
    StopTime_two = time.time()

    while GPIO.input(echo_two) == 0:
        StartTime_two = time.time()
 
    while GPIO.input(echo_two) == 1:
        StopTime_two = time.time()

    TimeElapsed_two = StopTime_two - StartTime_two
    distance_two = (TimeElapsed_two * 34300) / 2
 
    return distance_two

def distance_three():

    GPIO.output(trig_three, True)
    time.sleep(0.00001)
    GPIO.output(trig_three, False)
 
    StartTime_three = time.time()
    StopTime_three = time.time()

    while GPIO.input(echo_three) == 0:
        StartTime_three = time.time()
 
    while GPIO.input(echo_three) == 1:
        StopTime_three = time.time()

    TimeElapsed_three = StopTime_three - StartTime_three
    distance_three = (TimeElapsed_three * 34300) / 2
 
    return distance_three

def distance_four():

    GPIO.output(trig_four, True)
    time.sleep(0.00001)
    GPIO.output(trig_four, False)
 
    StartTime_four = time.time()
    StopTime_four = time.time()

    while GPIO.input(echo_four) == 0:
        StartTime_four = time.time()
 
    while GPIO.input(echo_four) == 1:
        StopTime_four = time.time()

    TimeElapsed_four = StopTime_four - StartTime_four
    distance_four = (TimeElapsed_four * 34300) / 2
 
    return distance_four

def distance_five():

    GPIO.output(trig_five, True)
    time.sleep(0.00001)
    GPIO.output(trig_five, False)
 
    StartTime_five = time.time()
    StopTime_five = time.time()

    while GPIO.input(echo_five) == 0:
        StartTime_five = time.time()
 
    while GPIO.input(echo_five) == 1:
        StopTime_five = time.time()

    TimeElapsed_five = StopTime_five - StartTime_five
    distance_five = (TimeElapsed_five * 34300) / 2
 
    return distance_five

def ultra_sensors():
    pub = rospy.Publisher('ultra_sensors',Float32MultiArray, queue_size=1)
    rospy.init_node('ultra_sensors', anonymous=True)
    rate = rospy.Rate(5) 
    #array = [23.0, 22.3, 3.2, 55.6, 12.4]

    while not rospy.is_shutdown():
        d_one = distance_one()
        d_two = distance_two()
        d_three = distance_three()
        d_four = distance_four()
        d_five = distance_five()
        array = [d_one, d_two, d_three, d_four, d_five]
        ultra_str = Float32MultiArray(data = array)
        rospy.loginfo(ultra_str)
        pub.publish(ultra_str)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        ultra_sensors()

    except rospy.ROSInterruptException:
        pass

