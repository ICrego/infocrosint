import requests

def analyze_viewdns(api_key , q , t):
    if t == '1':
        res=requests.get('https://api.viewdns.info/iplocation/?ip=' + q + '&apikey=' + api_key + '&output=json')
        
    if t == '4':
        res=requests.get('https://api.viewdns.info/httpheaders/?domain=' + q + '&apikey=' + api_key + '&output=json')
        todo=res.json()
        f=open('temp', 'a')
        f.writelines('\nCabeceras del dominio '+ q + '\n')
        for x in todo['response']['headers']:
            f.writelines(x['name']+ ': ' + x['value']+'\n')
        f.close()