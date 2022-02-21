import RPi.GPIO as GPIO
import time
import random
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
'''GPIO.setup(4,GPIO.OUT)
GPIO.setup(2,GPIO.OUT)
for i in range(5):
    GPIO.output(4,GPIO.HIGH)
    GPIO.output(2,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(4,GPIO.LOW)
    GPIO.output(2,GPIO.LOW)'''
pins=[4,17,22]

GPIO.setup(pins,GPIO.OUT)
'''for i in pins:
    GPIO.output(pins,GPIO.HIGH)
    time.sleep(1)
time.sleep(2)
for i in pins[::-1]:
    GPIO.output(i,GPIO.LOW)
    time.sleep(1)'''

'''for m in range(15):
    randpin=random.choice(pins)
    GPIO.output(randpin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(randpin,GPIO.LOW)
    time.sleep(0.5)'''

'''random.shuffle(pins)
for pin in pins:
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(0.5)
for pin in pins[::-1]:
    GPIO.output(pin,GPIO.LOW)
    time.sleep(0.5)'''

blinks=[0.5,1,1.5,2]
'''while True:
    for s in blinks:
        GPIO.output(4,GPIO.HIGH)
        time.sleep(s)
        GPIO.output(4,GPIO.LOW)
        time.sleep(0.5)
    for s in blinks[::-1]:
        GPIO.output(4,GPIO.HIGH)
        time.sleep(s)
        GPIO.output(4,GPIO.LOW)
        time.sleep(0.5)'''

'''def blinker(pin,blinktime,blinks):
    for s in range(blinks):
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(blinktime)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(0.7)
blinker(4,2,5)'''

'''GPIO.setup(14,GPIO.OUT)
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
light=1
while True:
    value=GPIO.input(22)
    if value==1:
        light=-light
        time.sleep(0.3)
    if light==1:
        GPIO.output(14,GPIO.HIGH)
    else: GPIO.output(14,GPIO.LOW)'''

'''GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
counter=0
while True:
    button1=GPIO.input(22)
    button2=GPIO.input(18)
    if button1==1:
        counter+=1
        time.sleep(0.3)
    if counter==2:
        if button2==1:
            for i in range(10):
                counter=0
                GPIO.output(14,GPIO.HIGH)
                time.sleep(0.3)
                GPIO.output(14,GPIO.LOW)
                time.sleep(0.3)    
    else:
        GPIO.output(14,GPIO.LOW)'''

#traffic light system
'''pins=[14,15,18,25,8,7]
GPIO.setup(pins,GPIO.OUT)
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
while True:
    button=GPIO.input(22)
    GPIO.output(14,GPIO.HIGH)
    GPIO.output(7,GPIO.HIGH)
    if button==1:
        #hyde street
        GPIO.output(14,GPIO.LOW)
        GPIO.output(15,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(15,GPIO.LOW)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(4)
        GPIO.output(18,GPIO.LOW)
        GPIO.output(14,GPIO.HIGH)
        
        #lombard street
        time.sleep(1)
        GPIO.output(7,GPIO.LOW)
        GPIO.output(25,GPIO.HIGH)
        time.sleep(3)
        GPIO.output(25,GPIO.LOW)
        GPIO.output(8,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(8,GPIO.LOW)
        GPIO.output(7,GPIO.HIGH)'''
import threading

pins=[14,24,18]
GPIO.setup(pins,GPIO.OUT)
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

'''cycle=False
x=0
def blinker():
    global cycle,pins,x
    while cycle==True:
        GPIO.output(pins[x],GPIO.LOW)
        print(x)
        x+=1
        if x==3:
            x=0
        GPIO.output(pins[x],GPIO.HIGH)
        time.sleep(0.5)
          
while True:
    button=GPIO.input(22)
    if button==1 and cycle==False:
        cycle=True
        thread1=threading.Thread(target=blinker)
        thread1.start()
        time.sleep(0.2)
    elif button==1 and cycle==True:
        time.sleep(0.2)
        cycle=False
        thread1.join()'''

'''green = GPIO.PWM(14,50)
yellow= GPIO.PWM(24,25)
blue= GPIO.PWM(18,16)
green.start(50)
blue.start(50)
yellow.start(50)
time.sleep(10)
blue.stop()
yellow.stop()
green.stop()'''
'''blue.start(50)
while True:
    for i in range(10,90,5):
        blue.ChangeFrequency(i)
        time.sleep(1)
    for m in range(90,10,-5):
        blue.ChangeFrequency(m)
        time.sleep(1)'''
'''yellow.start(30)
cycle=False
while True:
    button=GPIO.input(22)
    if button==1 and cycle==False:
        yellow.ChangeDutyCycle(60)
        time.sleep(0.2)
        cycle=True
    elif button==1 and cycle==True:
        yellow.ChangeDutyCycle(30)
        time.sleep(0.2)
        cycle=False'''

'''green = GPIO.PWM(14,50)
red= GPIO.PWM(24,50)
blue= GPIO.PWM(18,50)
red.start(0)
blue.start(0)
green.start(0)
redx=0
bluex=0
greenx=0
while True:
    for r in range(100):
        red.ChangeDutyCycle(r)
        time.sleep(0.1)
    for b in range(100):
        blue.ChangeDutyCycle(b)
        time.sleep(0.1)
    for r in range(100,0,-1):
        red.ChangeDutyCycle(r)
        time.sleep(0.1)
    for g in range(100,0,-1):
        red.ChangeDutyCycle(r)
        time.sleep(0.1)
    break'''
#finish RGB bulb frequency modulation and mood lamp
GPIO.cleanup()

