# Importamos las libreías
import requests
import json

def email_search(api_key, dom_email):

    HUNTER_API_KEY = api_key
    domain = dom_email
    # Se hace la petición a email hunter
    response = requests.get("https://api.hunter.io/v2/domain-search?domain="+domain+"&limit=5&api_key="+HUNTER_API_KEY)

      # Se obtiene la respuesta en formato JSON
    emails = response.json()

    # Diccionario principal donde se almacenarán todos los diccionarios generados por cada email
    dict_mails = {}

    # Añadimos el campo del nombre de la organización
    dict_mails.update({"organization":emails["data"]["organization"]})

    # Definimos el array donde se guardará una lista de todos los emails encontrados
    array_mails = []

    # Se recorren todos los emails
    for email in emails["data"]["emails"]:

        # Por cada email se genera un diccionario con datos por defecto que luego se van actualizando
        dict_mail = {"email" : [], "type": None,"confidence": None,"first_name": None,"last_name": None,"position": None,"seniority":None,"department":None,"linkedin":None,"twitter":None,"phone_number":[]}
    
         # Se comprueba si se tiene el campo de información y se añade al diccionario
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
        # Añadimos la url de las fuentes de donde se ha sacado la información
        for source in email["sources"]:
            sources.append(source["uri"])
        dict_mail.update({"sources":sources})

        # Añadimos este email al array de emails
        array_mails.append(dict_mail)

# Añadimos el array de emails al diccionario principal
    dict_mails.update({"emails":array_mails})


# Diccionario con toda la información de un dominio adaptada a un diccionario
# Esta variable es la que se devolvería si este script fuera un módulo en sí
#print(dict_mails)
#return dict_mails
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