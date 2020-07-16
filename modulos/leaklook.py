import requests, json


def analyze_leak(api_key, q, cual):
    if q == '2':
            typ = 'email_address'
    da={"key": api_key, "type": typ , "query":cual}
    res = requests.post('https://leak-lookup.com/api/search' , data=da)
    todo=res.json()
    f=open('temp','a')
    f.writelines('Listado de breachs: \n')
    for x in todo['message']:
        f.writelines(x + '\n')
    f.close()

