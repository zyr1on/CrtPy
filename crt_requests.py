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
domain = args.domain
print("Enumerating >>>",domain )

if int(sys.version_info.major) < 3:
    print("Run With Python3")
    exit()

url = (f"https://crt.sh/?q={domain}&output=json")

try:
    data_req = requests.get(url).content
    data = json.loads(data_req)
    if output == None or output == 'None':
        for a , b in enumerate(data):
            domains = str(b['name_value'])
            print(domains)
    else:
        file = open(output,"a")
        for a,b in enumerate(data):
            domains = str(b['name_value'])
            file.write(domains)
        file.close()
except KeyboardInterrupt:
        print("\nExiting...")
except Exception as err:
        print(err)
except requests.exceptions.RequestException as err:
    print ("Request Exception:",err)
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)     
