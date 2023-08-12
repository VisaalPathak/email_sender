from src.mailer import Mailer

if __name__=="__main__":
    mailer = Mailer()
    mail = mailer.create_mail()
    file_dir = "./data/"
    mail = mailer.attach_files(file_dir,mail)
    mailer.send_mail(receiver=mailer.receiver,msg=mail)