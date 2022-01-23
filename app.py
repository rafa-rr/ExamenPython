from cgi import test
from lib2to3.pgen2 import token
import requests
import json

from flask import Flask
app = Flask(__name__)
toquen='4bd8dda5-9f21-66f4-e929-49c4bb76c4dd'


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/pregunta_uno/<numero>', methods=['GET'])
def pregunta_uno(numero):
    secuencia=''
    cantidad=0
    for i in range(1,int(numero)+1):
        secuencia+=str(i)
        cantidad= len(secuencia)
    res="{ numero: "+str(numero)+ ", secuencia: "+ str(secuencia)+ ", cantidad: "+ str(cantidad)+"}"
    return res

@app.route('/pregunta_dos/<entidad_federativa>', methods=['GET'])
def pregunta_dos(entidad_federativa):
    url='https://www.inegi.org.mx/app/api/denue/v1/consulta/BuscarEntidad/todos/'+str(entidad_federativa)+'/1/100/'+str(toquen)

    response= requests.get(url)
    # content= json.loads(response)
    res= response.json()
    
    l_return={}
    negocio=0
    if len(res)>0:
        for i in res:
            negocio += 1
            l_return['negocio_'+str(negocio)]=i
        return l_return
    else:
        return 'error en la peticion' 

    return "{error: 'problemas con el servidor inegi'}"