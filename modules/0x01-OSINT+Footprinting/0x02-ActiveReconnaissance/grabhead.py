#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#This module requires TIDoS Framework
#https://github.com/0xInfection/TIDoS-Framework

from __future__ import print_function
import urllib
import time
import sys
from time import sleep
from core.Core.colors import *

def grabhead(web):

    time.sleep(0.4)
    print(R+'\n      ==================================')
    print(R+'      G R A B   H T T P   H E A D E R S')
    print(R+'     ===================================\n')
    print(GR + color.BOLD + ' [!] Grabbing HTTP Headers...')
    time.sleep(0.4)
    web = web.rstrip()
    try:
        header = urllib.request.urlopen(web).info()
        print('')
        print(G+str(header))
    except urllib.HTTPError:
        print(R+' [-] Exception while request (HTTPError)...')
    except:
        print(R+' [-] Something went wrong...')
