from django.core.mail import send_mail

def sendMail(subject,message,addressemail,recipient_list):
    send_mail(subject,message,addressemail,recipient_list) 