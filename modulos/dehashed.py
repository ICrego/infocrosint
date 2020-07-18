import requests , json

def analyze_dehashed(api_key , username , email):
    h={'Accept' : 'application/json' }
    aut=(username, api_key)
    res = requests.get('https://api.dehashed.com/search?query=' + email , auth=aut , headers=h)
    todo=res
    if res.status_code == 200:
        f=open('temp','a')
        f.writelines('El dominio tiene un total de ' + str(todo['balance']) + ' entradas en ' + str(len(todo['entries'])) + '  breachs \n')
        for x in todo['entries']:
            f.writelines('Email: '+ x['email'] + ' Usuario: '+ x['username'] +' Password: ' + x['password'] + '\n')
        f.close()
    if res.status_code == 400:
        print("Se ha excedido el límite de peticiones al mismo tiempo a Dehashed .")
    if res.status_code == 401:
        print("Dehashed  API inválida.")
    if res.status_code == 404:
        print("Método inválido en Dehashed .")
    if res.status_code == 302:
        print("Error en la petición a Dehashed .")
    if res.status_code == 404:
        print("Método inválido en Dehashed .")