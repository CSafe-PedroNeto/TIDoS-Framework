#!/usr/bin/env python
# coding: utf-8

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author : @_tID
#This module requires TIDoS Framework
#https://github.com/theInfectedDrake/TIDoS-Framework


import requests
import time
import re
import socket
import http.cookiejar
from urllib.parse import urlencode
from re import search
from core.Core.colors import *

def serverdetect(web):

    print(R+'\n   ===========================')
    print(R+'    D E T E C T   S E R V E R')
    print(R+'   ===========================\n')
    time.sleep(0.4)
    print(GR+' [*] Checking server status...')
    web = web.replace('https://','')
    web = web.replace('http://','')
    try:
        ip_addr = socket.gethostbyname(web)
        print(G+' [+] Server detected online...')
        time.sleep(0.5)
        print(G+' [+] Server IP :> '+ip_addr)
    except:
        print(R+' [-] Server seems down...')

    print(GR+' [*] Trying to identify backend...')
    time.sleep(0.4)
    web = 'http://' + web
    try:
        r = requests.get(web)
        header = r.headers['Server']
        if 'cloudflare' in header:
            print(O+' [+] The website is behind Cloudflare.')
            print(G+' [+] Server : Cloudflare')
            time.sleep(0.4)
            print(O+' [+] Use the "Cloudflare" VulnLysis module to try bypassing Clouflare...')

        else:
            print(B+' [+] Server : ' +C+header)
        try:
            print(O+' [+] Running On : ' +G+ r.headers['X-Powered-By'])
        except:
            pass
    except:
        print(R+' [-] Failed to identify server. Some error occured!')
        pass

# ===============================================================#
# THIS HAS BEEN MIGRATED TO THE VULNERABILITY ENUMERATION MODULE
# ===============================================================#

#def bypass(domain):

#    print GR+' [*] Trying to get real IP...'
 #   post = urlencode({'cfS': domain})
  #  result = br.open(
#       'http://www.crimeflare.info/cgi-bin/cfsearch.cgi ', post).read()
#
 #   match = search(r' \b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', result)
  #  if match:
   #     bypass.ip_addr = match.group().split(' ')[1][:-1]
#       print G+' [+] Cloudflare found misconfigured!'
#       time.sleep(0.4)
#       print GR+' [*] Identifying IP...'
#       time.sleep(0.5)
 #       print G+' [+] Real IP Address : ' + bypass.ip_addr + '\n'
  #  else:
#       print R+' [-] Cloudflare properly configured...'
#       print R+' [-] Unable to find remote IP!\n'
#       pass
#
