from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from proyectos.models import Usuario, Equipo

usuarios="""
[
    {
        "username" : "usuario1",
        "password" : "123"
    },
    {
        "username" : "usuario2",
        "password" : "abc"
    },
    {
        "username" : "usuario3",
        "password" : "aaa"
    }
]
"""

equipos= """
[
    {
        "nombre" : "Equipo 1",
        "integrantes" : [
            {
                "nombre" : "N1",
                "codigo" : "20202323"
            },
            {
                "nombre" : "N2",
                "codigo" : "20224533"
            }
        ]
    },
    {
        "nombre" : "Equipo 2",
        "integrantes" : [
            {
                "nombre" : "N3",
                "codigo" : "20202323"
            },
            {
                "nombre" : "N4",
                "codigo" : "20224533"
            }
        ]
    }
]
"""

def verEquiposEndpoint(request):
    if request.method== "GET":
        nombreFiltro=request.GET.get("nombre")

        #Reemplazado por lambda
        ##def filtro(equipo):
        ##    print(equipo["nombre"])
        ##    return equipo["nombre"].lower()==nombreFiltro

        if nombreFiltro == "":
            listaEquiposFiltrada= Equipo.objects.all()
        else:
            listaEquiposFiltrada= Equipo.objects.filter(nombre__contains=nombreFiltro)

        #listaEquipos= json.loads(equipos)
        
        #Reemplazado por lambda
        #listaEquiposFiltrada=list(filter(filtro, listaEquipos))
        
        # listaEquiposFiltrada=list(
        #    filter(
        #        lambda x: x["nombre"].lower()==nombreFiltro, 
        #        listaEquipos)) 
        #return HttpResponse(json.dumps(listaEquiposFiltrada))

        dataResponse=[]
        for equipo in listaEquiposFiltrada:
            dataResponse.append({
                "nombre": equipo.nombre,
                "integrantes": []
            })

        return HttpResponse(json.dumps(dataResponse))
    #return HttpResponse(equipos)

def verEquiposPathParametersEndpoint(request, filtro):
    if request.method== "GET":
        nombreFiltro=filtro

        listaEquipos= json.loads(equipos)
        listaEquiposFiltrada=list(
            filter(
                lambda x: x["nombre"].lower()==nombreFiltro, 
                listaEquipos))
        return HttpResponse(json.dumps(listaEquiposFiltrada))
    return HttpResponse(equipos)

#Path: /proyectos/login GET
def loginEndpoint(request, username, password):
    if request.method == "GET":
        #Peticion GET
        listaUsuarios=json.loads(usuarios)
        listaUsuariosFiltrada=list(
            filter(
                lambda x:x["username"]==username and x["password"]==password,
                listaUsuarios
            )
        )

        if len(listaUsuariosFiltrada)>0:
            respuesta={
                "msg":""
            }
            return HttpResponse(json.dumps(respuesta))
        else:
            respuesta={
                "msg": "Error en el login"
            }
            return HttpResponse(json.dumps(respuesta))


@csrf_exempt
def loginPostEndpoint(request):
    if request.method=="POST":
        username= request.POST.get("username")
        password= request.POST.get("password")
        
        listaUsuarios=json.loads(usuarios)
        listaUsuariosFiltrada=list(
            filter(
                lambda x:x["username"]==username and x["password"]==password,
                listaUsuarios
            )
        )

        if len(listaUsuariosFiltrada)>0:
            respuesta={
                "msg":""
            }
            return HttpResponse(json.dumps(respuesta))
        else:
            respuesta={
                "msg": "Error en el login"
            }
            return HttpResponse(json.dumps(respuesta))

@csrf_exempt
def loginPostJsonEndpoint(request):
    if request.method == "POST":
        data=request.body
        usernameData= json.loads(data)
        
        username=usernameData["username"]
        password=usernameData["password"]

        listaUsuariosFiltrada = Usuario.objects.filter(
            username=username, password=password
        )
        
        ##sin bd (desde usernameData=json.loads(data))
        ##listaUsuarios=json.loads(usuarios)
        ##listaUsuariosFiltrada=list(
        ##    filter(
        ##        lambda x:x["username"]==usernameData["username"] and x["password"]==usernameData["password"],
        ##        listaUsuarios
        ##    )
        ##)

        if len(listaUsuariosFiltrada)>0:
            respuesta={
                "msg":""
            }
            return HttpResponse(json.dumps(respuesta))
        else:
            respuesta={
                "msg": "Error en el login"
            }
            return HttpResponse(json.dumps(respuesta))