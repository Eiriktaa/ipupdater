
import requests, sys, os, json
##Gets the current ip and looks for changes

#Auth headers   
token = os.getenv("CLOUDFLARE_TOKEN")
zone = os.getenv("CLOUDFLARE_ZONE")
headers = {
    "X-Auth-Email":os.getenv("CLOUDFLARE_EMAIL"),
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json" 
}   

endpoint_url = "https://api.cloudflare.com/client/v4/"

def write_ip():
    with open(datafile,"w")as f:
        f.write(ip_adress)

def get_dns_records():
    ## GET zones/:zone_identifier/dns_records
    ## Loctates the ids for all records in the zone with the type of A
    ids=[]
    url = f"{endpoint_url}zones/{zone}/dns_records/?type=A"
    print(url)
    res = requests.get(url,headers=headers)
    jsondata = json.loads(res.text)

  
    for d in jsondata["result"]:
        ids.append(d)
    print(ids)
    return ids    
    #print(res.text)

def update_dns_records(ids):
    for record_id in ids:
        url = f"{endpoint_url}zones/{zone}/dns_records/{record_id['id']}"
        data = {
            "type": record_id["type"],
            "name": record_id["name"],    
            "content": ip_adress,
            "ttl":record_id["ttl"]
        }
        res = requests.patch(url,headers=headers, data=json.dumps(data))
    
ip_adress= requests.get("https://api.ipify.org?format=txt").text
historical_ip = ""
datafile = "ipfile.txt"

try:
    with open(datafile,"r") as ipfile:
        historical_ip = ipfile.read()
except:
    write_ip()
    print("Something wrong with opening fi")
## Ip unchanged

if historical_ip == ip_adress:
 sys.exit(0)
else:
    ## updates all the DNS records to the new ip
    update_dns_records(get_dns_records())
    write_ip()
