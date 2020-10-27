# from email.mime.multipart import MIMEMultipart 
# from email.mime.text import MIMEText 
# from email.mime.base import MIMEBase 
# from email import encoders 

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