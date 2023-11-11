from django.http import HttpResponse
import datetime
from django.shortcuts import render

from django.template import Context, Template


class Persona:
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido


def saludo(request):
    p1 = Persona("Sergio", "Guijarro")

    temasDelCurso = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]

    ahora = datetime.datetime.now()

    diccionario = {
        "nombre_persona": p1._nombre,
        "apellido_persona": p1._apellido,
        "momento_actual": ahora,
        "temas": temasDelCurso,
    }

    return render(request, "miplantilla.html", diccionario)


def despedida(request):
    return HttpResponse("Hasta luego alumnos")


def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    documento = (
        """
        <html>
        <body>
        <h1>Fecha y hora actuales %s</h1>
        </body>
        </html>"""
        % fecha_actual
    )

    return HttpResponse(documento)


def calculaEdad(request, edad, agno):
    periodo = agno - 2023
    edadFutura = edad + periodo
    documento = """<html>
        <body>
        <h2>En el año %s tendrás %s años    
        </body>
        </html>""" % (
        agno,
        edadFutura,
    )
    return HttpResponse(documento)


def cursoC(request):
    fecha_actual = datetime.datetime.now()

    return render(request, "CursoC.html", {"dameFecha": fecha_actual})
