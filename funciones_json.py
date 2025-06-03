import json

def datos():
    granListaDeDatos={}
    with open("./el_json/datos.json",'r') as openFile:
        granListaDeDatos=json.load(openFile)
    return granListaDeDatos

def datos(dic):
    with open("./el_json/datos.json",'w') as outFile:
        json.dump(dic,outFile)
