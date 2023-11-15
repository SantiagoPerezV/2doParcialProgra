from data_stark import lista_personajes
from funciones import *

#6 Menú
while True:
    print('Menú Stark Industries:\n1 - Imprimir la lista de nombres junto con sus iniciales\n2 - Imprimir la lista de nombres y el código del mismo\n3 - Normalizar datos\n4 - Imprimir índice de nombres\n5 - Navegar fichas\n6 - Salir')
    opcion = input()
    match opcion:
        case '1':
            stark_imprimir_nombres_con_iniciales(lista_personajes)
        case '2':
            print(stark_generar_codigos_heroes(lista_personajes))
        case '3':
            print(stark_normalizar_datos(lista_personajes))
        case '4':
            print(stark_imprimir_indice_nombre(lista_personajes))
        case '5':
            stark_navegar_fichas(lista_personajes)
        case '6':
            break