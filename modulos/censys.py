import sys
import requests



def analyze_censys ( api1, api2 , objetive , cual):
  API_URL = "https://censys.io/api/v1"
  UID = api1
  SECRET = api2
  who = objetive
  if cual == '1':
    res = requests.get(API_URL + '/view/ipv4/'+  who, auth=(UID, SECRET))
    todo=res.json()
    f=open('temp','a')
    f.writelines('Autonomous System: ' + todo['autonomous_system']['name']+'\n')
    f.close()
  if cual == '4':
    res = requests.get(API_URL + '/view/website/'+  who, auth=(UID, SECRET))
   
  return res.json()