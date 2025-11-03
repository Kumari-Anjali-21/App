from flask_mail import*

class Email:
    def __init__(self,app):
        #---------------------mail configuration-----------------
        app.config["MAIL_SERVER"]='smtp.gmail.com'
        app.config["MAIL_PORT"]='587'
        app.config["MAIL_USERNAME"]= 'anjalirwc@gmail.com'
        app.config["MAIL_PASSWORD"]= 'ribo wfsj hpgy cpwp'
        app.config["MAIL_USE_TLS"]= True
        app.config["MAIL_USE_SSL"]= False
        self.mail = Mail(app)     #mail object

    def compose_mail(self,subject,email,message):
        msg=Message(subject,sender='anjalirwc@gmail.com',recipients=[email])
        msg.html=message
        self.mail.send(msg)
