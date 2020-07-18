import requests

def analyze_virustotal(api_key, q , r):
    if r == '1':
        p = {'apikey': api_key,'ip': q}
        res = requests.get('https://www.virustotal.com/vtapi/v2/ip-address/report', params=p)
        todo=res.json()
        f=open('temp','a')
        if todo['last_https_certificate'] != "":
            f.writelines('Entidad: ' + str(todo['last_https_certificate']['issuer']['CN'])+ '\n')
            f.writelines('Algoritmo: ' + str(todo['last_https_certificate']['cert_signature']['signature_algorithm'])+'\n')
            f.writelines('Versión: ' + str(todo['last_https_certificate']['version'])+'\n')
        f.writelines('Detectadas URLs: \n')
        try:
            for x in todo['detected_urls']:
                f.writelines('Url: ' + str(todo['url'])  + '\n') 
                f.writelines('Positivos: ' + str(todo['positives']) + '\n')
                f.writelines('Fecha escaneo: ' + str(todo['scan_date']) + '\n')
        except:
            f.writelines('')
        f.close()
    
    if r == '3':
        p = {'apikey': api_key , 'domain': q}
        res = requests.get('https://www.virustotal.com/vtapi/v2/domain/report', params=p)
        todo=res.json()
        f=open('temp','a')
        f.writelines('\nInformación de Whois proporcionada por Virustotal: \n')
        f.write(todo['whois'])
        f.writelines('\nServidores DNS: \n')
        for x in todo['dns_records']:
            f.writelines(x['value']+'\n')
        f.writelines('Categoria: \n')
        f.writelines(str(todo['categories']) + '\n')
        if todo['detected_urls'] == "":
            f.writelines('Url detectadas: \n')
            f.writelines(str(todo['detected_urls'])+ '\n')
        f.close()