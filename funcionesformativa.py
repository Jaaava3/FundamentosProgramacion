

def validarNum(msjeInput, msjeRango, msjeExcept, min, max):
    valido = True
    while valido:
        try:
            num = int(input(msjeInput))
            if min <= num <= max:
                valido = False
            else:
                print(msjeRango)
        except:
            print(msjeExcept)

    return num

def menu():
    print('''*** MENU PRINCIPAL ***
1.- Turistas por país.
2.- Turista por mes.
3.- Eliminar turista.
4.- Salir''')
    
    return validarNum('Ingrese opción de Menú: ', 'Opción fuera de rango. Seleccione opciones entre 1 - 4', '¡Debe ingresar números enteros!', 1, 4)
    
def turistas_por_pais(diccturistas):
    pais = input('Ingrese nombre del país: ').upper()
    existe = False
    for numero, infoTuristas in diccturistas.items():
        if infoTuristas[1].upper() == pais:
            print(infoTuristas[0])
            existe = True
    
    if not existe:
        print('No hay turistas de ese país')
    

def turistas_por_mes(diccturistas):
    mes = validarNum('Ingrese el número del mes que desea revisar (1-12): ',
                     'Mes fuera de rango. Utilice número según mes correspondiente. Ej: 1 para Enero, 2 para Febrero... 12 para Diciembre', 
                     'Sólo números enteros', 1, 12)
    contador = 0
    total = len(diccturistas) 

    for infoTuristas in diccturistas.values():
        if int(infoTuristas[2].split('-')[1]) == mes:
            contador +=1
    if contador != 0:
        porcentaje = round((100*contador)/total, 1)
        print(f'El número de turistas equivale al {porcentaje}% del total')  
    else:
        print(f'No visitaron turistas el país el mes {mes}')
    
def eliminar_turista(diccturistas):
    nombre = input('Ingrese nombre del turista a eliminar: ').upper()
    existe = False
    for numero, infoTuristas in diccturistas.items():
        if infoTuristas[0].upper() == nombre:
            diccturistas.pop(numero)
            print('Turista se ha eliminado con éxtio')
            existe = True
            break
    
    if not existe:
        print('Turista no encontrado. No se pudo eliminar')
    
    return diccturistas


    
    
