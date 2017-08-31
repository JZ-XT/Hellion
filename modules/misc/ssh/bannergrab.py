#First Module for Hellion, will probaly define the standard for all future modules
import socket

#Module Settings
rhost   = '127.0.0.1'
rport   = 22
timeout = 5
recv    = 1024
settings = {
        'rhost'     : {'Desc': '(string) Ip to grab banner from', 'Value': rhost},
        'rport'     : {'Desc':'(int) Port to use', 'Value': rport},
        'timeout'   : {'Desc': '(int) Socket timeout', 'Value': timeout},
        'recv'      : {'Desc': '(int) Amount of bytes to recive', 'Value': recv}
        }

def reloadSettings():
    global rhost, rport, timeout, settings
    settings['rhost']['Value']      = rhost
    settings['rport']['Value']      = rport
    settings['timeout']['Value']    = timeout
    settings['recv']['Value']       = recv

def exploit(): #main fuction for all modules
    global rhost, rport, timeout, recv
    print('Grabbing Banner...')
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((str(rhost), int(rport)))
        s.send(b'WhoAreYou\r\n')
        banner = s.recv(recv)
        s.close()
        banner = str(banner[1:])
        print('[+] Grabbed Banner: ' + banner)
        return banner
    except Exception as e:
        print('[-] Error ' + str(e))
        return ''
