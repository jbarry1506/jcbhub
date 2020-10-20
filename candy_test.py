#!/usr/bin/python3

from time import sleep
from picamera import PiCamera
import datetime, smtplib, shutil, subprocess, pprint
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import webbrowser
# unable to import Jenkins on rpi - insecure request warning
# import jenkins
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
    webbrowser.open_new("https://jcbhub.com")


def button_detect():
    # detect input from button
    # signal to execute the rest of the program
    pass


def logic_switch():
    # turn off 'normally on' 
    # turn on 'normally off'
    pass


def snap_pic():
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture('/home/pi/Pictures/PiCam/latest.jpg')


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


def countdown():
    # triggered from button detect
    pass


def candy_drop():
    # triggered from button_detect
    pass


def pennywise():
    # triggered from button_detect
    pass


def sound_effect():
    pass


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
original_pic_location = "/home/pi/Pictures/PiCam/latest.jpg"
final_file_location = "/home/pi/Code/jcbhub/latest.jpg"

snap_pic()
move_file(original_pic_location, final_file_location)
# sleep(2)
push_pic()
email_picture(final_file_location)
# server = jenkins.Jenkins(vars.jenkins_server, username=vars.jenkins_user, password=vars.xv)
# pprint.pprint(server.get_all_jobs())
display_webpage()

