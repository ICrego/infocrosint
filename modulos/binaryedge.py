import requests

def analyze_binary(api_key , q , c):
    h = {'X-Key': api_key}
    if c == '2':
        res=requests.get('https://api.binaryedge.io/v2/query/dataleaks/email/' + q , headers=h)
        todo=res.json()
        if res.status_code == 401:
            print('Token de BinaryEdge invalido')
        if res.status_code == 404:
            print('BinaryEdge no ha encontrado ningún resultado')
        if res.status_code == 200:
            if todo['total'] != 0:
                f=open('temp','a')
                for x in todo['events']:
                    f.writelines(x + '\n')
                f.close()
    if c == '3':    
        res=requests.get('https://api.binaryedge.io/v2/query/dataleaks/organization/' + q , headers=h)
        todo=res.json()
        if res.status_code == 401:
            print('Token de BinaryEdge invalido.')
        if res.status_code == 403:
            print('La API actual de BinaryEdge no permite esta búsqueda.')
        if res.status_code == 404:
            print('BinaryEdge no ha encontrado ningún resultado.')
        if res.status_code == 200:
            print('entra')
            if todo['total'] != 0:
                f=open('temp','a')
                f.writelines('El dominio tiene un total de ' + str(todo['total']) + ' emails comprometidos en ' + str(len(todo['groups'])) + '  breachs \n')
                f.writelines('Listado de breachs: \n')
                for x in todo['groups']:
                    f.writelines('Leak: '+ x['leak'] + ' Cantidad: '+ str(x['count']) + '\n')
                f.close()