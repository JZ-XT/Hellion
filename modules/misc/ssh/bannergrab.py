#First Module for Hellion, will probaly define the standard for all future modules
import socket

#Module Settings
ip      = '127.0.0.1'
port    = 22
timeout = 5

exploit(ip, port, timeout): #main fuction for all modules
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        banner = s.recive(1024)
        s.close()
        banner = banner[1:]
        return banner
    except Exception as e:
        print(str(e))
        return ''
