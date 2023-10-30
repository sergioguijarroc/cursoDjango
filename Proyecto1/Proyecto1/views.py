from django.http import HttpResponse
import datetime


def saludo(request):
    documento = """
        <html>
        <body>
        <h1>Hola alumnos esta es nuestra primera página</h1>
        </body>
        </html>"""

    return HttpResponse(documento)


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
