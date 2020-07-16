import requests
from requests.auth import HTTPBasicAuth

def analyze_fraudguard(user, passw, q):
    ip=requests.get('https://api.fraudguard.io/v2/ip/'+q, verify=True, auth=HTTPBasicAuth('user', 'passw'))
    todo=ip
    if  todo.status_code == 200:
        f=open('temp','a')
        try:
            f.writelines('Tipo de amenaza: ' +str(todo['threat'])+ '\n')
            f.writelines('Nivel de riesgo: '+ str(todo['risk_level'])+ '\n')
        except:
            f.writelines('')
        f.close()
        
    if  todo.status_code == 400:
        print('Peticion incorrecta')
    if  todo.status_code == 401:
        print('Credenciales invalidas')
    if  todo.status_code == 429:
        print('Ha excedido el número de peticiones, Cambie de plan')
    if  todo.status_code == 500:
        print('Error interno del servidor. Intentelo mas tarde')
    if  todo.status_code == 503:
        print('Servicio no disponible. Intentelo mas tarde.')
