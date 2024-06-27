import smtplib
import ssl
from smtplib import (
    SMTPException , 
    SMTPAuthenticationError 
)

class SpamReport:
    count_emails = 0
    true_send = 0
    false_send = 0
    
    def __init__(self , file_name:str , text:str , send_to:str ):
        self.file_ = file_name
        self.text = text
        self.target = send_to
    
    def readfile(self) -> list:
        email_list = open(self.file_ ,'r').read().split('\n')
        self.count_emails = len(email_list) 
        return email_list
                
    def context(self):
        return ssl.create_default_context()
    
    def send_gmail(self) -> bool:
        for self.Gmail_pass in self.readfile():
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=self.context()) as self.gmail_:
                try:
                    self.gmail_.login(self.Gmail_pass.split(':')[0], self.Gmail_pass.split(":")[1])
                    self.gmail_.sendmail(self.Gmail_pass.split(':')[0], self.target, self.text)
                    self.gmail_.quit()
                    self.true_send += 1
                except SMTPAuthenticationError:
                    self.false_send += 1
                except SMTPException:
                    self.false_send += 1
        return True
        
        
    def send_yahoo(self) -> bool:
        for self.Yahoo_Pass in self.readfile:
            with smtplib.SMTP('smtp..mail.yahoo.com' , 465) as self.yahoo_:
                try:
                    self.yahoo_.login(self.yahoo_.split(':')[0], self.yahoo_.split(':')[1])
                    self.yahoo_.sendmail(self.yahoo_.split(':')[0], self.target, self.text)
                    self.yahoo_.quit()
                    self.true_send += 1
                except SMTPAuthenticationError:
                    self.false_send += 1
                except SMTPException:
                    self.false_send += 1
        return True


    def __enter__(self):
           return self
       
    def __exit__(self, *args, **kwargs):
           return    

