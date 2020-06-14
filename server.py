#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# pythones.net

#from conection import insert_function,importMultiple, cargarFuncion,traerFuncion, login, verify_reference_code, insert_reference, search_function,get_functions

from flask import Flask,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
"""
@app.route("/verify_user", methods=['POST'])
def ver_user():
    print("useerr",request.form['user_id'],request.form['password'])
    return (login(request.form['user_id'],request.form['password']))


@app.route("/cargar_funcion/<int:codigoFuncion>", methods=['GET'])
def cargar_funcion(codigoFuncion):
    codigos = cargarFuncion(codigoFuncion)
    print(codigos)
    resp = traerFuncion(codigos)
    print(resp)
    return resp


@app.route("/insert_function", methods=['POST'])
def ins_function():
    return (insert_function(request.form['us_id'],request.form['params'],request.form['desc'],request.form['tags'],request.form['func_name'],request.form['js']))

@app.route("/verify_code/<int:code>", methods=['GET'])
def verify_code(code):
    return (verify_reference_code(code))

@app.route("/importMultiple/<string:code>", methods=['GET'])
def importMult(code):
    codes= importMultiple(code)
    print(codes)
    resp = traerFuncion(codes)
    print(resp)
    return resp 

@app.route("/insert_reference", methods=['POST'])
def ins_ref():
    return (insert_reference(request.form['func_code'],request.form['ref_code']))

@app.route("/search_function", methods=['POST'])
def search_func():
    return (search_function(request.form['code'],request.form['search']))
"""
@app.route("/get_functions", methods=['GET'])
def get_func():
    return ('hola mundo')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
