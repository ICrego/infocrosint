import requests



def analyze_clearbit(api_key , email, t):
    if t == '2':
        aut=(api_key , '')
        res=requests.get('https://person.clearbit.com/v2/combined/find?email=:' + email , auth=aut)
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
        res=requests.get('https://api.viewdns.info/freeemail/?domain=test.com&apikey=yourapikey&output=output_type')
