# -*- coding:utf-8 -*-

import os , json , sys
from modulos import config
from modulos import ipgeolocation
from modulos import emailhunter
from modulos import censys
from modulos import shodan
from modulos import ipinfo
#from modulos import cymon
from modulos import viewdns
from modulos import clearbit
from modulos import securitytrails
from modulos import builtwith
from modulos import virustotal
from modulos import threatcrowd
from modulos import otx
from modulos import riskiq
from modulos import hybrid_analysis
from modulos import ibm
from modulos import intelx
from modulos import blockchain
from modulos import binaryedge
from modulos import zoomeye
from modulos import leaklook
from modulos import dehashed
from modulos import fraudguard
from modulos import pdf


os.system ('clear')


def info_ip(ip):
    t = '1'
    ipgeolocation.analyze(config.IPGEOLOCATION_API_KEY, ip)
    shodan.analyze_shodan(config.SHODAN_API_KEY , ip ,t )
    ipinfo.analyze_ipinfo(config.IPINFO_API_KEY, ip)
    censys.analyze_censys(config.CENSYS_UID , config.CENSYS_SECRET , ip , t)
    threatcrowd.analyze_threatcrowd(ip , t)
    fraudguard.analyze_fraudguard(config.FRAUDGUARD_USERNAME, config.FRAUDGUARD_PASSWORD, ip)
    virustotal.analyze_virustotal(config.VIRUSTOTAL_API_KEY , ip , t)
    otx.analyze_otx(config.OTX_API_KEY , ip , t)
    riskiq.analyze_riskiq(config.RISKIQ_API_KEY, config.RISKIQ_API_SECRET, ip , t)
    ibm.analyze_xforce(config.XFORCE_API_KEY , config.XFORCE_PASSWORD , ip , t)
    pdf.informe_ip(ip)
    
    
 
 
def info_email(em): 
   t = '2'
   clearbit.analyze_clearbit(config.CLEARBIT_SK, em, t)
   binaryedge.analyze_binary(config.BINARYEDGE_API_KEY , em , t)
   dehashed.analyze_dehashed(config.DEHASHED_API_KEY, config.DEHASHED_USERNAME, em)
   leaklook.analyze_leak(config.LEAKLOOKUP_APY_KEY , t, em )
   riskiq.analyze_riskiq(config.RISKIQ_API_KEY, config.RISKIQ_API_SECRET, em , t)
   pdf.informe_mail(em , t)
   
   
   
   
   
def info_dominio(dominio):
    t = '3'
    viewdns.analyze_viewdns(config.VIEWDNS_API_KEY , dominio , t)
    securitytrails.analyze_securitytr(config.SECURITYTRAILS_API_KEY , dominio , t)
    threatcrowd.analyze_threatcrowd(dominio , t)
    virustotal.analyze_virustotal(config.VIRUSTOTAL_API_KEY , dominio , t)
    otx.analyze_otx(config.OTX_API_KEY , dominio , t)
    riskiq.analyze_riskiq(config.RISKIQ_API_KEY, config.RISKIQ_API_SECRET, dominio , t)
    emailhunter.email_search(config.EMAILHUNTED_API_KEY, dominio)
    intelx.analyze_intelx(config.INTELX_API_KEY , dominio, t)
    binaryedge.analyze_binary(config.BINARYEDGE_API_KEY , dominio , t)
    pdf.informe_dominio(dominio)
    
def info_block(cual):
    t='5'
    blockchain.analyze_blockchain(cual)
    pdf.informe_block(cual)

def ayuda():
    print("""
  ######################################################################
   _____ _   _ ______ _____ _____ ______ _____ _____ _____ _   _ _____ 
  |_   _| \ | ||  ___|  _  /  __ \| ___ \  _  /  ___|_   _| \ | |_   _|
    | | |  \| || |_  | | | | /  \/| |_/ / | | \ `--.  | | |  \| | | |  
    | | | . ` ||  _| | | | | |    |    /| | | |`--. \ | | | . ` | | |  
   _| |_| |\  || |   \ \_/ / \__/\| |\ \\  \_/ /\__/ /_| |_| |\  | | |  
   \___/\_| \_/\_|    \___/ \____/\_| \_|\___/\____/ \___/\_| \_/ \_/  
                                             
  ######################################################################
    Usage: python infocrosint.py [OPTIONS]
    
    Ejemplo: python3 infocrosint.py -d dominio.com
    
    [OPTIONS]
    -h   Ayuda
    -d   Dominio         midominio.es
    -i   Ip              X.X.X.X
    -e   Email           direccion@email.com
    -c   Criptomonedas   direccion de monedero o hash de transaccion
    
    """)


if __name__ == "__main__":
    argumento = len(sys.argv)
    i=0
    for arg in sys.argv:
        if argumento != 3:
            os.system ('clear')
            ayuda()
        if argumento == 3:
            if arg == '-h':
                ayuda()
            if arg == '-d':
                info_dominio(sys.argv[2])
            if arg == '-i':
                info_ip(sys.argv[2])
            if arg == '-e':
                info_email(sys.argv[2])
            if arg == '-c':
                info_block(sys.argv[2])