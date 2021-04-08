"""
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
def NuevoCatalogo(tipo, loadfactor):
    catalogo = {
        "videos": None,
        "categorias": None,
        "indice_categorias": None
    }
    catalogo["videos"] = lt.newList("ARRAY_LIST")
    catalogo["categorias"] = lt.newList("ARRAY_LIST")
    catalogo["indice_categorias"] = mp.newMap(40,
                                  maptype=tipo,
                                  loadfactor=loadfactor)
    return catalogo

# Funciones para agregar informacion al catalogo


def addVideo(catalogo, video):
    lt.addLast(catalogo["videos"], video)


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


# Funciones utilizadas para comparar elementos dentro de una lista


def cmpVideosByViews(video1, video2):
    return (int(video1["views"]) > int(video2["views"]))


def cmpVideosByLikes(video1, video2):
    return (int(video1["likes"]) < int(video2["likes"]))

def cmpVideosByAppearances(video1, video2):
    return (int(video1["apariciones"]) > int(video2["apariciones"]))
# Funciones de ordenamiento

def buscarvideoslikescategorias(catalogo, categoria,numero):
    lista = mp.get(catalogo["indice_categorias"],categoria)["value"].copy()
    listasorteada = sa.sort(lista, cmpVideosByLikes)
    return lt.subList(listasorteada,0,numero)

