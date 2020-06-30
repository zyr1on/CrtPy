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
	base_url = (f"https://crt.sh/?q={domain}&output=json")
	req = requests.get(base_url).content
	#req = requests.get(base_url).content.decode('utf-8')
	data = json.loads(req)
	for keys,values in enumerate(data):
		print(values['name_value'])
