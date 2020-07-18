import requests, json

def analyze_intelx(api_key, q, t):
    h = {'User-Agent' : 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52' , 'x-key' : api_key}
    dat= {"term": q, "maxresults": 1000}
    r = requests.post('https://2.intelx.io/phonebook/search', headers=h, json=dat)
    if r.status_code == 200:
        uid=r.json()['id']
        resultado = requests.get('https://2.intelx.io/phonebook/search/result?id='+uid , headers=h)
        todo=resultado.json()
        f=open("temp" , "a")
        f.writelines('Emails localizados en el contenido de distintas URLs \n')
        for x in todo['selectors']:
           if x['selectortype'] == 1:
                f.writelines(str(x['selectorvalue']) + '\n')
        f.writelines('URLs :\n')
        for x in todo['selectors']:
           if x['selectortype'] == 3:
                f.writelines(str(x['selectorvalue']) + '\n')
        f.close()