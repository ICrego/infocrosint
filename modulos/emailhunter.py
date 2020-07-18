import requests
import json

def email_search(api_key, dom_email):

    HUNTER_API_KEY = api_key
    domain = dom_email
    response = requests.get("https://api.hunter.io/v2/domain-search?domain="+domain+"&limit=5&api_key="+HUNTER_API_KEY)
    emails = response.json()

    dict_mails = {}
    dict_mails.update({"organization":emails["data"]["organization"]})
    array_mails = []

    for email in emails["data"]["emails"]:
        dict_mail = {"email" : [], "type": None,"confidence": None,"first_name": None,"last_name": None,"position": None,"seniority":None,"department":None,"linkedin":None,"twitter":None,"phone_number":[]}
        if(email["value"] != []):
            dict_mail.update({"email" : [email["value"]]})
        if(email["type"] != None):
            dict_mail.update({"type": email["type"]})
        if(email["confidence"] != None):
            dict_mail.update({"confidence": email["confidence"]})
        if(email["first_name"] != None):
            dict_mail.update({"first_name": [email["first_name"]]})
        if(email["last_name"] != None):
            dict_mail.update({"last_name": [email["last_name"]]})
        if(email["position"] != None):
            dict_mail.update({"position": email["position"]})
        if(email["seniority"] != None):
            dict_mail.update({"seniority": email["seniority"]})
        if(email["department"] != None):
            dict_mail.update({"department": email["department"]})
        if(email["linkedin"] != None):
            dict_mail.update({"linkedin": [email["linkedin"]]})
        if(email["twitter"] != None):
            dict_mail.update({"twitter":[email["twitter"]]})
        if(email["phone_number"] != None):
            dict_mail.update({"phone_number":[email["phone_number"]]})
        sources = []

        for source in email["sources"]:
            sources.append(source["uri"])
        dict_mail.update({"sources":sources})
        array_mails.append(dict_mail)
    dict_mails.update({"emails":array_mails})

    f = open('temp', 'a')
    f.writelines('Listados de Emails asociados al dominio '+domain)
    for v in dict_mails['emails']:
            f.writelines('Email: ')
            f.writelines(v['email'])
            f.writelines('\n')
            if v['first_name'] is None:
                f.writelines('\n')
            else:
                f.writelines('Nombre: ')
                f.writelines(v['first_name'])
                f.writelines('\n')
            if v['last_name'] is None:
                f.writelines('\n')
            else:
                f.writelines('Apellido: ')
                f.writelines(v['last_name'])
                f.writelines('\n')
            if v['type'] is None:
                f.writelines('\n')
            else:
                f.writelines('Tipo de cuenta: ')
                f.writelines(v['type'])
                f.writelines('\n')
            if v['department'] is None:
                f.writelines('\n')
            else:
                f.writelines('Departamento')
                f.writelines(v['department'])
                f.writelines('\n')
            if v['linkedin'] is None:
                f.writelines('\n')
            else:
                f.writelines('Cuenta de LinkedIn: ')
                f.writelines(v['linkedin'])
                f.writelines('\n')
            if v['twitter'] is None:
                f.writelines('\n')
            else:
                f.writelines('Cuenta de Twitter: ')
                f.writelines(v['twitter'])
                f.writelines('\n')
            if v['phone_number'] is None:
                f.writelines('\n')
            else:
                f.writelines('Teléfono: ')
                f.writelines(v['phone_number'])
                f.writelines('\n')
            f.writelines('Fuentes: ')
            f.writelines('\n')
            for sourc in v['sources']:
                f.writelines(sourc)
                f.writelines('\n')
            f.writelines('============================================================= \n')
    f.close()