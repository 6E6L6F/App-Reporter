import smtplib
import ssl
import time

class SpamReport:
    def __init__(self , File_name:str , Text:str , Send_to:str ):
        self.File_ = File_name
        self.Text = Text
        self.Target = Send_to
    
    def __ReadFile__(self) -> list:
            try:
                return open(self.File_ ,'r').read().split('\n') 
            
            except FileNotFoundError as NF:
                raise "File Not Found : " + NF
            
            except KeyboardInterrupt as Key:
                raise "Cancel With " + Key
    def __Context__(self) -> 'ssl':
        return ssl.create_default_context()
    
    def SendWithGmail(self) -> bool:
        try:                
            for self.Gmail_pass in self.__ReadFile__():
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=self.__Context__()) as self.Gmail_:
                    self.Gmail_.login(self.Gmail_pass.split(':')[0], self.Gmail_pass.split(":")[1])
                    self.Gmail_.sendmail(self.Gmail_pass.split(':')[0], self.Target, self.Text)
                    print(f"Send Report With {self.Gmail_pass.split(':')[0]}")
                    self.Gmail_.quit()
            return True
        
        except Exception as ex:
            raise "Exception Error : " + ex

        except KeyboardInterrupt as Key:
            raise "Cancel Send Meil With : " + Key

        except TimeoutError as To:
            raise "Timeout Error : " + To
        
        except:
            return False
    def SendWithYahoo(self) -> bool:
        try:
            for self.Yahoo_Pass in self.__ReadFile__():
                with smtplib.SMTP('smtp..mail.yahoo.com' , 465) as self.Yahoo_:
                    self.Yahoo_.login(self.Yahoo_Pass.split(':')[0], self.Yahoo_Pass.split(':')[1])
                    self.Yahoo_.sendmail(self.Yahoo_Pass.split(':')[0], self.Target, self.Text)
                    print(f"Send Report With {self.Yahoo_Pass.split(':')[0]}")
                    self.Yahoo_.quit()
            return True

        except Exception as ex:
            raise "Exception Error : " + ex

        except KeyboardInterrupt as Key:
            raise "Cancel Send Meil With : " + Key

        except TimeoutError as To:
            raise "Timeout Error : " + To
        
        except:
            return False
    
    def __enter__(self) -> 'SpamReport':
           return self
       
    def __exit__(self, *args, **kwargs):
           return    

