import RPi.GPIO as GPIO
import time
import random
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(1,GPIO.OUT)

def forward(t):
    GPIO.output(14,0)
    GPIO.output(1,0)
    #forward - 18 and 7
    GPIO.output(18,1)
    GPIO.output(7,1)
    time.sleep(t)
def stop():
    GPIO.output(14,0)
    GPIO.output(18,0)
    GPIO.output(7,0)
    GPIO.output(1,0)
def backward(t):
    GPIO.output(14,1)
    GPIO.output(1,1)
    GPIO.output(18,0)
    GPIO.output(7,0)
    time.sleep(t)
def slow(t):
   n=GPIO.PWM(18,10)
   n.start(15)
   print("slow")
   time.sleep(t)
   n.stop()
def fast(t):
    x=GPIO.PWM(18,90)
    x.start(50)
    print("fast")
    time.sleep(t)
    x.stop()

forward(1)
backward(0.5)
stop()
GPIO.cleanup()