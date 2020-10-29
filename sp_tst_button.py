import RPi.GPIO as GPIO

# Sets pin numbering scheme to BCM
GPIO.setmode(GPIO.BCM)
# Logic output pin for the power strip (positive). Other power strip wire will go to GND.
GPIO.setup(16, GPIO.OUT)
# Input from pushbutton, using internal pulldown resistor. Other button wire will connect to 5V pin. 
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_UP)

print(GPIO.input(26))
while True:
    if GPIO.input(26) == 0:
        print("Button Pusher!  Button Pusher!")
    elif GPIO.input(26) == 1:
        GPIO.output(16,0)
        print("Button released")
        pressed = 0
