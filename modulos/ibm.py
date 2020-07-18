import requests

def analyze_xforce(api_key , passw , q , t):
    
    if t == '1':
        res = requests.get('https://api.xforce.ibmcloud.com/ipr/' + q , auth=(api_key,passw))
        todo=res.json()
        f=open('temp','a')
        p=str(todo['cats'])
        u=p[2:7]
        r=p[9:11]
        f.writelines('Según IBM X-Force Exchange esta IP está categorizada como  '+ u + ' con un '+ r +'%\n')
        f.close()