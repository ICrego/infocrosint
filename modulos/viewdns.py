import requests

def analyze_viewdns(api_key , q , t):
    if t == '1':
        res=requests.get('https://api.viewdns.info/spamdblookup/?ip' + q + '&apikey=' + api_key + '&output=json')
        todo=res.json()
        f=open('temp', 'a')
        f.writelines('\nBase de datos de Spam en las que aparece la IP: \n')
        for x in todo['response']['dbs']:
            if x['result'] =='ok':
                f.writelines(str(x['name']) + '\n')
        f.close()
    if t == '3':
        res=requests.get('https://api.viewdns.info/httpheaders/?domain=' + q + '&apikey=' + api_key + '&output=json')
        todo=res.json()
        f=open('temp', 'a')
        f.writelines('\nCabeceras del dominio '+ q + '\n')
        for x in todo['response']['headers']:
            f.writelines(x['name']+ ': ' + x['value']+'\n')
        f.close()