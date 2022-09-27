import ssl

print("Day 16 Sending email\n")

print("SMPT")
"""Simple Mail Transfer Protocol (SMTP) is a protocol, which handles sending an e-mail and routing 
e-mail between mail servers."""

"""Python provides smtplib module, which defines an SMTP client session object that can be used to 
   send mails to any Internet machine with an SMTP or ESMTP listener daemon."""

# smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] ) syntax

import smtplib
from email.message import EmailMessage

sender = 'sender@gmail.com'
pasw =  'password'

receiver = 'receiver@gmail.com' # receiver's email
subject = "message from python 🙄"

body = "this email is from python"

em = EmailMessage()
em['From'] = sender
em['To'] = receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465, context = context) as smtp:
    smtp.login(sender, pasw)
    smtp.sendmail(sender, receiver, em.as_string())