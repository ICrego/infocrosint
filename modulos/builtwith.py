import requests

def analyze_builtwith(api_key , q):
    res=requests.get('https://api.builtwith.com/v14/api.json?KEY=' + api_key + '&LOOKUP=' + q)
    todo=res.json()
    f=open('temp','a')
    f.writelines('\nInformación sobre el dominio de BuiltWith \n')
    f.writelines('Tecnología de pago que usa el dominio: \n')
    for x in todo['Results'][0]['Result']['Paths'][0]['Technologies']:
        if x['Categories'] is not None:
            if x['IsPremium'] != 'no':
                f.writelines('Categoría: '+ str(x['Categories']) + '\n')
                f.writelines('Nombre :' + str(x['Name']) + '\n')
                f.writelines('Descripción: ' + str(x['Description']) + '\n')
    f.writelines('\nDato del domino: \n')
    f.writelines('RRSS: \n')
    for x in todo['Results'][0]['Meta']['Social']:
        f.writelines(str(x)+'\n')
    f.writelines('Teléfonos: \n')
    for x in todo['Results'][0]['Meta']['Telephones']:
        f.writelines(str(x)+'\n')
    f.writelines('Emails: \n')
    for x in todo['Results'][0]['Meta']['Emails']:
        f.writelines(str(x)+'\n')
    f.writelines('Nombres: \n')
    if todo['Results'][0]['Meta']['Names'] is not None:
        for x in todo['Results'][0]['Meta']['Names']:
            f.writelines('Nombre: ' + str(x['Name'])+'\n')
            f.writelines('Email: ' + str(x['Email']) + '\n')
    f.close()