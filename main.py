import smtplib
from email.mime.text import MIMEText
import requests
import re
import time


localtime = time.asctime(time.localtime(time.time()))

send_mail_time = time.strftime("%H%M", time.localtime())

mail_time = ['0900','1200','1500','1900','2400']


def send_mail(subject, mail_content):
    gmail_user = 'davidh19940110@gmail.com'
    gmail_password = '' # your gmail password

    msg = MIMEText(mail_content)
    msg['Subject'] = subject
    msg['From'] = gmail_user
    msg['To'] = 'davidh83110@gmail.com'

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.send_message(msg)
        server.quit()
        print('Email sent !'+'\n'+mail_content)
        
    except:
        print('Email send failed')


    

def check_portal():
    portal_url = 'https://portal.admm.co/login/'
    
    res_portal = requests.get(portal_url)

    find_index = re.findall('title', str(res_portal.text))
    
    if find_index != []:
        print(localtime + "  portal success")
        
        if send_mail_time in mail_time:
            send_mail("Portal Check Status 'ok' ", "Check portal status is ok !" + "\n" + localtime + "\n\n" + res_portal.text[50:500])
        else:
            pass
        
        return("succeed")
    
    else:
        send_mail("Portal Check FAILED !", "Check Portal FAILED ! " + localtime + "\n\n" + res_portal.text)
        return("failed")
        

def check_redirect():
    redirect_url = 'https://admm.co/status.json'
    
    res_redirect = requests.get(redirect_url)
    
    find_test = re.findall('ok', str(res_redirect.text))
    
    if find_test != []:
        print(localtime + "  redirect success")
        
        if send_mail_time in mail_time:
            send_mail("Redirect Check Status 'ok' ", "Check Redirect status is ok !" + "\n" + localtime + "\n\n" + res_redirect.text)
        else:
            pass
        
        return("succeed")
    else:
        send_mail("Redirect Check FAILED !", "Check Redirect FAILED !" + localtime + "\n\n" + res_redirect.text)
        return("failed")
    
    
if __name__ == '__main__':
    check_portal()
    check_redirect()
        
