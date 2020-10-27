#!/usr/bin/python3

from time import sleep
from picamera import PiCamera
import RPi.GPIO as GPIO
import datetime, shutil, subprocess, os
import vars

# trigger pennywise servo
# trigger sound effect
# trigger candy drop
# move file


# Sets pin numbering scheme to BCM
GPIO.setmode(GPIO.BCM) 
# Logic output pin for the power strip (positive). Other power strip wire will go to GND.
GPIO.setup(16, GPIO.OUT) 
# Input from pushbutton, using internal pulldown resistor. Other button wire will connect to 5V pin. 
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_UP) 
original_pic_location = "/home/pi/Pictures/PiCam/latest.jpg"
final_file_location = "/home/pi/Code/jcbhub/latest.jpg"
# set up camera
camera = PiCamera()
camera.resolution = (1024, 768)


# signal to execute the rest of the program
def button_press():
    print("button pressed")
    camera.start_preview()
    logic_switch()
    # Camera warm-up time
    sleep(2)


# turn off 'normally on' 
# turn on 'normally off'
def logic_switch():
    print("logic switch activated")
    GPIO.output(16,1)
    sound_effect()
    camera.capture('/home/pi/Pictures/PiCam/latest.jpg')  
    sleep(2)


def snap_pic():
    camera.capture('/home/pi/Pictures/PiCam/latest.jpg')


def candy_drop():
    # triggered from button_press
    pass


def pennywise():
    # triggered from button_press
    pass


def sound_effect():
    os.system("aplay ./sounds/scream.wav")


def move_file(move_from, move_to):
    shutil.move(move_from, move_to)


def reset_pennywise():
    pass


def push_pic():
    current_time = str(datetime.datetime.now)
    commit_message = "commit -m 'latest"+current_time
    print(commit_message)

    subprocess.call(["git", "add", "-A"])
    subprocess.call(["git", "commit", "-m", commit_message])
    subprocess.call(["git", "push"])


def reset():
    pass


# initialize pyglet needs to happen before the rest of the program
# global vars
# no buttons have been pressed, yet
pressed = 0
# set up threads
# order as follows
    # logic_switch()
    # sound_effect()
    # snap_pic()
    # sound_effect()

camera.start_preview()
# Camera warm-up time
sleep(2)

try:
    while True:
        for _ in range(2):
            sleep(1)
            pressed = GPIO.input(12)
        if GPIO.input(12) == 0:
            # pressed = 1
            # button_press()
            print("button pressed")
            logic_switch()
            sound_effect()
            move_file(original_pic_location, final_file_location)
            # sleep(2)
            push_pic()
        elif pressed == 1:
            GPIO.output(16,0)
            print("Button released")
            pressed = 0
except KeyboardInterrupt:
    # clean up settings
    GPIO.cleanup()


# email_picture(final_file_location)
# server = jenkins.Jenkins(vars.jenkins_server, username=vars.jenkins_user, password=vars.xv)
# pprint.pprint(server.get_all_jobs())
# display_webpage()

