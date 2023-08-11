from src.mailer import Mailer

if __name__=="__main__":
    mailer = Mailer()
    mail = mailer.create_mail()
    for user in mailer.receiver:
        mailer.send_mail(receiver=user,msg=mail)