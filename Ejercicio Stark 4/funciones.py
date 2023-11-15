import re
from data_stark import lista_personajes


#1.1 La función guarda las iniciales del nombre que le pases por parámetro en una lista; en el retorno devuelve las iniciales unidas en un string y separadas por un ".".
def extraer_iniciales (nombre_heroe:str):
    retorno = ''
    if nombre_heroe == '':
        retorno = 'N/A'
    iniciales = re.sub('the',' ',nombre_heroe)
    iniciales = re.sub('-', ' ', nombre_heroe)
    iniciales = re.findall('[A-Z]', nombre_heroe)
    for i in range(len(iniciales)):
        retorno += f'{iniciales[i]}.'
    return retorno

#1.2 Por parámetro recibe un dato específico de la lista, en caso de que el dato no sea str, devuelve False. La función retorna el dato en modo snake_case y en minúsculas.
def obtener_dato_formato(dato:str):
    if type(dato) != str:
        retorno = False
    else:
        retorno = re.sub(' ', '_', dato)
        retorno = retorno.lower()
    return retorno

#1.3 Por parámetro recibe SOLO UN DICT, lista con dentro diccionario no; Valida que el dato sea dict y que el diccionario contenga la clave "nombre", sino retorna false; La función printeael nombre del diccionario que le pases en modo snake_case y luego con sus iniciales. Si cumple con la validación y la función va correctamente devuelve True, sino devuelve False.
def stark_imprimir_nombre_con_iniciales(nombre_heroe:dict):
    retorno = True
    if type(nombre_heroe) != dict:
        retorno = False
    if retorno == True:
        for i in nombre_heroe.keys():
            if i == 'nombre':
                retorno = True
                break
            else:
                retorno = False
    if retorno == True:
        print(f'* {obtener_dato_formato(nombre_heroe["nombre"])} ({extraer_iniciales(nombre_heroe["nombre"])})')
    return retorno

#1.4 Como parámetro recibe una lista a recorrer; se debe validad que lo pasado por parámetro sea un tipo de dato lista y que tenga por lo menos un elemento; imprimirá toda la lista de heroes con el mismo formato que la función anterior (snake_case y con las iniciales); la función retornara True si completa la validación o False si hubo algún problema
def stark_imprimir_nombres_con_iniciales(lista_heroes:list):
    retorno = True
    mensaje = ''
    if type(lista_heroes) != list:
        retorno = False
    if len(lista_heroes) == 0:
        retorno = False
    
    if retorno == True:
        for elemento in range(len(lista_heroes)):
            diccionario = lista_heroes[elemento]
            mensaje += f'{stark_imprimir_nombre_con_iniciales(diccionario)}'
        mensaje = re.sub('True', '', mensaje)
        print(mensaje)
    return retorno

#2.1 Por parámetro recibe un diccionario y un id;la función retorna un str, el valor de la key género, ya sea M,F o NB, le sigue un 2,1,0 según su genero correspondiente y el id. Entre el id y el número de valor según su género, hay 0 que hacen que completen el str hasta que llegue a 10 caracteres; tiene una validación de que si la key género se encuentra vacía o no corresponde a M, F o NB, retorna 'N/A'
def generar_codigo_heroe(diccionario:dict, id:int):
    retorno = 'N/A'
    for key in diccionario.keys():
        if key == 'genero':
            validacion_key = True
            break
        else:
            validacion_key = False
    if validacion_key == True:
        for i in diccionario.values():
            if i == 'M':
                identidad = f'{id}'
                identidad = identidad.zfill(7)
                retorno = 'M-1' + identidad
                break
            elif i == 'F':
                identidad = f'{id}'
                identidad = identidad.zfill(7)
                retorno = 'F-2' + identidad
                break
            elif i == 'NB':
                identidad = f'{id}'
                identidad = identidad.zfill(6)
                retorno = 'NB-0' + identidad
                break
    return retorno

#2.2 Por parámetro recibe la lista a ser recorrida; la función valida que la lista tenga al menos un elemento y que todos los elementos de la lista sean tipo diccionario; si no cumple la validación retorna False, si la cumple y sale todo como lo esperado, retorna los nombres de los heroes en minuscula y estilo snake_case y el código generado en la función anterior.
def stark_generar_codigos_heroes(lista_heroes:list):
    id_heroe = 0
    msj = ''
    if len(lista_heroes) > 0:
        for i in range(len(lista_heroes)):
            if type(lista_heroes[i]) == dict:
                diccionario = lista_heroes[i] 
                id_heroe += 1
                msj += f' {obtener_dato_formato(diccionario["nombre"])} ({extraer_iniciales(diccionario["nombre"])}) | {generar_codigo_heroe(diccionario, id_heroe)}\n'
            else:
                msj = False
                break
    else:
        msj = False
    return msj

#3.1 Por parámetro recibe el string numero_str, que posiblemente represente un número; La función tiene distintas validaciones con su retorno cada una. Si contiene carácteres no númericos, retorna -1. Si el número es negativo, retorna -2. Si ocurre otro error que hace no lograr al número retornarlo en entero, retorna -3 y en caso de que se verifique el texto tiene un número entero positivo, retorna el número en tipo de dato entero. Quita los espacios en blanco si los hay.
def sanitizar_entero (numero_str:str):
    retorno = -3
    if type(numero_str) == str:
        validacion = re.search('(\d)', numero_str)
        if validacion != None:
            numero_str = numero_str.replace(' ', '')
            numero_str = int(numero_str)
            if numero_str < 0:
                retorno = -2
            else:
                retorno = numero_str
        else:
            retorno = -1
    return retorno

#3.2 Por parámetro recibe el string numero_str, que posiblemente represente un número; La función tiene distintas validaciones con su retorno cada una. Si contiene carácteres no númericos, retorna -1. Si el número es negativo, retorna -2. Si ocurre otro error que hace no lograr al número retornarlo a flotante, retorna -3 y en caso de que se verifique el texto tiene un número flotante positivo, retorna el número en tipo de dato flotante. Quita los espacios en blanco si los hay.
def sanitizar_flotante(numero_str:str):
    retorno = -3
    if type(numero_str) == str:
        validacion = re.search('(\d)', numero_str)
        if validacion != None:
            numero_str = numero_str.replace(' ', '')
            numero_str = float(numero_str)
            if numero_str < 0:
                retorno = -2
            else:
                retorno = numero_str
        else:
            retorno = -1
    return retorno

#3.3 Por parámetro recibe valor_str, que es un posible string con solo carácteres alfabéticos. La única validación que conlleva es que en la cadena haya no numéricos, en ese caso contrario retorna 'N/A. Si cumple la validación, la validación reemplaza una '/' por un espacio si lo hay; y que finalmente la retorne en minúscula y sin espacios vacíos.
def sanitizar_string(valor_str:str):
    validacion = re.search('[(\d)]', valor_str)
    if validacion == None:
        valor_str = valor_str.replace('/', ' ')
        valor_str = valor_str.lower().strip()
        retorno = str(valor_str)
    else:
        retorno = 'N/A'
    return retorno

#3.4 La función por parámetro recibe heroe (dict del superheroe), clave_a_sanitizar (dato del dict a sanitizar) y tipo_dato (tipo de dato a querer devolver). Se deberá validar que tipo_dato sea string, entero o flotante y que puedan llegar mayúsculas, en caso de que no se cumple retornara 'tipo de dato no reconocido'; También se deberá validar que la clave exista dentro del diccionario, en caso de que no pase retornará ‘La clave especificada no existe en el héroe’, acá si es sensible a mayúsculas o minúsculas. Finalmente, en caso de que se sanitice el dato, devolverá True, caso contrario devolverá False. 
def sanitizar_dato(heroe:dict, clave_a_sanitizar:str, tipo_dato:str): #string, entero o flotante
    tipo_dato = tipo_dato.lower()
    validacion = None
    if tipo_dato != 'string' and tipo_dato != 'entero' and tipo_dato != 'flotante':
        retorno = 'Tipo de dato no reconocido'
        validacion = False
    else:
        for i in heroe.keys():
            if i == clave_a_sanitizar:
                validacion = True
                break
            else:
                validacion = False
                retorno = 'La clave especificada no existe en el héroe'
    #Supera las validaciones
    if validacion == True:
        if tipo_dato == 'string':
            if sanitizar_string(heroe[clave_a_sanitizar]) == 'N/A': #-> 0 porque si la validación de str daba error, retornaba N/A.
                retorno = False
            else:
                retorno = True
        elif tipo_dato == 'entero':
            if sanitizar_entero(heroe[clave_a_sanitizar]) > 0: #-> 0 porque si la validación de sanitizar int o float daba error, retornaba -.
                retorno = True
            else:
                retorno = False
        else:
            if sanitizar_flotante(heroe[clave_a_sanitizar]) > 0:
                retorno = True
            else:
                retorno = False
    
    return retorno

#3.5 La función lleva por parámetro una lista que será la recorrida para sanitizar los datos. La única validación que tiene es que la lista no esté vacía, en ese caso retorna error. Si cumple la validación, recorre la lista, sanitiza los valores ‘altura’, ‘peso’, ‘color_ojos’, ‘color_pelo’, ‘fuerza’ e ‘inteligencia’ y muestra el mensaje 'Datos normalizados'.
def stark_normalizar_datos(lista_heroes:list):
    if len(lista_heroes) == 0:
        retorno = 'Error: Lista de héroes vacía'
    else:
        for dic in range(len(lista_heroes)):
            sanitizar_dato(lista_heroes[dic], 'altura', 'flotante')        
            sanitizar_dato(lista_heroes[dic], 'peso', 'flotante')
            sanitizar_dato(lista_heroes[dic], 'color_ojos', 'string')
            sanitizar_dato(lista_heroes[dic], 'color_pelo', 'string')
            sanitizar_dato(lista_heroes[dic], 'fuerza', 'entero')
            sanitizar_dato(lista_heroes[dic], 'inteligencia', 'string')
        retorno = 'Datos normalizados.'
    return retorno

#4.1 Por parámetro le paso la lista_heroes que será recorrida. La función debe mostrar por pantalla los nombres de los superhéroes separando cada espacio con un '-', y en caso de que haya un 'the', debe ser ignorado.
def stark_imprimir_indice_nombre(lista_heroes:list):
    mensaje_final = ''
    for i in range(len(lista_heroes)):
        nombre = lista_heroes[i]["nombre"]
        #Pregunto si existe un 'the' en el nombre
        validacion = re.search('the', nombre)
        if validacion != None:
            #En caso de que si, reemplazo el 'the' por un '-' y borro espacios.
            nombre = nombre.replace('the', '-').replace(' ', '')
        else:
            #En caso de que no, simplemente reemplazo espacios por un '-'
            nombre = re.sub(' ', '-', nombre)
        mensaje_final += f'{nombre}-'
    return mensaje_final

#5.1 Por parámetro recibe el patrón a repetir; el número de veces que se repite el patrón; y el booleano imprimir, si es False, solo retornara el separador, en caso de ser True, imprime el separador antes de retornarlo. Tiene 2 validaciones, que el patrón tenga 1 o 2 carácteres como máximo y que el largo del separador sea entre 1 y 235 veces repetido. Si no pasa la validación, retornara 'N/A', sino, retornara el separador armado.
def generar_separador(patron:str, largo:int, imprimir:bool):
    retorno = None
    separador = ''
    #1ra validacion, si el patrón tiene 1 o 2 carácteres.
    if len(patron) > 0 and len(patron) < 3:
        #2da validación, que el largo sea entre 1 y 235.
        if largo > 0 and largo <= 235:
            for i in range(largo):
                separador += patron
            #Si imprimir es True, imprimir antes de retornarlo
            if imprimir == True:
                print(separador)
            retorno = separador
        else:
            retorno = 'N/A'
    else:
        retorno = 'N/A'
    return retorno

#5.2 Recibe como parámetro un título que representa una sección de la ficha; No conlleva ninguna validación. Sólo devuelve el titulo en mayúscula entre separadores de líneas.
def generar_encabezado(titulo:str):
    titulo = titulo.upper()
    encabezado = f"{generar_separador('*', 165, False)}\n{titulo}\n{generar_separador('*', 165, False)}"
    return encabezado


#5.3 De parámetro lleva un diccionario que representa al héroe y el id que llevará el personaje para su código; validación no tiene; imprime en formato de ficha, los datos del héroe.
def imprimir_ficha_heroe(heroe:dict, id:int):
    ficha = generar_encabezado('principal')
    ficha += f'NOMBRE DEL HÉROE: {obtener_dato_formato(heroe["nombre"])} ({extraer_iniciales(heroe["nombre"])})\nIDENTIDAD SECRETA: {obtener_dato_formato(heroe["identidad"])}\nCONSULTORA: {obtener_dato_formato(heroe["empresa"])}\nCÓDIGO DE HÉROE: {generar_codigo_heroe(heroe, id)}\n'
    ficha += generar_encabezado('fisico')
    ficha += f'ALTURA: {sanitizar_flotante(heroe["altura"]):.0f} cm.\nPESO: {sanitizar_flotante(heroe["peso"]):.2f} kg.\nFUERZA: {sanitizar_entero(heroe["fuerza"])} N.\n'
    ficha += generar_encabezado('señas particulares')
    ficha += f'COLOR DE OJOS: {sanitizar_string(heroe["color_ojos"])}\nCOLOR DE PELO: {sanitizar_string(heroe["color_pelo"])}'

    return ficha

#5.5 Por parámetro recibe la lista que será controlada para navegar. No tiene validación. La función imprime el primer heroe y luego le da a elegir al usuario, si ver el heroe de la izquierda, de la derecha o salir de la función; en caso de que el diccionario se vaya de rango tiene que volver para hacer un bucle dentro de los elementos de la lista; en otro caso de que el usuario a la hora de navegar no elija ninguna opción de las que se pide, volverá a imprimir el menú hasta que utilice una opción correcta.
def stark_navegar_fichas(lista_heroes:list):
    diccionario = 0
    print(imprimir_ficha_heroe(lista_heroes[diccionario], (diccionario + 1)))
    while True:
        print('Navegue entre los héroes con estas opciones: ')
        menu = input('Ingresando 1: Ir a la izquierda\nIngresando 2: Ir a la derecha\nIngresando 3: Salir\n')
        match menu:
            case '1':
                diccionario -= 1
                if diccionario < 0:
                    diccionario = len(lista_heroes) - 1 
                print(imprimir_ficha_heroe(lista_heroes[diccionario], (diccionario + 1)))
            case '2':
                diccionario += 1
                if diccionario > 23:
                    diccionario = 0 
                print(imprimir_ficha_heroe(lista_heroes[diccionario], (diccionario + 1)))
            case '3':
                break

