import requests
from random import choice
from string import ascii_lowercase
from colorama import Fore, Style
from datetime import date

class SendCall():
    # Change the githubusercontent.com links to change the wordlists that are going to be used for Name / Surname
    name = choice((requests.get("https://gist.githubusercontent.com/tolgarecep/251c7fcde01f9ea0a8f3883243c360a5/raw/4707ba1a669b32632ced646e302551bbfd5a904e/tr-names.txt").text).splitlines())
    surname = choice((requests.get("https://gist.githubusercontent.com/emrekgn/493304c6445de15657b2/raw/5ff32a4b0baa4999748d69650754243fd0fd6ed9/soyisimler").text).splitlines()).lower()
    datetoday =  date.today().strftime('%d-%m-%Y')
    adet = 0
    

    def __init__(self, phone, mail):
        self.phone = str(phone)
        if len(mail) != 0:
            self.mail = mail
        else:
            self.mail = ''.join(choice(ascii_lowercase) for i in range(19))+"@gmail.com"

    #porsche.com.tr
    def Porsche(self):
        try:
            url = "https://www.porsche.com.tr:443/biz-sizi-arayalim"
            data = {"firstname": self.ad, "lastname": self.soyad, "email": self.mail, "phone": self.phone, "dealer": "4830", "approved": "on", "contactapproved": "on"}
            r = requests.post(url, data=data, allow_redirects=False)
            if r.status_code == 302:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> porsche.com.tr")
                self.adet += 1
            else:
                raise 
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Status: Failed! --> porsche.com.tr")

    # Change the url and the details according to the website that you want to test.
    # You can add multiple blocks of code to test multiple websites.

  #  def Porsche(self):
       # try:
        #    url = "https://www.porsche.com.tr:443/biz-sizi-arayalim"
         #   data = {"firstname": self.ad, "lastname": self.soyad, "email": self.mail, "phone": self.phone, "dealer": "4830", "approved": "on", "contactapproved": "on"}
          #  r = requests.post(url, data=data, allow_redirects=False)
           # if r.status_code == 302:
            #    print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> porsche.com.tr")
             #   self.adet += 1
            # else:
             #   raise 
        # except:
          #  print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> porsche.com.tr")
            
    
   