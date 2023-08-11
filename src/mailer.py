import smtplib

from utilities.varaibles import var

smtp_host = var.smtp_host
smtp_port = int(var.smtp_port)
user = var.email_sender
passw = var.email_sender_password
receiver = ",".join([i for i in var.email_receivers])

def send_mail(): 
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.connect(smtp_host,smtp_port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(user, passw)

    server.sendmail(user,receiver,"mail try2")