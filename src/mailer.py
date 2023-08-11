import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from utilities.varaibles import var

class Mailer:
    smtp_host = var.smtp_host
    smtp_port = int(var.smtp_port)
    user = var.email_sender
    passw = var.email_sender_password
    receiver = var.email_receivers
    # print(receiver)

    def create_mail(self):
        msg = MIMEMultipart()
        msg['subject'] = "Dummy Email Sending Tutorial"
        msg['from'] = self.user
        msg['to'] = ",".join([i for i in self.receiver])

        html_content = """<p>Dear Sir/Madam,<br>\
            This is a dummy message sent to you."""
        part = MIMEText(html_content,'html')
        msg.attach(part)
        
        return msg
        
        

    def send_mail(self, receiver,msg): 
        server = smtplib.SMTP(self.smtp_host, self.smtp_port)
        server.connect(self.smtp_host,self.smtp_port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.user, self.passw)

        server.sendmail(self.user,receiver,msg.as_string())