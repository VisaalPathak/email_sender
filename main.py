from src.mailer import Mailer

if __name__=="__main__":
    mailer = Mailer()
    mail = mailer.create_mail()
    file_path = "./data/dummy.txt"
    mail = mailer.attach_files(file_path,mail)
    mailer.send_mail(receiver=mailer.receiver,msg=mail)