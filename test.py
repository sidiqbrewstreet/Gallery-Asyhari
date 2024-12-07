import requests, re, time, calendar, random, datetime, binascii, struct, base64, sys, os, pyotp, json, uuid

from colorama import Fore
from termcolor import colored
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
# from rich import print
from fake_email import Email
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
from Cryptodome import Random
from Cryptodome.Cipher import AES
from nacl.public import PublicKey, SealedBox

HeadersChangPicture = lambda token, p_pic_s : {"Host": "www.instagram.com", "Accept": "*/*", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://www.instagram.com", "X-CSRFToken": str(token),"X-Instagram-AJAX": "1013618137", "X-Requested-With": "XMLHttpRequest", "Content-Length": str(p_pic_s),"DNT": "1", "Connection": "keep-alive",}

def clear(): os.system('cls' if 'win' in sys.platform.lower() else 'clear')

class instagram:
    def __init__(self):
        self.ses = requests.Session()
        self.head_email = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Ua':'','Sec-Ch-Ua-Mobile':'?1','Sec-Ch-Ua-Platform':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Linux; Android 11; vivo 1918 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.0000.00 Mobile Safari/537.36'}
        
        version = random.randint(8, 12)
        build1  = random.randint(189999, 201217)
        build2  = random.randint(1, 9)
        ver1 = random.randint(90, 299)
        ver2 = random.randint(3800, 5000)
        ver3 = random.randint(100, 299)
        self.headers = {'Host': 'www.instagram.com','X-Ig-Www-Claim': '0','X-Requested-With': 'XMLHttpRequest','Sec-Ch-Prefers-Color-Scheme': 'dark','X-Ig-App-Id': '1217981644879628','User-Agent': 'Mozilla/5.0 (Linux; Android {}; DT{}C; Build/RKQ1.{}.00{}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{}.0.{}.{} Mobile Safari/537.36 Firefox-KiToBrowser/{}.0'.format(version, ver2, build1, build2, ver1, ver2, ver3, ver1),'Content-Type': 'application/x-www-form-urlencoded','Accept': '*/*','X-Asbd-Id': '129477','Origin': 'https://www.instagram.com','Sec-Fetch-Site': 'same-origin','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://www.instagram.com/accounts/signup/email/','Accept-Encoding': 'gzip, deflate','Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','Priority': 'u=1, i'}

    
    def jeda(self, x, msg):
        timers = int(x)
        while timers > 0:
            print(f'\rMenunggu {msg} Dalam {timers} Detik...  ', end='\r')
            time.sleep(1)
            timers -= 1

    def getname(self):
        print('\rGet Username  ', end='\r')
        soup = bs(str(self.ses.get('https://www.random-name-generator.com/indonesia').text), 'html.parser')
        nama_tags = soup.find_all('li', class_='nav-item')
        self.nama_list = []
        for tag in nama_tags:
            nama = tag.find('a').text.strip()
            self.nama_list.append(nama)
        name = random.choice(self.nama_list)
        self.username = f'{name[:3]}.{name}'.lower().replace(' ','') + str(random.randint(100, 89898))
        self.names = str(name)
        print(self.names)
        print()

    def get_email_10minute(self):
        print('\rGet Email              ', end='\r')
        req = bs(self.ses.get('https://10minutemail.net/m/?lang=id',headers=self.head_email,allow_redirects=True).content,'html.parser')
        self.ses_email = re.search('sessionid="(.*?)"',str(req)).group(1)
        self.tim_email = str(time.time()).replace('.','')[:13]
        dat = {'new':'1','sessionid':self.ses_email,'_':self.tim_email}
        pos = self.ses.post('https://10minutemail.net/address.api.php',data=dat,headers=self.head_email,allow_redirects=True).json()
        self.email  = pos['mail_get_mail']
        self.mail   = pos['mail_get_user']
        self.domain = pos['mail_get_host']
        self.cookie_email = '; '.join([str(x)+"="+str(y) for x,y in self.ses.cookies.get_dict().items()])
        print('Email :',self.email)
        print('')

    def get_code_10minutemail(self):
        try:
            print('\rGet Code OTP                           ', end='\n')
            print('')
            dat = {'new':'0','sessionid':self.ses_email,'_':self.tim_email}
            pos = self.ses.post('https://10minutemail.net/address.api.php',data=dat,headers=self.head_email,cookies={'cookie':self.cookie_email},allow_redirects=True).json()
            print(f'\r{pos}')
            self.code = re.search(r'(\d+) is your Instagram code', str(pos)).group(1)
            print('Code :',self.code)
            print('')
        except AttributeError as e:
            self.code = re.search(r'(\d+) adalah kode Instagram Anda', str(pos)).group(1)
        
    def GetData(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'id,en-US;q=0.7,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Alt-Used': 'www.instagram.com',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Priority': 'u=0, i',
        }

        response = self.ses.get('https://www.instagram.com/', headers=headers).text
        self.cookies = ";".join([key+"="+value.replace('"','') for key, value in self.ses.cookies.get_dict().items()])
        match = re.search(r'"InstagramPasswordEncryption",\[\],{"key_id":"(\d+)","public_key":"(.*?)","version":"(\d+)"', str(response))
        if match: self.key_id, self.pub_key, self.version = match.group(1), match.group(2), match.group(3)
        self.clienid = re.search(r'"machine_id":"(.*?)"',str(response)).group(1)
        self.csrf    = re.search(r'csrftoken=(.*?);', str(self.cookies)).group(1)
        self.claim   = re.search(r'"claim":"(.*?)"', str(response)).group(1)
    
    def encrypt_password(self):
        self.password = 'aws111@'
        key   = Random.get_random_bytes(32)
        iv    = bytes([0] * 12)
        times = int(datetime.datetime.now().timestamp())
        aes   = AES.new(key, AES.MODE_GCM, nonce=iv, mac_len=16)
        aes.update(str(times).encode('utf-8'))
        encrypted_password, cipher_tag = aes.encrypt_and_digest(self.password.encode('utf-8'))

        pub_key_bytes = binascii.unhexlify(str(self.pub_key))
        seal_box = SealedBox(PublicKey(pub_key_bytes))
        encrypted_key = seal_box.encrypt(key)

        encrypted = bytes([1,
                    int(self.key_id),
                    *list(struct.pack('<h', len(encrypted_key))),
                    *list(encrypted_key),
                    *list(cipher_tag),
                    *list(encrypted_password)])
        encrypted = base64.b64encode(encrypted).decode('utf-8')
        return (f'#PWD_INSTAGRAM_BROWSER:{self.version}:{times}:{encrypted}')
    
    def step1(self):
        headers = {
            'Host': 'www.instagram.com',
            'Sec-Ch-Ua-Platform': '"Android"',
            'X-Csrftoken': self.csrf,
            'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="131", "Google Chrome";v="131"',
            'Sec-Ch-Ua-Mobile': '?1',
            'X-Ig-App-Id': '1217981644879628',
            'X-Asbd-Id': '129477',
            'X-Requested-With': 'XMLHttpRequest',
            'Sec-Ch-Prefers-Color-Scheme': 'dark',
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
            'X-Ig-Www-Claim': self.claim,
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.instagram.com/accounts/signup/email/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Priority': 'u=1, i',
        }

        response = self.ses.get('https://www.instagram.com/api/v1/web/login_page/', cookies={'cookie': self.cookies}, headers=headers, allow_redirects=True).text
        print(response)
        print()

    def step2(self):
        headers = {
            'Host': 'www.instagram.com',
            'Sec-Ch-Ua-Platform': '"Android"',
            'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="131", "Google Chrome";v="131"',
            'Sec-Ch-Ua-Mobile': '?1',
            'X-Ig-App-Id': '1217981644879628',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Instagram-Ajax': '1018644775',
            'X-Csrftoken': self.csrf,
            'X-Asbd-Id': '129477',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
            'Sec-Ch-Prefers-Color-Scheme': 'dark',
            'X-Ig-Www-Claim': self.claim,
            'Origin': 'https://www.instagram.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.instagram.com/accounts/signup/email/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Priority': 'u=1, i',
        }
        
        data = {'email': self.email}

        response = self.ses.post('https://www.instagram.com/api/v1/web/accounts/check_email/', cookies={'cookie': self.cookies}, data=data, headers=headers, allow_redirects=True).text
        print(response)
        print()

    def step3(self):
        headers = {
            'Host': 'www.instagram.com',
            'Sec-Ch-Ua-Platform': '"Android"',
            'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="131", "Google Chrome";v="131"',
            'Sec-Ch-Ua-Mobile': '?1',
            'X-Ig-App-Id': '1217981644879628',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Instagram-Ajax': '1018644775',
            'X-Csrftoken': self.csrf,
            'X-Asbd-Id': '129477',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
            'Sec-Ch-Prefers-Color-Scheme': 'dark',
            'X-Ig-Www-Claim': self.claim,
            'Origin': 'https://www.instagram.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.instagram.com/accounts/signup/email/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Priority': 'u=1, i',
        }

        data = {
            'device_id': self.clienid,
            'email': self.email,
        }

        response = self.ses.post('https://www.instagram.com/api/v1/accounts/send_verify_email/', cookies={'cookie': self.cookies}, data=data, headers=headers, allow_redirects=True).text
        print(response)
        print()

    def step4(self):
        headers = {
            'Host': 'www.instagram.com',
            'Sec-Ch-Ua-Platform': '"Android"',
            'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="131", "Google Chrome";v="131"',
            'Sec-Ch-Ua-Mobile': '?1',
            'X-Ig-App-Id': '1217981644879628',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Instagram-Ajax': '1018644775',
            'X-Csrftoken': self.csrf,
            'X-Asbd-Id': '129477',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
            'Sec-Ch-Prefers-Color-Scheme': 'dark',
            'X-Ig-Www-Claim': self.claim,
            'Origin': 'https://www.instagram.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.instagram.com/accounts/signup/emailConfirmation/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Priority': 'u=1, i',
        }

        data = {
            'code': self.code,
            'device_id': self.clienid,
            'email': self.email,
        }

        response = self.ses.post('https://www.instagram.com/api/v1/accounts/check_confirmation_code/', cookies={'cookie': self.cookies}, data=data, headers=headers, allow_redirects=True).json()
        self.konfircode = response["signup_code"]
        print(response)
        print()

    def step5(self):
        headers = {
            'Host': 'www.instagram.com',
            'Sec-Ch-Ua-Platform': '"Android"',
            'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="131", "Google Chrome";v="131"',
            'Sec-Ch-Ua-Mobile': '?1',
            'X-Ig-App-Id': '1217981644879628',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Instagram-Ajax': '1018644775',
            'X-Csrftoken': self.csrf,
            'X-Asbd-Id': '129477',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
            'Sec-Ch-Prefers-Color-Scheme': 'dark',
            'X-Ig-Www-Claim': self.claim,
            'Origin': 'https://www.instagram.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.instagram.com/accounts/signup/name/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Priority': 'u=1, i',
        }

        data = {
            'enc_password': self.encrypt_password(),
            'email': self.email,
            'failed_birthday_year_count': '{}',
            'first_name': self.names,
            'username': '',
            'seamless_login_enabled': '1',
            'use_new_suggested_user_name': 'true',
        }

        response = self.ses.post('https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/', cookies={'cookie': self.cookies}, data=data, headers=headers, allow_redirects=True).text
        print(response)
        print()

    def step6(self):
        self.day = str(random.randint(1, 25))
        self.month = str(random.randint(1, 10))
        self.year  = str(random.randint(1998, 2005))
        headers = {
            'Host': 'www.instagram.com',
            # 'Content-Length': '23',
            'Sec-Ch-Ua-Platform': '"Android"',
            'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="131", "Google Chrome";v="131"',
            'Sec-Ch-Ua-Mobile': '?1',
            'X-Ig-App-Id': '1217981644879628',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Instagram-Ajax': '1018644775',
            'X-Csrftoken': self.csrf,
            'X-Asbd-Id': '129477',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
            'Sec-Ch-Prefers-Color-Scheme': 'dark',
            'X-Ig-Www-Claim': self.claim,
            'Origin': 'https://www.instagram.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.instagram.com/accounts/signup/birthday/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Priority': 'u=1, i',
        }

        data = {
            'day'  : self.day,
            'month': self.month,
            'year' : self.year,
        }

        response = self.ses.post('https://www.instagram.com/api/v1/web/consent/check_age_eligibility/', cookies={'cookie': self.cookies}, data=data, headers=headers, allow_redirects=True).text
        print(response)
        print()

    def step7(self):
        headers = {
            'Host': 'www.instagram.com',
            'Sec-Ch-Ua-Platform': '"Android"',
            'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="131", "Google Chrome";v="131"',
            'Sec-Ch-Ua-Mobile': '?1',
            'X-Ig-App-Id': '1217981644879628',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Instagram-Ajax': '1018644775',
            'X-Csrftoken': self.csrf,
            'X-Asbd-Id': '129477',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
            'Sec-Ch-Prefers-Color-Scheme': 'dark',
            'X-Ig-Www-Claim': self.claim,
            'Origin': 'https://www.instagram.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.instagram.com/accounts/signup/username/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Priority': 'u=1, i',
        }

        data = {'username': self.names}

        response = self.ses.post('https://www.instagram.com/api/v1/users/check_username/', cookies={'cookie': self.cookies}, data=data, headers=headers, allow_redirects=True).json()
        # self.username = response["username_suggestions"]["suggestions"][4]
        print(response)
        print()

    def step8(self):
        headers = {
            'Host': 'www.instagram.com',
            'Sec-Ch-Ua-Platform': '"Android"',
            'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="131", "Google Chrome";v="131"',
            'Sec-Ch-Ua-Mobile': '?1',
            'X-Ig-App-Id': '1217981644879628',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Instagram-Ajax': '1018644775',
            'X-Csrftoken': self.csrf,
            'X-Asbd-Id': '129477',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
            'Sec-Ch-Prefers-Color-Scheme': 'dark',
            'X-Ig-Www-Claim': self.claim,
            'Origin': 'https://www.instagram.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.instagram.com/accounts/signup/username/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Priority': 'u=1, i',
        }

        data = {
            'enc_password': self.encrypt_password(),
            'day': self.day,
            'email': self.email,
            'failed_birthday_year_count': '{}',
            'first_name': self.names,
            'month': self.month,
            'username': self.username,
            'year': self.year,
            'client_id': self.clienid,
            'seamless_login_enabled': '1',
            'tos_version': 'row',
            'force_sign_up_code': self.konfircode,
            # 'extra_session_id': '5oxdc6:1he7cf:6q5g2x',
        }

        response = self.ses.post('https://www.instagram.com/api/v1/web/accounts/web_create_ajax/', cookies={'cookie': self.cookies}, data=data, headers=headers, allow_redirects=True).text
        self.cookies = ";".join([key+"="+value.replace('"','') for key, value in self.ses.cookies.get_dict().items()])
        print(response)
        print()

    def step9(self):
        headers = {
            'Host': 'www.instagram.com',
            'Dpr': '1.2000000000000002',
            'Viewport-Width': '718',
            'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="131", "Google Chrome";v="131"',
            'Sec-Ch-Ua-Mobile': '?1',
            'Sec-Ch-Ua-Platform': '"Android"',
            'Sec-Ch-Prefers-Color-Scheme': 'dark',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'https://www.instagram.com/accounts/signup/username/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Priority': 'u=0, i',
        }

        response = self.ses.get('https://www.instagram.com/accounts/registered/', cookies={'cookie': self.cookies}, headers=headers, allow_redirects=True).text
        print('Sukses :', re.search(r'"username":"(.*?)"', str(response)).group(1))
        print('cookie :', self.cookies)
        print()

    def ChangePictire(self):
        self.__path__ = 'furina.jpg'
        p_pic_s = os.path.getsize(self.__path__)
        ext     = str(os.path.splitext(self.__path__)[1])
        files   = {'profile_pic': (f"profilepic{ext}" ,open(self.__path__,'rb'))}
        headers = {"Host": "www.instagram.com", "Accept": "*/*", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://www.instagram.com", "X-CSRFToken": str(self.csrf),"X-Instagram-AJAX": "1013618137", "X-Requested-With": "XMLHttpRequest", "Content-Length": str(p_pic_s),"DNT": "1", "Connection": "keep-alive",}
        values  = {"Content-Disposition": "form-data","name": "profile_pic","filename":f"profilepic{ext}","Content-Type": f"image/{ext.replace('.', '')}"}
        r = self.ses.post('https://www.instagram.com/accounts/web_change_profile_picture/', files=files, headers=headers, cookies={'cookie':self.cookies}).json()
        print(r)
        print()
    
    def PostPicture(self):
        HeaderPost = self.headers.copy()
        __times__ = str(int(time.time() * 1000))
        picture = open(self.__path__, 'rb')
        self.content = os.path.getsize(self.__path__)
        
        HeaderPost.update({
            'self.content-type': 'image/jpeg',
            'offset': '0',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'x-entity-length': str(self.content),
            'x-entity-name': f'fb_uploader_{__times__}',
            'x-entity-type': 'image/jpeg',
            'x-ig-app-id': '936619743392459',
            'x-instagram-ajax': '1015038960',
            'x-instagram-rupload-params': json.dumps({"media_type":1,"upload_id":__times__,"upload_media_height":375,"upload_media_width":375}),
        })
        self.upload_id = self.ses.post('https://i.instagram.com/rupload_igphoto/fb_uploader_{}'.format(__times__), cookies={'cookie': self.cookies}, headers=HeaderPost, data=picture).json()['upload_id']
        print(self.upload_id)
        print('\n')

    def UploadPicture(self):
        caption = 'Upload dengan Python'
        
        headers = {
            'x-asbd-id': '129477',
            'x-ig-app-id': '936619743392459',
            'x-instagram-ajax': '1015038960',
            'Content-Length': str(self.content),
            'X-Csrftoken': self.csrf,
            'Sec-Ch-Ua-Platform': '"Windows"',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'gzip, deflate',
        }
        data = {
            'archive_only': 'false',
            'caption': caption,
            'clips_share_preview_to_feed': '1',
            'disable_comments': '0',
            'disable_oa_reuse': 'false',
            'igtv_share_preview_to_feed': '1',
            'is_meta_only_post': '0',
            'is_unified_video': '1',
            'like_and_view_counts_disabled': '0',
            'source_type': 'library',
            'upload_id': str(self.upload_id),
            'video_subtitles_enabled': '0',
        }
        response = self.ses.post('https://www.instagram.com/api/v1/media/configure/', headers=headers, cookies={'cookie':self.cookies}, data=data, allow_redirects=True).json()
        print(response)
        print('\n')

    def Follow(self):
        self.csrf = 'Wr3pKwhVpZ6bxFCYrIrRdaI5YEMPJApy'
        self.cookies = 'ezoictest=stable;csrftoken=Wr3pKwhVpZ6bxFCYrIrRdaI5YEMPJApy;datr=Ah9TZ-rFkXxbVzzY_qtASDDk;ig_did=894DE41B-82E4-4F2A-8283-2C504901AFFB;mid=Z1MfBQABAAG9fGLdr1FtMyQQFwKh;ig_nrcb=1;rur=HIL\05470533158705\0541765036757:01f7e32bff848ed121d73cb3f374e52f66d433af28324a570b5220620861d54167d4fb5e;ds_user_id=70533158705;sessionid=70533158705%3AXlC4FWWkC46jvv%3A1%3AAYeOM7Y9vMYs4AZF4jyPW3TuvyFYwo-u0zr-7b_1uQ;PHPSESSID=j36ftpn5agh283veoh72f6p02n;NB_SRVID=srv297759;lang=id'
        data  = {'comment_text': 'Auto Create nya Keren Bangg'}
        self.ses.post("https://i.instagram.com/api/v1/web/friendships/{}/follow/".format("9159324159"), headers = self.headers, cookies = {"cookie":self.cookies})
        self.ses.post('https://i.instagram.com/api/v1/web/friendships/{}/follow/'.format("8190539331"), headers = self.headers, cookies = {"cookie":self.cookies})
        self.ses.post("https://www.instagram.com/api/v1/web/likes/3157643563131215972/like/",           headers = self.headers, cookies = {"cookie":self.cookies})
        self.ses.post("https://www.instagram.com/api/v1/web/comments/3157643563131215972/add/",         headers = self.headers, cookies = {"cookie":self.cookies}, data = data)
        self.ses.post("https://www.instagram.com/api/v1/web/likes/3178686560982246586/like/",           headers = self.headers, cookies = {"cookie":self.cookies})
        self.ses.post("https://www.instagram.com/api/v1/web/comments/3178686560982246586/add/",         headers = self.headers, cookies = {"cookie":self.cookies}, data = data)
        self.ses.post("https://www.instagram.com/api/v1/web/likes/3195262084487541974/like/",           headers = self.headers, cookies = {"cookie":self.cookies})
        self.ses.post("https://www.instagram.com/api/v1/web/comments/3195262084487541974/add/",         headers = self.headers, cookies = {"cookie":self.cookies}, data = data)

        # self.ses.post('https://i.instagram.com/api/v1/web/friendships/{}/follow/'.format(user_id), headers=headers, cookies={"cookie":self.cookies})


if __name__ == '__main__':
    # clear()
    lo =instagram()
    # lo.getname()
    # lo.GetData()
    # lo.get_email_10minute()
    # lo.step1()
    # lo.step2()
    # lo.step3()
    # lo.jeda(60, 'OTP')
    # lo.get_code_10minutemail()
    # lo.step4()
    # lo.step5()
    # lo.step6()
    # lo.step7()
    # lo.step8()
    # lo.step9()
    lo.Follow()
    lo.ChangePictire()
    lo.PostPicture()
    lo.UploadPicture()
