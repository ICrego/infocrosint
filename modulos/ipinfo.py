import requests


def analyze_ipinfo (api_key, ip):
    r = requests.get('https://ipinfo.io/' + ip + '?token=' + api_key)
    todo=r.json()
    f=open('temp','a')
    f.writelines('ASN: ' + todo['org'] + '\n')
    f.close()