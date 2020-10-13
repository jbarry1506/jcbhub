#!/usr/bin/python3

from time import sleep
from picamera import PiCamera
import shutil
# import jenkins
import pprint
import vars

# detect button push
# display countdown on screen
# trigger logic power
    # 10 seconds
    # strobe light
# trigger camera
# trigger pennywise servo
# trigger sound effect
# trigger candy drop
# move file
# start jenkins build
# reset Pennywise
# display website


def display_webpage():
    pass


def button_detect():
    pass


def logic_switch():
    pass


def snap_pic():
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture('/home/pi/Pictures/PiCam/latest.jpg')


def countdown():
    pass


def candy_drop():
    pass


def pennywise():
    pass


def sound_effect():
    pass


def move_file():
    shutil.move("/home/pi/Pictures/PiCam/latest.jpg", "/home/pi/Code/jcbhub/latest.jpg")


def jenkins_build():
    pass


def reset_pennywise():
    pass


snap_pic()
move_file()
# server = jenkins.Jenkins(vars.jenkins_server, username=vars.jenkins_user, password=vars.jenkins_password)
# pprint.pprint(server.get_all_jobs())
