import requests,json
import urllib3
urllib3.disable_warnings()
url = "https://api.covid19tracking.narrativa.com/api/countries"
response = requests.request("GET", url, verify=False)
data = dict(json.loads(response.text))
count=0
cont=len(data["countries"])-1

#while count<=cont:
#    print(data["countries"][count]["name_es"])
#    count+=1

for elem in data["countries"]:
    print(elem["id"],"->",elem["name_es"])