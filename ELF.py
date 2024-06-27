import smtplib
import ssl
import time

class SpamReport:
    def __init__(self , File_name:str , Text:str , Send_to:str ):
        self.File_ = File_name
        self.Text = Text
        self.Target = Send_to
    
    def readfile(self) -> list:
            try:
                return open(self.File_ ,'r').read().split('\n') 
            
            except FileNotFoundError:
                raise FileNotFoundError("File Not Found In Dircetory")
            
            except KeyboardInterrupt:
                exit(0)
                
    def context(self):
        return ssl.create_default_context()
    
    def SendWithGmail(self) -> bool:
        try:                
            for self.Gmail_pass in self.readfile():
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=self.context()) as self.Gmail_:
                    self.Gmail_.login(self.Gmail_pass.split(':')[0], self.Gmail_pass.split(":")[1])
                    self.Gmail_.sendmail(self.Gmail_pass.split(':')[0], self.Target, self.Text)
                    print(f"Send Report With {self.Gmail_pass.split(':')[0]}")
                    self.Gmail_.quit()
            return True
        
        except Exception:
            raise  Exception("Error")

        except KeyboardInterrupt:
            exit(0)

        except TimeoutError as To:
            raise TimeoutError("please check your connections internet")
        
    def SendWithYahoo(self) -> bool:
        try:
            for self.Yahoo_Pass in self.readfile:
                with smtplib.SMTP('smtp..mail.yahoo.com' , 465) as self.Yahoo_:
                    self.Yahoo_.login(self.Yahoo_Pass.split(':')[0], self.Yahoo_Pass.split(':')[1])
                    self.Yahoo_.sendmail(self.Yahoo_Pass.split(':')[0], self.Target, self.Text)
                    print(f"Send Report With {self.Yahoo_Pass.split(':')[0]}")
                    self.Yahoo_.quit()
            return True

        except Exception:
            raise  Exception("Error")

        except KeyboardInterrupt:
            exit(0)

        except TimeoutError:
            raise TimeoutError("please check your connections internet")
    
    def __enter__(self):
           return self
       
    def __exit__(self, *args, **kwargs):
           return    

