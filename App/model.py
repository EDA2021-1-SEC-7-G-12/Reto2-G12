﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as ms
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def NuevoCatalogo():
    catalogo = {
        "videos": None,
        "categorias": None,
    }
    catalogo["videos"] = mp.newMap(40,
                                  maptype="PROBING")
    catalogo["categorias"] = lt.newList("ARRAY_LIST")
    return catalogo

# Funciones para agregar informacion al catalogo


def addVideo(catalogo, video):
    mp.put(catalogo["videos"], str(video["video_id"]) + str(video["trending_date"])  + str(video["country"]), video)
#Esa llave para cada video se usa para que el mismo video en distintos paises y en distintas fechas no sea reemplazado por solo una instancia de este video.

def addCategoria(catalogo, categoria):
    
    cat = newCategoria(categoria['id'], categoria['name'])
    lt.addLast(catalogo['categorias'], cat)


# Funciones para creacion de datos

def newCategoria(id, name):
    categoria = {'id': '', 'name': ''}
    categoria['id'] = id
    categoria['name'] = name
    return categoria

def loadIndice_categorias(catalogo): 
    for x in catalogo["videos"]["elements"]:
        if not mp.contains(catalogo["indice_categorias"], sacarcategoriaid(catalogo, x["category_id"])):
            listavacia = lt.newList("ARRAY_LIST")
            lt.addLast(listavacia, x)
            mp.put(catalogo["indice_categorias"], sacarcategoriaid(catalogo, x["category_id"]), listavacia)
        else:
            lt.addLast(mp.get(catalogo["indice_categorias"], sacarcategoriaid(catalogo, x["category_id"]))["value"],x)

# Funciones de consulta



def sacaridcategoria(catalogo, nombre_categoria):
    lista = catalogo["categorias"]
    categoria = -1
    for x in range(lista["size"]):
        elemento = lt.getElement(lista, x)
        if elemento["name"] == nombre_categoria:
            categoria = elemento["id"]
    return categoria

def sacarcategoriaid(catalogo, idcategoria):
    lista = catalogo["categorias"]
    categoria = -1
    for x in range(lista["size"]):
        elemento = lt.getElement(lista, x)
        if str(elemento["id"]) == str(idcategoria):
            categoria = elemento["name"]
    return categoria

def videospaiscategoría(numero,pais,categoria,catalogo):
    category = sacaridcategoria(catalogo,categoria)
    mapacondiciones = mp.newMap(40, maptype="PROBING")
    videos = mp.valueSet(catalogo["videos"])
    for x in range(mp.valueSet(catalogo["videos"])["size"]):
        video = lt.getElement(videos,x)
        if (video["country"] == pais) and (int(video["category_id"]) == int(category)):
            mp.put(mapacondiciones,str(video["video_id"]) + str(video["trending_date"]) + str(video["country"]),video)
    sorteado = sa.sort(mp.valueSet(mapacondiciones),cmpVideosByViews)
    listavideos = lt.subList(sorteado, 1, int(numero))
    return listavideos


def videos_a_dias_trending(videos):
    lst = lt.newList("ARRAY_LIST")
    listaids = []
    for i in range(mp.valueSet(videos["videos"])["size"]):
        if not i["video_id"] == "#NAME?":
            if not i["video_id"] in listaids:
                listaids.append(i["video_id"])
                lt.addFirst(lst, {"id" : i["video_id"], "apariciones": 1})
            else:
                for y in lst["elements"]:
                    if y["id"] == i["video_id"]:
                        y["apariciones"] += 1
    diccionariosorteado = ms.sort(lst, cmpVideosByAppearances)
    return diccionariosorteado


def topdiastrendingporpais(catalogo, pais):
    catalog2 = mp.newMap(40, maptype="PROBING")
    vids=mp.valueSet(catalogo["videos"])
    for i in range(mp.valueSet(catalogo["videos"])["size"]):
        video= lt.getElement(vids, i)
        if (pais == video["country"]):
             mp.put(catalog2, str(video["title"]), video)
    respuesta = ""
    ordenado = videos_a_dias_trending(catalog2)
    for i in catalog2["elements"]:
        if i["video_id"] == ordenado["elements"][0]["id"]:
            respuesta = i
    return respuesta, sorteado["elements"][0]["apariciones"]

# Funciones utilizadas para comparar elementos dentro de una lista


def cmpVideosByViews(video1, video2):
    return (int(video1["views"]) > int(video2["views"]))


def cmpVideosByLikes(video1, video2):
    return (int(video1["likes"]) > int(video2["likes"]))

def cmpVideosByAppearances(video1, video2):
    return (int(video1["apariciones"]) > int(video2["apariciones"]))
# Funciones de ordenamiento

def buscarvideoslikescategorias(catalogo, categoria,numero):
    lista = mp.get(catalogo["indice_categorias"],categoria)["value"].copy()
    listasorteada = sa.sort(lista, cmpVideosByLikes)
    return lt.subList(listasorteada,0,numero)

