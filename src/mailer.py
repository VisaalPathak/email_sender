import smtplib

smtp_host = "smtp.gmail.com"
smtp_port = 587
user = "your_email_address"
passw = "your_password"
receiver = "receiver_email_address"

server = smtplib.SMTP(smtp_host, smtp_port)
server.connect(smtp_host,smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(user, passw)

server.sendmail(user,receiver,"mail try2")