from stark_desafio_5 import *
from funciones import *
'''
3. Desarrollar los siguientes puntos (usando el data_stark.py) -> Se deben
desarrollar funciones extra dependiendo de la situación o reutilizar funciones
anteriores como normalizar o listar.
● 1-Normalizar datos (No debe dejar de entrar a las otras opciones)
● 2-Generar CSV (Guardar la lista generada en otra variable)
● 3-Listar heroes del archivo CSV ordenados por altura ASC (Validar si el
mismo existe)
● 4-Generar JSON (Guardar la lista generada en otra variable)
● 5-Listar heroes del archivo JSON ordenados por peso DESC (Validar si
el mismo existe)
● 6-Ordenar Lista por fuerza (Se le tiene que preguntar al usuario si
ordenar de manera ASC o DESC
● 7-Salir
'''
print('Antes de iniciar debe normalizar datos: si/no')
normalizar = input()
match normalizar:
    case 'si':
        print('● 1-Normalizar datos\n● 2-Generar CSV (Guardar la lista generada en otra variable)\n● 3-Listar heroes del archivo CSV ordenados por altura ASC (Validar si el mismo existe)\n● 4-Generar JSON (Guardar la lista generada en otra variable)\n● 5-Listar heroes del archivo JSON ordenados por peso DESC (Validar si el mismo existe)\n● 6-Ordenar Lista por fuerza\n● 7-Salir')
        while True:
            stark_normalizar_datos(lista_personajes)
            opcion = input()
            match opcion:
                case '1':
                    print(stark_normalizar_datos(lista_personajes))
                case '2':
                    nombre_archivo = input('Ingrese el nombre que quiere para el csv: ')
                    generar_csv(pasarString(lista_personajes), nombre_archivo + '.csv')
                case '3':
                    archivo = input('Ingrese la ubicación del archivo csv: ')
                    lista_ordenada = (ordenarAsc("altura", leer_csv(archivo)))
                    for i in range(len(lista_ordenada)):
                        print(f'{lista_ordenada[i]["nombre"]} - {lista_ordenada[i]["altura"]}')
                case '4':
                    nombre_archivo = input('Ingrese el nombre del archivo json: ')
                    print(generar_json(nombre_archivo + '.json', lista_personajes, nombre_archivo))
                case '5':
                    archivo = input('Ingrese la ubicación del archivo json: ')
                    nombre_clave = input('Ingrese el nombre de la clave principal del dic: ')
                    lista_ordenada = (ordenarDesc("peso", leer_json(archivo, nombre_clave)))
                    for i in range(len(lista_ordenada)):
                        print(f'{lista_ordenada[i]["nombre"]} - {lista_ordenada[i]["peso"]}\n')
                case '6':
                    manera = input('Ingrese cómo quiere obtener la lista (asc/desc): ')
                    lista_ordenada = ordenar("fuerza", manera, lista_personajes)
                    for i in range(len(lista_ordenada)):
                        print(f'{lista_ordenada[i]["nombre"]} - {lista_ordenada[i]["fuerza"]}')
                case '7':
                    break