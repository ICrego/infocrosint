import requests

def analyze_otx (api_key , q , t):
    
    if t == '1':
        res = requests.get('https://otx.alienvault.com/api/v1/indicators/IPv4/' + q + '/general')
        todo=res.json()
        f=open('temp','a')
        if todo['pulse_info']['count']!='0':
            f.writelines('La Ip ' + q + ' está considerada como maliciosa por OTX\n')
        else:
            f.writelines('OTX no detecta la ip como maliciosa\n')
        f.close()
    if t == '3':
        res = requests.get('https://otx.alienvault.com/api/v1/indicators/domain/' + q + '/general')
        todo=res.json()
        f=open('temp','a')
        if todo['pulse_info']['count']!=0:
            f.writelines('El domino ' + q + ' está considerado como malicioso por OTX\n')
        else:
            f.writelines('OTX no detecta el dominio como malicioso\n')
        f.close()
