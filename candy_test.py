#!/usr/bin/python3

from time import sleep
from picamera import PiCamera
import RPi.GPIO as GPIO
import datetime, smtplib, shutil, subprocess, pprint, sys, os
# from email.mime.multipart import MIMEMultipart 
# from email.mime.text import MIMEText 
# from email.mime.base import MIMEBase 
# from email import encoders 
import webbrowser
# unable to import Jenkins on rpi - insecure request warning
# import jenkins
import vars


# trigger camera
# trigger pennywise servo
# trigger sound effect
# trigger candy drop
# move file
# start jenkins build
# reset Pennywise
# display website

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


# display webpage not working on pi
def display_webpage():
    # doesn't appear to work in python 3.4
    webbrowser.open_new("https://jcbhub.com")


# signal to execute the rest of the program
def button_press():
    print("button pressed")
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    for r in range(2):
        sound_effect()
    logic_switch()
    snap_pic()


# turn off 'normally on' 
# turn on 'normally off'
def logic_switch():
    print("logic switch activated")
    GPIO.output(16,1)
    sleep(2)


def snap_pic():
    camera.capture('/home/pi/Pictures/PiCam/latest.jpg')
    camera.stop_preview()
    camera.close()


# taking this funciton out because picture is showing up as text.
def email_picture(fl):
    # fl = file location
    em = vars.em
    pw = vars.xv

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(em, pw)
    except Exception as e:
        print('Something went wrong with Login.')
        print(e)

    try:
        server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server_ssl.ehlo()   # optional
        # ...send emails
    except Exception as e:
        print('Something went wrong in SSL')
        print(e)

# https://www.geeksforgeeks.org/send-mail-attachment-gmail-account-using-python/
#-------------------------------------------------------------------------------
    
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    
    # storing the senders email address   
    msg['From'] = em
    # storing the receivers email address  
    msg['To'] = em 
    # storing the subject  
    msg['Subject'] = "Scaredy-Pi"
    # string to store the body of the mail 
    body = "WE GOT ONE!!!"
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    # open the file to be sent  
    filename = fl
    attachment = open(fl, "rb") 
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    # encode into base64 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    
    # sending the mail 
    # s.sendmail(fromaddr, toaddr, text) 

#-------------------------------------------------------------------------------
    email_text = ("""\
    From: {}
    To: {}
    Subject: {}

    {}
    """).format(em, ", ".join(em), msg['Subject'], text)

    try:
        server.sendmail(em, em, email_text)
        server.close()

        print('Email sent!')
    except Exception as e:
        print("The email wasn't sent.")
        print(e)
    
    # terminating the session 
    server.quit() 


# removed due to loop functionality errors
def countdown():
    # triggered from button press
    pass


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


def jenkins_build():
    pass


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

try:
    while True:
        if GPIO.input(12) == 0:
            pressed = 1
            button_press()
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

