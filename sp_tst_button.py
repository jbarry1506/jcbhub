import RPi.GPIO as GPIO

# Sets pin numbering scheme to BCM
GPIO.setmode(GPIO.BCM) 
# Logic output pin for the power strip (positive). Other power strip wire will go to GND.
GPIO.setup(16, GPIO.OUT) 
# Input from pushbutton, using internal pulldown resistor. Other button wire will connect to 5V pin. 
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_UP) 

<<<<<<< HEAD
if GPIO.input(12) == 0:
    print("Button Pusher!  Button Pusher!")
=======
while True:
    if GPIO.Input(12) == 0:
        print("Button Pusher!  Button Pusher!")
>>>>>>> 6d0214e096169e43f38b4aa58d9a6daa3bbf4813
