import json
from data_stark import lista_personajes
from funciones import *
import os

'''
1.1. Crear la función 'leer_archivo' la cual recibirá por parámetro un string
que indicará el nombre y extensión del archivo a leer (Ejemplo:
archivo.json). Dicho archivo se abrirá en modo lectura únicamente y
retornara un string con la información del mismo.
ATENCIÓN:Controlar las excepciones posibles en caso de
presentarse alguna imprimir el mensaje de la misma y retornar
False
Usar de Encoding UTF-8
'''

#1.1
def leer_archivo(nombre_archivo:str, ubicacion:str) -> str:
    try:
        with open(ubicacion, 'r', encoding ='utf-8') as nombre_archivo:
            información_archivo = nombre_archivo.read() 
            return información_archivo
    except:
        print(False)

'''
1.2. Crear la función 'guardar_archivo' la cual recibirá por parámetro un
string que indicará el nombre con el cual se guardará el archivo junto
con su extensión (ejemplo: 'archivo.csv') y como segundo parámetro
tendrá un string el cual será el contenido a guardar en dicho archivo.
Debe abrirse el archivo en modo escritura+, ya que en caso de no
existir, lo creara y en caso de existir, lo va a sobreescribir La función
debera retornar True si no hubo errores, caso contrario False
(VALIDAR CON EXCEPCIONES), además en caso de éxito, deberá
imprimir un mensaje respetando el formato:
Se creó el archivo: nombre_archivo.csv
ATENCIÓN:Controlar las excepciones posibles en caso de
presentarse alguna retornar false e imprimir un mensaje que
diga:: ‘Error al crear el archivo: nombre_archivo’
Donde nombre_archivo será el nombre que recibirá el archivo a
ser creado, conjuntamente con su extensión.
Usar de Encoding UTF-8
'''

#1.2 
def guardar_archivo(nombre_archivo:str, contenido:str):
    retorno = False
    try:
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, 'w', encoding ='utf-8') as nombre_archivo:
                nombre_archivo.write(contenido)
                retorno = True
        else:
            with open(nombre_archivo, 'w', encoding ='utf-8') as nombre_archivo:
                nombre_archivo.write(contenido)
                retorno = True
                print(f'Se ha creado el archivo {nombre_archivo}')
    except:
        print('Error al crear el archivo: nombre_archivo')

    return retorno

'''
1.3. Crear la función generar_csv()
La función va a recibir el nombre y extensión del archivo csv de los
superhéroes (Puede ser ruta absoluta o relativa) y la lista de los
mismos.
Si la lista no está vacía la función deberá guardar en un string la
información en formato csv (separado con comas) con la cabecera
correspondiente.
Una vez generado el string debería usar la función de 1.2 para guardar
ese string generado al archivo.
Si la lista está vacia retornar False
Debería quedar algo como esto:
'''

#1.3
def generar_csv(lista_heroes:list, nombre_de_archivo:str):
    datos = ''
    if len(lista_heroes) > 0:
        lista_claves = list(lista_heroes[0].keys())
        cabecera = ",".join(lista_claves)
        for i in lista_heroes:
            lista_valores = list(i.values())
            dato = ",".join(lista_valores)
            datos += f'{dato}\n'
        guardar_archivo(nombre_de_archivo, (f'{cabecera}\n' f'{datos}'))
    else:
        return False

'''
1.4
Crear la función leer_csv() que va a recibir el nombre y extensión de
donde se ubica el archivo a leer (Ruta absoluta o relativa)
La función se tiene que encargar de generar una lista de superhéroes
en base al contenido de ese archivo csv que se le paso. Pueden usar
la cabecera de ese csv para generar las claves de cada uno de los
diccionarios.
La función debe retornar la lista de diccionarios si es que existe el
archivo y sino False.
'''

#1.4 PROBAR 
def leer_csv(nombre_archivo:str):
    lista = []
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r', encoding= 'utf-8') as archivo:
            keys = archivo.readline()
            keys = keys.replace('\n', '')
            lista_keys = keys.split(',')

            for linea in archivo:
                elemento = {}
                lista_elemento = linea.replace('\n', '')
                lista_elemento = linea.split(',')
                for i in range(len(lista_keys)):
                    key = lista_keys[i]
                    elemento[key] = lista_elemento[i]
                lista.append(elemento)
        retorno = lista
    else:
        retorno = False
    return retorno

'''
1.5
Crear la función generar_json() que va a recibir el nombre y extensión
de donde se ubica el archivo a guardar (Ruta absoluta o relativa) , la
lista de los superhéroes y el nombre de la lista.
Si la lista no está vacía debería guardar en un diccionario de una sóla
clave la lista de superhéroes,el nombre de clave debería ser la del
tercer parámetro que sería el nombre de la lista.
'''
#1.5
def generar_json(nombre_de_archivo:str, lista_superheroes:list, nombre_dic:str):
    if len(lista_superheroes) > 0:
        stark_normalizar_datos(lista_superheroes)
        dic = {nombre_dic: lista_superheroes}
        contenido = open(nombre_de_archivo, 'w', encoding= 'utf-8')
        json.dump(dic, contenido, indent= 4)
        contenido.close()

'''
1.6
Crear la función leer_json() que va a recibir el nombre y extensión de
donde se ubica el archivo a leer (Ruta absoluta o relativa), y también el
nombre de la lista a leer por ejemplo en la imagen anterior la lista está
en la clave “heroes”
Si el archivo existe deberia leer el archivo json y retornar la lista
obtenida.
Si el achivo no existe deberia retornar False (USAR EXCEPCIONES)
'''
#1.6
def leer_json(nombre_de_archivo:str, nombre_lista):
    try:
        with open(nombre_de_archivo, 'r', encoding= 'utf-8') as archivo:
            lista = json.load(archivo)
            lista = lista[nombre_lista]
            retorno = lista
    except FileNotFoundError:
        retorno = False

    return retorno

'''
2.1
Crear una función para ordenar héroes por alguna de las claves
númericas (altura, peso y fuerza) de manera ascendente
'''
#2.1
def ordenarAsc(dato, lista):
    stark_normalizar_datos(lista)
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i][dato] > lista[j][dato]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    lista_ordenada = lista
    return lista_ordenada
'''
2.2. Crear una función para ordenar héroes por alguna de las claves
númericas (altura, peso y fuerza) de manera descendente.
'''
#2.2
def ordenarDesc(dato, lista):
    stark_normalizar_datos(lista)
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i][dato] < lista[j][dato]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    lista_ordenada = lista
    return lista_ordenada

'''
2.3. Crear una función para ordenar héroes por alguna de las claves
númericas (altura, peso y fuerza). Preguntar al usuario si lo quiere
ordenar de manera ascendente (‘asc’) o descendente (‘desc’) (reutilizar
funciones anteriores dependiendo del caso)
'''
#2.3
def ordenar(dato:str, asc_o_desc:str, lista):
    if asc_o_desc == 'desc':
        retorno = ordenarDesc(dato, lista)
    elif asc_o_desc == 'asc':
        retorno = ordenarAsc(dato, lista)
    return retorno

