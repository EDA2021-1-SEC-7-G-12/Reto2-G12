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
 """

import config as cf
import model
import csv
import time
import tracemalloc


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.NuevoCatalogo()
    return catalog



# Funciones para la carga de datos
def loadData(catalogo):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """

    loadVideos(catalogo)
    loadCategorias(catalogo)


def loadVideos(catalogo):
    videosfile = cf.test_dir + 'videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalogo, video)


def loadCategorias(catalogo):
    categoriasfile = cf.test_dir + 'category-id.csv'
    input_file = csv.DictReader(open(categoriasfile, encoding='utf-8'))
    for categoria in input_file:
        model.addCategoria(catalogo, categoria)

def loadIndice_categorias(catalogo):
    model.loadIndice_categorias(catalogo)
# Funciones de ordenamiento
def buscarvideoslikescategorias(catalogo,categoria,numero):
    return model.buscarvideoslikescategorias(catalogo, categoria,numero)
# Funciones de consulta sobre el catálogo
def videospaiscategoría(numero,pais,categoría, catalogo):
    return model.videospaiscategoría(numero,pais,categoría,catalogo)

#Funciones copiadas literalmente del lab 7
