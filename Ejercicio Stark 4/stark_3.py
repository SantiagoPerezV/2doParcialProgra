#ARCHIVO PADRE DE STARK 3
from data_stark import lista_personajes
from funciones import *

lista_personajes_femenino = []
lista_personajes_masculino = []
lista_personajes_nb = []
for i in range(len(lista_personajes)):
    if obtener_dato(i,"genero") == "F":
        lista_personajes_femenino.append(lista_personajes[i])
    elif obtener_dato(i,"genero") == "M":
        lista_personajes_masculino.append(lista_personajes[i])
    else:
        lista_personajes_nb.append(lista_personajes[i])

#7 Stark 2 optimizado con funciones que debimos hacer con el stark3; por parámetro tiene la lista a usar
match stark_marvel_app_7(lista_personajes):
    case 1:
        print(stark_normalizar_datos(lista_personajes))
    case 2:
        for i in range(len(lista_personajes)):
            if obtener_dato(i,"genero") == "NB":
                print(obtener_nombre(i))
    case 3:
        for i in range(len(lista_personajes_femenino)):
            if lista_personajes_femenino[i]["altura"] == obtener_maximo(lista_personajes_femenino,"altura"):
                print(f'Superhéroe femenina más alta: {lista_personajes_femenino[i]["nombre"]}')
    case 4:
        for i in range(len(lista_personajes_masculino)):
            if lista_personajes_masculino[i]["altura"] == obtener_maximo(lista_personajes_masculino,"altura"):
                print(f'Superhéroe masculino más alto: {lista_personajes_masculino[i]["nombre"]}')
    case 5:
        for i in range(len(lista_personajes_masculino)):
            if lista_personajes_masculino[i]["fuerza"] == obtener_minimo(lista_personajes_masculino,"fuerza"):
                print(f'Superhéroes masculinos más débiles: {lista_personajes_masculino[i]["nombre"]}')
    case 6:
        for i in range(len(lista_personajes_nb)):
            if lista_personajes_nb[i]["fuerza"] == obtener_minimo(lista_personajes_nb,"fuerza"):
                print(f'Superhéroe no binario más débil: {lista_personajes_nb[i]["nombre"]}')
    case 7:
        print(mostrar_promedio_dato(lista_personajes_nb,"fuerza"))
    case 8:
        contador_color_ojos_red = 0
        contador_color_ojos_blue = 0
        contador_color_ojos_green = 0
        contador_color_ojos_otro = 0
        contador_color_ojos_brown = 0
        contador_color_ojos_yellow = 0

        for i in range(len(lista_personajes)):
            if obtener_dato(i,"color_ojos") == "Red":
                contador_color_ojos_red += 1
            elif obtener_dato(i,"color_ojos") == "Blue":
                contador_color_ojos_blue += 1
            elif obtener_dato(i,"color_ojos") == "Green":
                contador_color_ojos_green += 1
            elif obtener_dato(i,"color_ojos") == "Brown":
                contador_color_ojos_brown += 1
            elif obtener_dato(i,"color_ojos") == "Yellow":
                contador_color_ojos_yellow += 1
            else:
                contador_color_ojos_otro += 1
        print (f'Superheroes con color de ojos rojos: {contador_color_ojos_red} \nColor de ojos azules: {contador_color_ojos_blue} \nColor de ojos verdes: {contador_color_ojos_green} \nColor de ojos marrones: {contador_color_ojos_brown} \nColor de ojos amarillos: {contador_color_ojos_yellow} \nColor de ojos otro: {contador_color_ojos_otro}')
    case 9:
        contador_color_pelo_black = 0
        contador_color_pelo_brown = 0
        contador_color_pelo_blond = 0
        contador_color_pelo_green = 0
        contador_color_pelo_yellow = 0
        contador_color_pelo_auburn = 0
        contador_color_pelo_white = 0
        contador_color_pelo_nopelo = 0
        contador_color_pelo_red = 0
        contador_color_pelo_dos_colores = 0

        for i in range(len(lista_personajes)):
            if obtener_dato(i,"color_pelo") == "Black":
                contador_color_pelo_black += 1
            elif obtener_dato(i,"color_pelo") == "Blond":
                contador_color_pelo_blond += 1
            elif obtener_dato(i,"color_pelo") == "Green":
                contador_color_pelo_green += 1
            elif obtener_dato(i,"color_pelo") == "Brown":
                contador_color_pelo_brown += 1
            elif obtener_dato(i,"color_pelo") == "Yellow":
                contador_color_pelo_yellow += 1
            elif obtener_dato(i,"color_pelo") == "Auburn":
                contador_color_pelo_auburn += 1
            elif obtener_dato(i,"color_pelo") == "White":
                contador_color_pelo_white += 1
            elif obtener_dato(i,"color_pelo") == "No Hair":
                contador_color_pelo_nopelo += 1
            elif obtener_dato(i,"color_pelo") == "Red":
                contador_color_pelo_red += 1
            else:
                contador_color_pelo_dos_colores += 1

        print(f'Superheroes con color de pelo negro: {contador_color_pelo_black} \nColor de pelo rubio: {contador_color_pelo_blond} \nColor de pelo verde: {contador_color_pelo_green} \nColor de pelo marron: {contador_color_pelo_brown} \nColor de pelo amarillos: {contador_color_pelo_yellow} \nColor de pelo auburn: {contador_color_pelo_auburn} \nColor de pelo blanco: {contador_color_pelo_white} \nColor de pelo rojo: {contador_color_pelo_red} \nPelados: {contador_color_pelo_nopelo} \nMas de dos colores de pelo: {contador_color_pelo_dos_colores} ')
    case 10:
        nombres_color_ojos_red = ''
        nombres_color_ojos_blue = ''
        nombres_color_ojos_green = ''
        nombres_color_ojos_otro = ''
        nombres_color_ojos_brown = ''
        nombres_color_ojos_yellow = ''
        nombres_color_ojos_yellow_no_irises = ''
        nombres_color_ojos_hazel = ''
        nombres_color_ojos_silver = ''

        for i in range(len(lista_personajes)):
            if obtener_dato(i, "color_ojos") == "Red":
                nombres_color_ojos_red += f'\n {lista_personajes[i]["nombre"]}'
            elif obtener_dato(i, "color_ojos") == "Blue":
                nombres_color_ojos_blue += f'\n {lista_personajes[i]["nombre"]}'
            elif obtener_dato(i, "color_ojos") == "Green":
                nombres_color_ojos_green += f'\n {lista_personajes[i]["nombre"]}'
            elif obtener_dato(i, "color_ojos") == "Brown":
                nombres_color_ojos_brown += f'\n {lista_personajes[i]["nombre"]}'
            elif obtener_dato(i, "color_ojos") == "Yellow":
                nombres_color_ojos_yellow += f'\n {lista_personajes[i]["nombre"]}'
            elif obtener_dato(i, "color_ojos") == "Yellow (without irises)":
                nombres_color_ojos_yellow_no_irises += f'\n {lista_personajes[i]["nombre"]}'
            elif obtener_dato(i, "color_ojos") == "Hazel":
                nombres_color_ojos_hazel += f'\n {lista_personajes[i]["nombre"]}'
            elif obtener_dato(i, "color_ojos") == "Silver":
                nombres_color_ojos_silver += f'\n {lista_personajes[i]["nombre"]}'
            else:
                nombres_color_ojos_otro += f'\n {lista_personajes[i]["nombre"]}'

        print(f'Superheroes con color de ojos rojos: {nombres_color_ojos_red} \nColor de ojos azules: {nombres_color_ojos_blue} \nColor de ojos verdes: {nombres_color_ojos_green} \nColor de ojos marrones: {nombres_color_ojos_brown} \nColor de ojos amarillos: {nombres_color_ojos_yellow} \nColor de ojos amarillos (sin iris): {nombres_color_ojos_yellow_no_irises} \nColor de ojos hazel: {nombres_color_ojos_hazel} \nColor de ojos plateados: {nombres_color_ojos_silver} ')
    case 11:
        nombres_inteligencia_good= ''
        nombres_inteligencia_average= ''
        nombres_inteligencia_high= ''

        for i in range(len(lista_personajes)):
            if obtener_dato(i,"inteligencia") == "good":
                nombres_inteligencia_good += f'\n {lista_personajes[i]["nombre"]}'
            elif obtener_dato(i,"inteligencia") == "high":
                nombres_inteligencia_high += f'\n {lista_personajes[i]["nombre"]}'
            else:
                nombres_inteligencia_average += f'\n {lista_personajes[i]["nombre"]}'

        print(f'Superheroes con inteligencia promedia: {nombres_inteligencia_average} \nInteligencia buena: {nombres_inteligencia_good} \nInteligencia alta: {nombres_inteligencia_high}')