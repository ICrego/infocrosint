import requests


def analyze_shodan(api_key, q, t):
    if t == '1':
        r = requests.get('https://api.shodan.io/shodan/host/' + q + '?key=' + api_key)
        todo=r.json()
        f=open('temp', 'a')
        if todo.get('ports',None) is not None:
            f.writelines('Puertos abiertos: ' + str(todo['ports']) + '\n')
        if todo['hostnames'] is not None:
            f.writelines('Hostnames: ' + str(todo['hostnames']) + '\n')
        try:
            if todo['data'][0]['http']['server'] is not None:
                f.writelines('Servidor: ' + todo['data'][0]['http']['server'] + '\n')
        except:
            f.writelines('')
        try:
            if todo['vulns'] is not None:
                f.writelines('Vulnerabilidades: ' + str(todo['vulns']) + '\n')
        except:
            f.writelines('')
        if todo['os'] is not None:
            f.writelines('Sistema operativo: ' + todo['os'] + '\n')
        f.close()
