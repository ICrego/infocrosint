import requests

def analyze_threatcrowd(q, t):
    
    if t == '1':
        res= requests.get('https://www.threatcrowd.org/searchApi/v2/ip/report/', params = {'ip': q})
        todo=res.json()
        if todo['response_code'] == '1':
            f=open('temp','a')
            f.writelines('Ultimos dominios en esa IP\n')
            for x in todo['resolutions']:
                f.write('Fecha: ' + x['last_resolved'] + ' dominio: ' + x['domain'] + '\n')
            f.close()
        if todo['response_code'] == '0':
            print("No se ha podido obtener ninguna información de ThreatCrowd\n")
            
    if t == '3':
        res= requests.get('https://www.threatcrowd.org/searchApi/v2/domain/report/', params = {"domain": q})
        todo=res.json()
        if todo['response_code'] == '1':
            f=open('temp','a')
            f.writelines('\nSubdominios\n')
            for x in todo['subdomains']:
                f.writelines(x+'\n')
            f.close()
        if todo['response_code'] == '0':
            print("No se ha podido obtener ninguna información de ThreatCrowd\n")
