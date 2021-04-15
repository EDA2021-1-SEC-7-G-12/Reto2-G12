"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printResults(ord_videos, mostrardos):
    size = lt.size(ord_videos)
    if size >= mostrardos:
        print("Los primeros ", mostrardos, " videos ordenados son:")
        i = 1
        while i <= mostrardos:
            video = lt.getElement(ord_videos, i)
            print('Trending date: ' + video['trending_date'] + ' Title: ' +
                  video['title'] + ' Channel title: ' + video['channel_title']
                  + ' Publish time: ' + video['publish_time'] + ' Views: ' +
                  video['views'] + ' Likes: ' + video['likes'] + ' Dislikes: '
                  + video['dislikes'])
            i += 1


def printResultPais(video, dias):
    print(' Title: ' +
                  video['title'] + ' Channel title: ' + video['channel_title']
                  + ' Country: ' + video['country'] + ' Dias: ' +
                  str(dias))


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Buscar los videos con más views en un pais específico y una categoría de interés")
    print("3- Buscar el video con mas días siendo tendencia en un país de interés")
    print("4- Buscar el video con mas días siendo tendencia en una categoría de interés")
    print("5- Buscar los videos con más likes en un pais específico y con una etiqueta específica")
catalog = None


def loadData(catalog):
    return controller.loadData(catalog)



def initCatalog():
    return controller.initCatalog()

def videospaiscategoria(numero, pais, categoria, catalogo):
    return controller.videospaiscategoría(numero,pais,categoria,catalogo)
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalogo = initCatalog()
        loadData(catalogo)
        #controller.loadIndice_categorias(catalogo)
        print("Información cargada.")
    
    elif int(inputs[0]) == 2:
        numero = int(input("ingrese el numero de videos que desea consultar: "))
        pais = input("Ingrese el país de su interés: ")
        categoria = input("Ingrese la categoría de su interés: ")
        videos = videospaiscategoria(numero, pais, categoria, catalogo)
        printResults(videos, int(numero))

    elif int(inputs[0]) == 3:
        pais = input("Ingrese el país de su interés: ")
        resultado = controller.topdiastrendingporpais(catalogo, pais)
        printResultPais(resultado[0], resultado[1])

    elif int(inputs[0]) == 4:
        categoria = input("Ingrese la categoría de su interés: ")
        resultado = controller.topdiastrendingporcategoria(catalogo, categoria)
        print(resultado)
        
    elif int(inputs[0]) == 5:
        numero = int(input("ingrese el numero de videos que desea consultar: "))
        pais = input("Ingrese el país de su interés: ")
        tag = input("Ingrese la etiqueta de su interés: ")
    else:
        sys.exit(0)
sys.exit(0)
