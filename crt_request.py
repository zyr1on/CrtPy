#!/usr/bin/python3
#author : @semihozdmirr

import requests
import json
import sys

if len(sys.argv) < 2:
	print("usage python3 crt.py <domain>")
else:
	domain = sys.argv[1]
	print("Enumerating >> " , domain , "\n")
	url = (f"https://crt.sh/?q={domain}&output=json")
	req = requests.get(url).content
	#req = requests.get(url).content.decode('utf-8')
	data = json.loads(req)
	for keys,values in enumerate(data):
		print(values['name_value'])
