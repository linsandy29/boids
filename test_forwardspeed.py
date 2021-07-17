import RPi.GPIO as GPIO          
from time import sleep

in1 = 24
in2 = 23
en = 25
in3 = 17
in4 = 27
en2 = 22
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)
p.start(50)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
pp=GPIO.PWM(en2,1000)
pp.start(50)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):

    x=input()
    
    if x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='a':
        print("1")
        p.ChangeDutyCycle(30)
        pp.ChangeDutyCycle(30)
        x='z'

    elif x=='b':
        print("2")
        p.ChangeDutyCycle(40)
        pp.ChangeDutyCycle(40)
        x='z'

    elif x=='c':
        print("3")
        p.ChangeDutyCycle(50)
        pp.ChangeDutyCycle(50)
        x='z'

    elif x=='d':
        print("4")
        p.ChangeDutyCycle(60)
        pp.ChangeDutyCycle(60)
        x='z'

    elif x=='e':
        print("5")
        p.ChangeDutyCycle(70)
        pp.ChangeDutyCycle(70)
        x='z'

    elif x=='E':
        GPIO.cleanup()
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
