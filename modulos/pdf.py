from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from datetime import datetime
import time
import itertools
import os

def formateo(c,d):
    c.line(5, 780, 590, 780)
    c.drawString(200, 800, 'INFORME '+ d)
    fecha = datetime.now().strftime("%d/%m/%y %H:%M")
    c.drawString(450, 800, 'FECHA: '+fecha)
    #c.drawString(510, 800, now)
    c.line(35 , 780 , 35 , 35) 
    # Pie del informe
    c.line(5 , 35 , 590 , 35) 
  

def  informe_mail(d,t):
    c = canvas.Canvas("reporte_ " + d + ".pdf")
    #now = date.today()
    formateo(c,d)
    cont=1
    text = c.beginText(50 , 750)
    if t == '2':
        text.textLine('Listados de breachs en los que aparece el email '+ d)
    if t == '4':
        text.textLine('Listados de Emails asociados al dominio '+ d)
    f = open('temp', 'r')
    for linea in f:
       if cont == 50:
          c.drawText(text)
          c.showPage()
          cont=0
          formateo(c,d)
          text = c.beginText(50 , 750)
       else:
            if linea != '\n':
                linea = linea.rstrip()
                text.textLine(linea)
                cont=cont+1
    f.close()
    c.drawText(text)
    c.showPage()
    c.save()
    os.remove('temp')

def informe_dominio(dom):
    c = canvas.Canvas("reporte_" + dom + ".pdf")
    #now = date.today()
    formateo(c,dom)
    cont=1
    text = c.beginText(50 , 750)
    text.textLine('Datos asociados asociados al dominio '+ dom)
    f = open('temp', 'r')
    for linea in f:
        if cont == 50:
            c.drawText(text)
            c.showPage()
            cont=0
            formateo(c,dom)
            text = c.beginText(50 , 750)
        else:
          if linea != '\n':
            linea = linea.rstrip()
            text.textLine(linea)
            cont=cont+1
    f.close()
    c.drawText(text)
    c.showPage()
    c.save()
    os.remove('temp')
    
def informe_ip(ip):
    c = canvas.Canvas("reporte_" + ip + ".pdf")
    formateo(c,ip)
    cont=1
    text = c.beginText(50 , 750)
    text.textLine('Datos asociados asociados a la IP '+ ip)
    f=open("temp" , "r")
    for linea in f:
        if cont == 50:
            c.drawText(text)
            c.showPage()
            cont=0
            formateo(c,ip)
            text = c.beginText(50 , 750)
        else:
          if linea != '\n':
            linea = linea.rstrip()
            text.textLine(linea)
            cont=cont+1
    f.close()
    c.drawText(text)
    c.showPage()
    c.save()
    os.remove('temp')
    
def informe_block(cual):
    c = canvas.Canvas("reporte_" + cual + ".pdf")
    if len(cual)==64:
        que="Transacción"
    if len(cual)==34:
        que="Monedero"
    formateo(c,que)
    cont=1
    text = c.beginText(50 , 750)
    text.textLine('Información sobre '+ cual)
    f=open("temp" , "r")
    for linea in f:
        if cont == 50:
            c.drawText(text)
            c.showPage()
            cont=0
            formateo(c,ip)
            text = c.beginText(50 , 750)
        else:
          if linea != '\n':
            linea = linea.rstrip()
            text.textLine(linea)
            cont=cont+1
    f.close()
    c.drawText(text)
    c.showPage()
    c.save()
    os.remove('temp')