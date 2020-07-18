import sys
import requests


def analyze_censys ( api1, api2 , objetive , cual):
  API_URL = "https://censys.io/api/v1"
  UID = api1
  SECRET = api2
  who = objetive
  res = requests.get(API_URL + '/view/ipv4/'+  who, auth=(UID, SECRET))
  todo=res.json()
  f=open('temp','a')
  f.writelines('Autonomous System: ' + todo['autonomous_system']['name']+'\n')
  f.close()
