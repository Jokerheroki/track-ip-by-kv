#!/usr/bin/python

#Name          : Track-ip-by-kv
#Writer(s)     : Kisna verma 
#Description   : Track-ip-by-kv is a simple IP Tracker using Python.

import os
import urllib2
import json
import colorama
colorama.init(autoreset=True)

os.system("clear");
print (colorama.Fore.CYAN + """)

  __                        __             .__                ___.                    __           
_/  |_____________    ____ |  | __         |__|_____          \_ |__ ___.__.         |  | _____  __
\   __\_  __ \__  \ _/ ___\|  |/ /  ______ |  \____ \   ______ | __ <   |  |  ______ |  |/ /\  \/ /
 |  |  |  | \// __ \\  \___|    <  /_____/ |  |  |_> > /_____/ | \_\ \___  | /_____/ |    <  \   / 
 |__|  |__|  (____  /\___  >__|_ \         |__|   __/          |___  / ____|         |__|_ \  \_/  
                  \/     \/     \/            |__|                 \/\/                   \/         
                                           
  Python IP Tracker - kisna verma
"""
print "\r"
while True:
		ip = raw_input("What Your Target IP : ")
		url = "https://api.ipdata.co/"
		response = urllib2.urlopen(url + ip)
		data = response.read()
		values = json.loads(data)

		print("------------------------------------")
		print "\r"
		print(" IP           :  " + values['ip'])
		print(" City         :  " + values['city'])
		print(" Region       :  " + values['region'])
		print(" Country      :  " + values['country_name'])
		print(" Continent    :  " + values['continent_name'])
		print(" Time Zone    :  " + values['time_zone'])
		print(" Currency     :  " + values['currency'])
		print(" Calling Code :  " + "+" + values['calling_code'])
		print(" Organisation :  " + values['organisation'])
		print(" ASN          :  " + values['asn'])
		print "\r"
		break
