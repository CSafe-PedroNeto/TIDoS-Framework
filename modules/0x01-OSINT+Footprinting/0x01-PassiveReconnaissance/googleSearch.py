#!/usr/bin/env python
# coding: utf-8

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author : @_tID
#This module requires TIDoS Framework
#https://github.com/theInfectedDrake/TIDoS-Framework


import time
import sys, platform
import os
import urllib.request, urllib.error, urllib.parse
try:
    from google import search
except:
    from googlesearch import search
from time import sleep
from core.Core.colors import *

def googleSearch():

    try:
        time.sleep(0.4)
        print(R+'\n   ===========================')
        print(R+'    G O O G L E   S E A R C H')
        print(R+'   ===========================\n')
        lol = input(O+ " [#] QUERY :> " + color.END)
        time.sleep(0.8)
        m = input(O+' [#] Search limit (not recommended above 30) :> ')
        print(G+ " [!] Below are the list of websites with info on '" +lol+ "'")
        x = search(lol, tld='com', lang='es', stop=int(m))
        for url in x:
            print(O+"   [!] Site Found :> "+W + url)
            q = open('.google-cookie','w')
            q.close()
    except urllib.error.HTTPError:
        print(R+' [-] You have used google many times.')
        print(R+' [-] Service temporarily unavailable.')
