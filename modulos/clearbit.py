import requests



def analyze_clearbit(api_key , q, t):
    aut=(api_key , '')
    if t == '2':
        res=requests.get('https://person.clearbit.com/v2/combined/find?email=:' + q , auth=aut)
        todo=res.json()
        if todo['error']['type'] == "unknown_record":
            print('No se ha encontrado informacion en Clearbit')
        else:
            f=open('temp','a')
            f.writelines('Datos personales asociados a dicho email\n')
            f.writelines('Nombre:  '+ str(todo['person']['name']['fullName']) + '\n')
            f.writelines('Localización: '+ str(todo['person']['location']) + '\n')
            f.writelines('Bio: '+ str(todo['person']['bio']) + '\n')
            f.writelines('Site: '+ str(todo['person']['site']) + '\n')
            f.writelines('Avatar: '+ str(todo['person']['avatar']) + '\n')
            f.writelines('Empleo: '+ str(todo['person']['employment']['name']) + ' con el título de ' + str(todo['person']['employment']['title'])+'\n')
            f.writelines('RRSS\n')
            f.writelines('Facebook: '+ str(todo['person']['facebook']['handle']) +'\n')
            f.writelines('Github: '+ str(todo['person']['github']['handle']) + '| ID: ' + str(todo['person']['github']['id']) + '\n')
            f.writelines('Twitter: '+ str(todo['person']['twitter']['handle']) + '| ID: ' + str(todo['person']['twitter']['id']) + '\n')
            f.writelines('LinkedIn: '+ str(todo['person']['linkedin']['handle']) + '\n')
            f.writelines('Google+: '+ str(todo['person']['googleplus']['handle']) + '\n')
            f.writelines('Gravatar: '+ str(todo['person']['gravatar']['handle']) + '\n')
            f.close()
           
    if t == '3':
        res=requests.get('https://company.clearbit.com/v2/companies/find?domain=' + q, auth=aut)
        todo=res.json()
        f=open('temp', 'a')
        f.writelines('\n Información del dominio: \n')
        for x in todo['domainAliases']:
            f.writelines('Alias: '+  str(x) + '\n')
        f.writelines('Sector: '+  str(todo['category']['sector']) + '\n')
        f.writelines('Fundada en: '+  str(todo['foundedYear']) + '\n')
        f.writelines('Dirección: '+  str(todo['location']) + '\n')
        f.writelines('Facebook handle: '+  str(todo['facebook']['handle']) + '\n')
        f.writelines('LinkedIn handle: '+  str(todo['linkedin']['handle']) + '\n')
        f.writelines('Twitter handle: '+  str(todo['twitter']['handle']) + '\n')
        f.writelines('Crunchbase handle: '+  str(todo['crunchbase']['handle']) + '\n')
        f.writelines('Número de empleados: '+  str(todo['metrics']['employees']) + '\n')
        f.writelines('Tecnología encontrada en el sitio web:\n')
        for x in todo['tech']:
            f.writelines(str(x) + '\n')
        f.close()
