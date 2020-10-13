#!/usr/bin/python3

import shutil
import jenkins
import pprint
import vars

# detect button push
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

# shutil.move("/home/pi/Pictures/PiCam/teststill_gomiami.jpg", "/home/pi/Code/jcbhub/latest.jpg")


def button_detect():
    pass


def logic_switch():
    pass


def snap_pic():
    pass


def candy_drop():
    pass


def pennywise():
    pass


def sound_effect():
    pass


def move_file():
    pass


def jenkins_build():
    pass


def reset_pennywise():
    pass


server = jenkins.Jenkins(vars.jenkins_server, username=vars.jenkins_user, password=vars.jenkins_password)
pprint.pprint(server.get_all_jobs())
