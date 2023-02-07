#!/usr/bin/python3
#author : @semihozdmirr
import requests
import json
import sys
import argparse

parser = argparse.ArgumentParser(description="CrtPy to enumerate Subdomains from Crt.sh")
parser.add_argument("--domain","-d",required=True,help="specify the target domain")
parser.add_argument("--output","-o",required=False,help="specify output file name")
args = parser.parse_args()
output = str(args.output)

v = str("".join(sys.version))[0:3]
if v < "3.6":
    print("Python Version is old,Recommended 3.6+")
    exit()
else:
        domain = args.domain
        print("Enumerating >> " , domain , "\n")
        url = (f"https://crt.sh/?q={domain}&output=json")
        req = requests.get(url).content
        data = json.loads(req)
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

