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

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Buscar los n videos con más LIKES para una categoría específica")

catalog = None


def loadData(catalog):
    return controller.loadData(catalog)



def initCatalog(tipo, loadfactor):
    return controller.initCatalog(tipo, loadfactor)
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        tipo = input("Ingrese el tipo de manejo de colisiones: ")
        loadfactor = float(input("Ingrese el factor de carga: "))
        print("Cargando información de los archivos ....")
        catalogo = initCatalog(tipo, loadfactor)
        requerimientos = loadData(catalogo)
        controller.loadIndice_categorias(catalogo)
        print("Información cargada.")
        print("Tiempo [ms]: ", f"{requerimientos[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{requerimientos[1]:.3f}")
    elif int(inputs[0]) == 2:
        categoria = input("Ingrese el nombre de la categoría: ")
        numero = int(input("ingrese el numero de videos que quiere consultar: "))
        print(controller.buscarvideoslikescategorias(catalogo,categoria,numero))
    else:
        sys.exit(0)
sys.exit(0)
