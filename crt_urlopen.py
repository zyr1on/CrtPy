#!/usr/bin/python3
#author : @semihozdmirr
from urllib.request import urlopen
import json
import sys

if len(sys.argv) < 2:
	print("usage python3 crt.py <domain>")
else:
	domain = sys.argv[1]
	print("Enumerating >> " , domain , "\n")
	url = (f"https://crt.sh/?q={domain}&output=json")
	req = urlopen(url)
	data = json.loads(req.read())
	for keys,values in enumerate(data):
		print(values['name_value'])

