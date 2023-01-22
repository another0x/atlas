import os, re, time, requests
from colorama import Fore

def main(kode):
    m = 0
    while True:
    # Generate Random Email
        sene = 'https://www.1secmail.com/api/v1/'
        umail = requests.get(sene+'?action=genRandomMailbox&count=1').text
        mail = umail.replace('["', '').replace('"]', '')
        un = mail.split('@')

    # Sennding Reff
        sf = 'https://user.atlasvpn.com/v1/request/join'
        hulu = {"Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Origin": "https://account.atlasvpn.com", "Referer": "https://account.atlasvpn.com/", "Sec-Ch-Ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "X-Client-Id": "Web", "Content-Type": "application/json;charset=UTF-8"}
        isi = {"email": mail,"marketing_consent": True,"referrer_uuid": kode,"referral_offer": "initial"}
        x = requests.post(sf, json=isi, headers=hulu)
        print('[\033[32m', time.strftime('%H:%M:%S', time.localtime()), '\033[93m] Sending Request...')
        time.sleep(1)

    # Checking Email
        cekID = sene+'?action=getMessages&login='+un[0]+'&domain='+un[1]
        getID = requests.get(cekID).json()
        i = getID[0]['id']
        print('[\033[32m', time.strftime('%H:%M:%S', time.localtime()), '\033[93m] Validating Email...')

        cekMSG = sene+'?action=readMessage&login='+un[0]+'&domain='+un[1]+'&id='+str(i)
        getMSG = requests.get(cekMSG).json()
        txt = getMSG['textBody']
        tkn = re.search('token=(.*) ', txt).group(1)

    # Verified Email
        m += 1
        app = 'https://user.atlasvpn.com/v1/auth/confirm'
        air = {"Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Authorization": "Bearer "+str(tkn)+"", "Origin": "https://account.atlasvpn.com", "Referer": "https://account.atlasvpn.com/", "Sec-Ch-Ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
        dor = requests.get(app, headers=air)
        print(f'[\033[32m', time.strftime('%H:%M:%S', time.localtime()), '\033[93m] Success adding {} refferal!!!'.format(m))

if __name__ == '__main__':
    os.system('@echo off')
    os.system('MODE 95,25')
    os.system('title Get Reff AtlasVPN by _MMAUL_')
    print(Fore.CYAN+'[-]--------------------------AtlasVPN Ultimate Reff--------------------------[-]')
    print(Fore.CYAN+'[-]                    By _MMAUL_ --> https://mmaul.my.id                    [+]')
    print(Fore.CYAN+'[x]--------------------------------------------------------------------------[x]'+Fore.RESET)
    kode = input('Input your User ID: ')
    main(kode)
