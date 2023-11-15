import re
from data_stark import lista_personajes
def stark_normalizar_datos(lista:list):
    bandera_datos_modificados = False
    mensaje_menu = ''
    for i in range(len(lista)):
        if type(lista[i]['fuerza']) != int:
            lista[i]['fuerza'] = int(lista[i]['fuerza'])
            bandera_datos_modificados = True
        if type(lista[i]['altura']) != float:
            lista[i]['altura'] = float(lista[i]['altura'])
            bandera_datos_modificados = True
        if type(lista[i]['peso']) != float:
            lista[i]['peso'] = float(lista[i]['peso'])
            bandera_datos_modificados = True
        else:
            bandera_datos_modificados = False
    if bandera_datos_modificados == True:
        mensaje_menu = 'Datos modificados.'
    else:
        mensaje_menu = 'Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente'
    return mensaje_menu

#Funcion creada para devolver en str los tipos de datos flotantes o enteros
def pasarString(lista_heroes:list):
    for i in range(len(lista_heroes)):
        if type(lista_heroes[i]['altura']) == float:
            lista_heroes[i]['altura'] = str(lista_heroes[i]['altura'])
        if type(lista_heroes[i]['peso']) == float:
            lista_heroes[i]['peso'] = str(lista_heroes[i]['peso'])
        if type(lista_heroes[i]['fuerza']) == int:
            lista_heroes[i]['fuerza'] = str(lista_heroes[i]['fuerza'])
    return lista_heroes