#!/usr/bin/env python2
#Libraries
import rospy
import time 
from std_msgs.msg import Float32MultiArray
import RPi.GPIO as GPIO
from time import sleep


speed = 0
angle = 0
stop = 0
sight = 0

temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

def callback(data):
    global speed,angle,stop,sight
    speed = data.data[0]
    angle = data.data[1]
    stop = data.data[2]
    sight = data.data[3]
    showled()
    #rospy.loginfo('%.2f %.2f %.0f %.0f', data.data[0],data.data[1],data.data[2],data.data[3])
    rospy.loginfo('%.2f %.2f %.0f %.0f', speed,angle,stop,sight)

def listener():

    rospy.init_node('motor_control', anonymous=True)

    rospy.Subscriber('RobotData', Float32MultiArray, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def showled():
    global speed,angle,stop,sight
    
    if stop == 0 and sight == 0:
        GPIO.output(18,GPIO.HIGH)
        #print ("led on")

    else:
        GPIO.output(18,GPIO.LOW)
    
        
if __name__ == '__main__':
    try:
        listener()
        
    except rospy.ROSInterruptException:
        pass

