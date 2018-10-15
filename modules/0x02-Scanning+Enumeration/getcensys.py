#!/usr/bin/env python
# coding: utf-8

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author : @_tID
#This module requires TIDoS Framework
#https://github.com/theInfectedDrake/TIDoS-Framework

import re
import urllib
import socket
import http.cookiejar
import subprocess
import time
from re import search
from getports import *
from core.Core.colors import *

def getos0x00(web):

    global flag
    flag = 0x00
    ip_addr = socket.gethostbyname(web)
    print(GR+' [*] Getting ip address...')
    time.sleep(0.7)
    print(G+' [+] Website IP : ' +O+ str(ip_addr))
    time.sleep(0.5)
    print(GR+' [*] Trying to identify operating system...')
    time.sleep(0.5)
    print(O+' [!] Configuring requests...')
    result = urllib.request.urlopen('https://www.censys.io/ipv4/%s/raw' % ip_addr).read()
    print(GR+' [*] Getting raw data...')
    time.sleep(0.8)
    print(R+' [*] Analysing responses...')
    try:
        match = search(r'&#34;os_description&#34;: &#34;[^<]*&#34;', result) # regex forked from Striker
        if match:
            flag = 0x01
            print(B+' [+] Operating System Identified : ' + C+ match.group().split('n&#34;: &#34;')[1][:-5])

        else:
            print(R+' [-] No exact OS match for '+O+web+'...')
            flag = 0x00
        return flag

    except Exception as e:
        print(R+' [-] Unhandled Exception : '+str(e))
