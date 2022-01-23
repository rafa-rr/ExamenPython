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

