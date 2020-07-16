import requests

def analyze_builtwith(api_key , q , t):
    res=requests.get('https://api.builtwith.com/v14/api.json?KEY=' + api_key + '&LOOKUP=' + q)
    
    todo=res.json()
    print(todo)