import requests


def analyze_blockchain(q):
    if len(q) == 64:
        res=requests.get('https://blockchain.info/rawtx/' + q)
        todo=res.json()
        f=open('temp','a')
        ad=str(todo['inputs'][0]['prev_out']['addr'])
        va=str(todo['inputs'][0]['prev_out']['value'])
        f.writelines('1')
        f.writelines('Desde la dirección ' + ad + 'se envia la cantidad de ' + va +' a\n')
        for x in todo['out']:
             f.writelines('Envío de ' +  str(x['value']) + ' a la dirección ' +  str(x['addr']) + '\n')
        f.close()
    if len(q) == 34:
        res=requests.get('https://blockchain.info/rawaddr/'+ q)
        todo=res.json()
        f=open('temp','a')
        f.writelines('2')
        f.writelines('Total transacciones recibidas: ' + str(todo['total_received']) +'\n')
        f.writelines('Total transacciones enviadas: ' + str(todo['total_sent']) +'\n')
        f.writelines('Balance final: ' + str(todo['final_balance']) +'\n')
        f.close()

    