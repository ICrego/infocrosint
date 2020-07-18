import requests
import json



def analyze_securitytr(api_key, q, t):
    url = "https://api.securitytrails.com/v1/domain/"+ q
    headers = {'APIKEY': api_key}
    response = requests.request("GET", url, headers=headers)
    todo=response.json()
    f=open("temp" , "a")
    for x in todo['current_dns']['a']['values']:
        f.writelines('IP asociada al dominio es: ' + x['ip'] + '\n')
    f.writelines('Servidores de correo: \n')
    for x in todo['current_dns']['mx']['values']:
        f.writelines('Nombre organización: ' + x['hostname_organization'] + ' /// ' + x['hostname']+  '\n')
    f.writelines('Servidores DNS: \n')
    for x in todo['current_dns']['ns']['values']:
        f.writelines(x['nameserver'] + '\n')
    f.close()




