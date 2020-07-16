import requests

def analyze_riskiq(key , secret , q , t):
    if t == '1':
        d={"query": q}
        res = requests.get('https://api.passivetotal.org/v2/actions/classification', auth=(key, secret) , json=d)
        todo=res.json()
        if todo['classification'] != None:
            f=open('temp','a')
            f.writelines('Clasificación según RiskIQ: ' + str(todo['classification']) + '\n')
            f.close()
        res = requests.get('https://api.passivetotal.org/v2/enrichment/malware', auth=(key, secret) , json=d)
        todo=res.json()
        f=open('temp','a')
        if todo['success'] is True:
            f.writelines('Información de malware sobre la IP desde PassiveTotal\n')
            for x in todo['results']:
                f.writelines('Fecha: ' + str(x['collectionDate']) + '\n')
                f.writelines('Fuente: ' + str(x['source'])+ '\n')
                f.writelines('Enlace: ' + str(x['sourceUrl'])+ '\n\n')
        f.close()
        
    if t =='2':
        res = requests.get('https://api.passivetotal.org/v2/whois/search?query=' + q + '&field=email', auth=(key, secret))
        todo=res.json()
        if todo['results'] =='':
            f=open('temp','a')
            f.writelines('Datos de Whois asociado a dicha dirección de email: \n')
            f.writelines('Nombre: ' + todo['results'][0]['admin']['name'] + '\n')
            f.writelines('Calle: ' + todo['results'][0]['admin']['street'] + '\n')
            f.writelines('Ciudad: ' + todo['results'][0]['admin']['city']+'\n')
            f.writelines('Código postal: ' + todo['results'][0]['admin']['postalCode']+'\n')
            f.writelines('Provincia: ' + todo['results'][0]['admin']['state']+'\n')
            f.writelines('País: ' + todo['results'][0]['admin']['country']+'\n')
            f.writelines('Teléfono: '+ todo['results'][0]['admin']['telephone']+'\n')
            f.writelines('Organización: ' + todo['results'][0]['admin']['organization']+'\n')
            f.writelines('Datos del registrante: \n')
            f.writelines('Nombre: ' + todo['results'][0]['registrant']['name']+'\n')
            f.writelines('Email: '+ todo['results'][0]['registrant']['email']+'\n')
            f.writelines('Calle: '+ todo['results'][0]['registrant']['street']+'\n')
            f.writelines('Ciudad: '+todo['results'][0]['registrant']['city']+'\n')
            f.writelines('Código postal: '+ todo['results'][0]['registrant']['postalCode']+'\n')
            f.writelines('Provincia: '+ todo['results'][0]['registrant']['state']+'\n')
            f.writelines('País: '+ todo['results'][0]['registrant']['country']+'\n')
            f.writelines('Teléfono: ' + todo['results'][0]['registrant']['telephone']+'\n')
            f.writelines('Organización: ' + todo['results'][0]['registrant']['organization']+'\n')
            f.writelines('Dominio: ' + todo['results'][0]['domain']+'\n')
            f.writelines('Servidores DNS')
            f.writelines(str(todo['results'][0]['nameServers'])+'\n')
            f.writelines('Fecha de registro: ' + todo['results'][0]['registered']+'\n')
            f.writelines('Fecha de expiración: ' + todo['results'][0]['expiresAt']+'\n')
            f.close()

    if t == '3':
        res = requests.get('https://api.passivetotal.org/v2/enrichment?query=' + q, auth=(key, secret))
        todo=res.json()
        f=open('temp','a')
        if todo['classification'] is not None:
            f.writelines('Clasificación: ' + str(todo['classification']) + '\n')
            if todo['everCompromised'] != False:
                f.writelines('Comprometido: ' + str(todo['everCompromised']) + '\n')
        else:
            f.writelines('RsikIQ no detecta el dominio no malicioso\n')
        f.close()