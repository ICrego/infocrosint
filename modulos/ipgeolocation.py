import requests


def analyze(api_key, ip):
    parametros = {
        'apiKey': api_key,
        'ip': ip
    }
    r = requests.get('https://api.ipgeolocation.io/ipgeo', params=parametros)
    todo=r.json()
    f=open('temp','a')
    f.writelines('País: ' + todo['country_name'] + '\n')
    f.writelines('Ciudad: ' + todo['city'] + '\n')
    f.writelines('Latitud: ' + todo['latitude'] + '\n')
    f.writelines('Longitud: ' + todo['longitude'] + '\n')
    f.writelines('ISP: ' + todo['isp'] + '\n')
    f.writelines('Organización: ' + todo['organization'] + '\n')
    f.close()

