import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

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
        msg['subject'] = "Email Sending Tutorial"
        msg['from'] = self.user
        msg['to'] = ",".join([i for i in self.receiver])

        html_content = """<p>Dear Sir/Madam,<br>\
            This is a dummy message sent to you."""
        part = MIMEText(html_content,'html')
        msg.attach(part)
        
        return msg
        
    def attach_files(self, file_path, msg):
        files = os.listdir(file_path)
        for i in files:
            file_addr = os.path.join(file_path,i)
            with open(file_addr, 'rb') as file:
                p = MIMEApplication(file.read())
                p.add_header('Content-Disposition',f"attachment; filename={file_addr.split('/')[-1]}")
                msg.attach(p)
            
        return msg

    def send_mail(self, receiver,msg): 
        server = smtplib.SMTP(self.smtp_host, self.smtp_port)
        server.connect(self.smtp_host,self.smtp_port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.user, self.passw)

        server.sendmail(self.user,receiver,msg.as_string())