import json
from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
from datetime import datetime
import codecs
import configparser
import csv
import base64

# import connexion
from db import cnxnweek

config = configparser.ConfigParser()
config.read('config.ini')

origins = config.get('CORS', 'origins')

app = Blueprint('Week', __name__)

CORS(app, origins=origins)

def guardar_en_csv_y_mostrar_base64(json_data, nombre_archivo):
    # Convierte el objeto JSON en una lista de listas para que pueda ser escrita en un archivo CSV
    datos_csv = []
    for key in json_data.keys():
        fila = [key, json_data[key]]
        datos_csv.append(fila)

    # Escribe los datos en un archivo CSV
    with open(nombre_archivo + '.csv', 'w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerows(datos_csv)

    # Lee los datos del archivo CSV y los codifica en Base64
    with open(nombre_archivo + '.csv', 'rb') as archivo_csv:
        datos_csv = archivo_csv.read()
        datos_base64 = base64.b64encode(datos_csv).decode('utf-8')

    # Muestra los datos codificados en Base64
    return {'Base64': datos_base64}

# 1- metodos originales
@app.route("/PostDataWeek", methods=["POST"])
def get_Week():
    if request.is_json:
        json_data = request.get_json()

        # Variables que se desea formatear
        variables = [
            "startDate",
            "endDate",
        ]

        for variable in variables:
            # Se obtiene el valor de la variable del JSON
            valor = json_data.get(variable)
            if valor is not None:
                # La variable está presente en el JSON de entrada
                # Se formatea con la sintaxis SQL deseada
                sql_variable = f"@{variable} = '{valor}'"
                # Se agrega la variable al JSON de respuesta
                json_data[variable] = sql_variable

        SPaEjecutar = "SP_TotalMailsByStatusAndWeek " + ", ".join(
            str(value) if value is not None else "" for value in json_data.values()
        )

        print(SPaEjecutar)

        cursor = cnxnweek.cursor()
        cursor.execute(SPaEjecutar)

        rows = cursor.fetchall()

        # cnxnweek.close()

        if len(rows) > 0:
            # Creamos una lista de diccionarios donde cada diccionario representa una fila del resultado
            result_list = []
            for row in rows:
                result_dict = {}
                for index, column in enumerate(cursor.description):
                    column_name = column[0]
                    column_value = row[index]
                    if isinstance(column_value, datetime):
                        # Convertimos la fecha en una cadena de texto antes de agregarla al diccionario
                        column_value = column_value.strftime(
                            "%Y-%m-%d %H:%M:%S")
                    elif isinstance(column_value, bytes):
                        # Convertimos los datos binarios a una cadena de caracteres
                        column_value = codecs.decode(column_value, "utf-8")
                    result_dict[column_name] = column_value
                result_list.append(result_dict)

            # output_dict = {"Cantidad": len(rows), "Radicados": result_list}

            # Convertimos la lista de diccionarios en un objeto JSON
            json_output = json.dumps(result_list)
            # cursor.close()
            # cnxnweek.close()
            return json_output, 200
        else:
            # cursor.close()
            # cnxnweek.close()
            return (
                jsonify(
                    {"error": "No hay Radicados que coincidan con el criterio de busqueda."}),
                404,
            )
    else:
        SPaEjecutar = "SP_TotalMailsByStatusAndWeek "
        print(SPaEjecutar)

        cursor = cnxnweek.cursor()
        cursor.execute(SPaEjecutar)

        rows = cursor.fetchall()

        # cnxnweek.close()

        if len(rows) > 0:
            # Creamos una lista de diccionarios donde cada diccionario representa una fila del resultado
            result_list = []
            for row in rows:
                result_dict = {}
                for index, column in enumerate(cursor.description):
                    column_name = column[0]
                    column_value = row[index]
                    if isinstance(column_value, datetime):
                        # Convertimos la fecha en una cadena de texto antes de agregarla al diccionario
                        column_value = column_value.strftime(
                            "%Y-%m-%d %H:%M:%S")
                    elif isinstance(column_value, bytes):
                        # Convertimos los datos binarios a una cadena de caracteres
                        column_value = codecs.decode(column_value, "utf-8")
                    result_dict[column_name] = column_value
                result_list.append(result_dict)

            output_dict = {"Totales": result_list}

            # Convertimos la lista de diccionarios en un objeto JSON
            json_output = json.dumps(output_dict)
            # cursor.close()
            # cnxnweek.close()
            return json_output, 200
        else:
            # cursor.close()
            # cnxnweek.close()
            return (
                jsonify(
                    {"error": "No hay Radicados que coincidan con el criterio de busqueda."}),
                404,
            )

# 2- metodos nuevos para csv
@app.route("/PostDataWeek_CSV", methods=["POST"])
def get_Week_CSV():
    if request.is_json:
        json_data = request.get_json()

        # Variables que se desea formatear
        variables = [
            "startDate",
            "endDate",
        ]

        for variable in variables:
            # Se obtiene el valor de la variable del JSON
            valor = json_data.get(variable)
            if valor is not None:
                # La variable está presente en el JSON de entrada
                # Se formatea con la sintaxis SQL deseada
                sql_variable = f"@{variable} = '{valor}'"
                # Se agrega la variable al JSON de respuesta
                json_data[variable] = sql_variable

        SPaEjecutar = "SP_TotalMailsByStatusAndWeek " + ", ".join(
            str(value) if value is not None else "" for value in json_data.values()
        )

        print(SPaEjecutar)

        cursor = cnxnweek.cursor()
        cursor.execute(SPaEjecutar)

        rows = cursor.fetchall()

        # cnxnweek.close()

        if len(rows) > 0:
            # Creamos una lista de diccionarios donde cada diccionario representa una fila del resultado
            result_list = []
            for row in rows:
                result_dict = {}
                for index, column in enumerate(cursor.description):
                    column_name = column[0]
                    column_value = row[index]
                    if isinstance(column_value, datetime):
                        # Convertimos la fecha en una cadena de texto antes de agregarla al diccionario
                        column_value = column_value.strftime(
                            "%Y-%m-%d %H:%M:%S")
                    elif isinstance(column_value, bytes):
                        # Convertimos los datos binarios a una cadena de caracteres
                        column_value = codecs.decode(column_value, "utf-8")
                    result_dict[column_name] = column_value
                result_list.append(result_dict)

            # output_dict = {"Cantidad": len(rows), "Radicados": result_list}

            # Convertimos la lista de diccionarios en un objeto JSON
            json_output = json.dumps(result_list)
            # cursor.close()
            # cnxnweek.close()
            nombre_archivo = 'ConsultaSemana'
            resultado = guardar_en_csv_y_mostrar_base64(
                result_list, nombre_archivo)

            return jsonify({"Nombre": nombre_archivo, "Archivo": resultado}), 200
        else:
            # cursor.close()
            # cnxnweek.close()
            return (
                jsonify(
                    {"error": "No hay Radicados que coincidan con el criterio de busqueda."}),
                404,
            )
    else:
        SPaEjecutar = "SP_TotalMailsByStatusAndWeek "
        print(SPaEjecutar)

        cursor = cnxnweek.cursor()
        cursor.execute(SPaEjecutar)

        rows = cursor.fetchall()

        # cnxnweek.close()

        if len(rows) > 0:
            # Creamos una lista de diccionarios donde cada diccionario representa una fila del resultado
            result_list = []
            for row in rows:
                result_dict = {}
                for index, column in enumerate(cursor.description):
                    column_name = column[0]
                    column_value = row[index]
                    if isinstance(column_value, datetime):
                        # Convertimos la fecha en una cadena de texto antes de agregarla al diccionario
                        column_value = column_value.strftime(
                            "%Y-%m-%d %H:%M:%S")
                    elif isinstance(column_value, bytes):
                        # Convertimos los datos binarios a una cadena de caracteres
                        column_value = codecs.decode(column_value, "utf-8")
                    result_dict[column_name] = column_value
                result_list.append(result_dict)

            output_dict = {"Totales": result_list}

            # Convertimos la lista de diccionarios en un objeto JSON
            json_output = json.dumps(output_dict)
            # cursor.close()
            # cnxnweek.close()
            nombre_archivo = 'ConsultaSemana_SF'
            resultado = guardar_en_csv_y_mostrar_base64(
                result_list, nombre_archivo)

            return jsonify({"Nombre": nombre_archivo, "Archivo": resultado}), 200
        else:
            # cursor.close()
            # cnxnweek.close()
            return (
                jsonify(
                    {"error": "No hay Radicados que coincidan con el criterio de busqueda."}),
                404,
            )