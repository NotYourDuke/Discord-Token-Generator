# Description: This file contains the Utils class, which contains static methods that are used in other files.

import random
import string
from json import dumps,loads
from base64 import b64encode
import os
config = loads(open("data/config.json", "r").read())



class Utils(object):
    @staticmethod
    def getborndate():
        year=str(random.randint(1997,2001));month=str(random.randint(1,12));day=str(random.randint(1,28))
        if len(month)==1:
            month='0'+month
        if len(day)==1:
            day='0'+day
        return year+'-'+month+'-'+day

    @staticmethod
    def getemail():
        return ''.join(random.choice(string.ascii_letters) for i in range(10)) + '@gmail.com'
    
    @staticmethod
    def passw():
        if config["password"] == "random":
            #return a strong password
            return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(10))
        else:
            return config["password"]
        
    @staticmethod
    def username():
        if config["username"] == "real":
            return open("data/usernames.txt", encoding="utf-8").read().splitlines()[random.randint(0, len(open("data/usernames.txt", encoding="utf-8").read().splitlines()) - 1)]
        else:
            return config['username']
        
    @staticmethod
    def getsuperproperties(buildNum: int):
        return b64encode(dumps({"os":"Windows","browser":"Chrome","device":"","system_locale":"pl-PL","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36","browser_version":"108.0.0.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":buildNum,"client_event_source":None,"design_id":0}).encode()).decode()
    
    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
        
    @staticmethod
    def getproxy():
        with open('data/proxies.txt', "r") as f:
            return random.choice(f.readlines()).strip()
    
    @staticmethod
    def getformattedproxy(proxy):
        if '@' in proxy:
            return proxy
        elif len(proxy.split(':')) == 2:
            return proxy
        else:
            if '.' in proxy.split(':')[0]:
                return ':'.join(proxy.split(':')[2:]) + '@' + ':'.join(proxy.split(':')[:2])
            else:
                return ':'.join(proxy.split(':')[:2]) + '@' + ':'.join(proxy.split(':')[2:])
        