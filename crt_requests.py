#!/usr/bin/python3
import requests
import json
import sys
import argparse

parser = argparse.ArgumentParser(description="CrtPy to enumerate Subdomains from Crt.sh")
parser.add_argument("--domain","-d",required=True,help="specify the target domain")
parser.add_argument("--output","-o",required=False,help="specify output file name")
args = parser.parse_args()
output = str(args.output)

if int(sys.version_info.major) < 3:
    print("Run With Python3")
    exit()
else:
    domain = args.domain
    print("Enumerating >> " , domain , "\n")
    url = (f"https://crt.sh/?q={domain}&output=json")
    data_req = requests.get(url).content
    data = json.loads(data_req)
    for a,b in enumerate(data):
        domains = str(b['name_value'])
        print(domains)
        if output == None:
            pass
        elif output == "None":
            pass
        else:
            file = open(output,"a")
            file.write(domains)
            file.close()
