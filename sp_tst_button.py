import RPi.GPIO as GPIO

# Sets pin numbering scheme to BCM
GPIO.setmode(GPIO.BCM) 
# Logic output pin for the power strip (positive). Other power strip wire will go to GND.
GPIO.setup(16, GPIO.OUT) 
# Input from pushbutton, using internal pulldown resistor. Other button wire will connect to 5V pin. 
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_UP) 

if GPIO.input(12) == 0:
    print("Button Pusher!  Button Pusher!")
