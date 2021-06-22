import smtplib
import time
import math
import datetime
from setup import sender, pw


def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    subject = "Trial is about to expire"
    message = 'Subject: {}\n\n{}'.format(subject, final)


    try:
        server.login(sender, pw)
        print("Login success")

    except:
        print("Error logging in")

    try:
        server.sendmail(sender, sender, message)
        print("Email has been sent to",sender)
        print('Sent email at: %s\n' % time.ctime())


    except:
        print("Error sending email to",sender)




d = datetime.datetime.now()
dateNow = str(d.strftime("%x"))

f = open("date.txt", "r")
dateTrial = f.readline()
f = open("trial.txt", "r")
trialName = f.readline()
final = "Your "+trialName+" trial is about to expire"
print("date now:",dateNow)
print("trial end:",dateTrial)
print("trial name:",trialName)

if dateNow == dateTrial:
    sendEmail()
else:
    with open("error.txt", "w") as f:
        f.write("There has been an error")



