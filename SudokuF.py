import random 
import time
from colorama import Back, Fore, init
from SudokuT import *
from Menus import *

def imprimeTablero(t, name_tablero):
    """El sudoku se presenta en una tabla de 9 × 9,  compuesta por casillas de 3 × 3,
    El objetivo es rellenar las celdas vacías, con un número en cada una de ellas,
    de tal forma que cada columna, fila y región contenga los números 1–9 solo una vez.
    Además, cada número de la solución aparece solo una vez en cada una de las direcciones
    print(name_tablero)"""
    print(name_tablero)
    print("  | 1 2 3 | 4 5 6 | 7 8 9 |")
    for i in range(9):
        if i%3==0:
            print("−−−−−−−−−−−−−−−−−−−−−−−−−−−")
        print(i+1, end=" ")
        for j in range(9):
            if j%3==0:
                print("|", end=" ")
            if t[i][j] == 0:
                print(".", end=" ")
            else:
                print(t[i][j], end=" ")
        print("|")
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−")
    
def tableroCompleto(t):
    """ Verifica si el tablero esta completo recorriendo cada casilla del tablero, 
    si encuentra una casilla vacia; que viene a se representada como 0, retorna False, si no retorna True"""
    for i in range(9):
        for j in range(9):
            if t[i][j] == 0:
                return False
    return True

def verificarfila(t,x, y, d):
    '''Verifica a lo largo de la fila, si el valor que se ha ingresado no se 
    ha repetido en la fila seleccioada. Recibe los parametros de: valor ingresado, fila 
    en donde se desea poner el valor. he itera en la fila, buscando si este valor ya fue
    previamente ingresado'''
    for j in range(9):
        if t[x-1][j] == d:
            return False
    return True

def verificarColumna(t,x, y, d):
    for i in range(9):
        if t[i][y-1] == d:
            return False
    return True

def verificarCuadricula(t,x, y, d):
    """ Esta funcion verificara si el numero ingresado se encuentra dentro de la cuadricula, si no es el caso no se ejecutara la funcion.
    Recibe los parametros de la funcion esJugadaValida, y retorna un valor booleano"""
    x1 = (x-1)//3
    y1 = (y-1)//3
    for i in range(3):
        for j in range(3):
            if t[x1*3+i][y1*3+j] == d:
                return False
    return True


def guardar_tablero(tablero, name, name_tablero):
    """Esta funcion guarda el tablero en un archivo de texto, recibe como parametros el tablero, 
    el nombre del archivo y el nombre del tablero""" 
    with open("tableros.txt", "a") as file:
        file.write(name + " " + name_tablero + " ")
        for i in range(9):
            for j in range(9):
                file.write(str(tablero[i][j]) + " ")
        file.write("\n")

def vertablerosguardados():
    '''Hace un llamado de los tableros previamente guardados, 
    solicta 3 parametros: tablero, name y nombre del tablero  . Asímismo, 
    esta funcion utiliza otra funcion llamada imprimeTablero.'''
    # verificar que exista el archivo tableros.txt
    try:
        file = open("tableros.txt", "r")
        file.close()
    except:
        print(Fore.RED+"No hay tableros guardados"+Fore.RESET)
        return
    file = open("tableros.txt", "r")
    print("Tableros guardados:")
    for line in file:
        line = line.split()
        print(line[0], end=", ")
    file.close()
    name = input("\nIngrese el nombre del tablero que desea jugar: ")
    file = open("tableros.txt", "r")
    for line in file:
        line = line.split()
        if line[0] == name:
            tablero = []
            for i in range(9):
                tablero.append([])
                for j in range(9):
                    tablero[i].append(int(line[2+i*9+j]))
            imprimeTablero(tablero, line[1])
            file.close()
            return tablero
    file.close()
    print(Fore.RED+"No se encontro el tablero"+Fore.RESET)
    return

def verificarcasillaocupada(t,x,y,d):
    """ Esta funcion verificara si la casilla ya esta siendo ocupada 
    por otro numero, si es el caso no se ejecutara la funcion."""
    if t[x-1][y-1] == 0:
        return True
    return False

def newgame():
    """ Esta función crea un nuevo juego secreto"""
    print("\nNew Game unblocked \n")

    numero_aleatorio = random.randint(1,10) 
    intentos = 0
    while intentos < 3:
        numero = int(input(Fore.BLUE + "Adivina el numero: " + Fore.RESET))
        if numero == numero_aleatorio:
            print("Adivinaste! \n")
            break
        elif numero < numero_aleatorio:
            intentos += 1
            print("El numero es mayor")
        else:
            print("El numero es menor")
            intentos += 1
    else:
        print("Perdiste \n")
    
def verificardigitosvalidos(numbers):
    """ Esta funcion verifica que los digitos ingresados sean validos, permitiendo que 
    sean solo numeros del 1 al 9 y no letras o caracteres especiales y vacios""" 
    while len(numbers) != 3:
        print(Fore.RED +"...Error. Ingrese fila columna cifra: " + Fore.RESET)
        return False
    while not numbers[0].isdigit() or not numbers[1].isdigit() or not numbers[2].isdigit():
        print(Fore.RED +"...Error. Ingrese fila columna cifra: " + Fore.RESET)
        return False
    while int(numbers[0]) > 9 or int(numbers[0]) < 1 or int(numbers[1]) > 9 or int(numbers[1]) < 1 or int(numbers[2]) > 9 or int(numbers[2]) < 1:
        print(Fore.RED +"...Error. Ingrese fila columna cifra: " + Fore.RESET)
        return False
    return numbers

def verificarjugadavalida(tablero,x,y,d, tablerverificar):
    """ Esta funcion verifica si la jugada es valida, si es el caso se ejecutara la funcion, 
    si no es el caso no se ejecutara la funcion y retornara en que casilla se encuentra el error"""
    if verificarfila(tablero, x, y, d):
        if verificarColumna(tablero, x, y, d):
            if verificarCuadricula(tablero, x, y, d):
                if tablerverificar[x-1][y-1] == 0:
                    return True
                else:
                    print(Fore.RED +"Jugada inválida. Esta casilla no se puede modificar." + Fore.RESET)
                    return False
            else:
                print(Fore.RED + "Jugada inválida: se repite cifra en la misma cuadricula" + Fore.RESET)
                return False
        else:
            print(Fore.RED+ "Jugada inválida: se repite cifra en la misma columna" + Fore.RESET)
            return False
    else:
        print(Fore.RED+ "Jugada inválida: se repite la cifra en la misma fila" + Fore.RESET)
        return False

def tablerodificultad(opcion):
    """ Esta funcion crea un tablero de dificultad facil, media o dificil, posteriormente llama a la funcion tableroaleatorio"""
    if opcion == 1:
        k = tableroaleatorio_valido_con_reglas_por_dificultad(3)
        return k
    elif opcion == 2:
        k =tableroaleatorio_valido_con_reglas_por_dificultad(2)
        return k
    elif opcion == 3:
        k =tableroaleatorio_valido_con_reglas_por_dificultad(1)
        return k

def final(tablero, name, name_tablero):
    """ Esta funcion se ejecuta una sola vez que se sale del loop del jueg y el tablero este completo, par apreguntar si se desea guardar el tablero""" 
    creditosfinales()
    print(Fore.GREEN + "Felicidades, has ganado el juego" + Fore.RESET)
    print(Fore.GREEN + "Desea guardar el tablero?" + Fore.RESET)
    print("[1] Si")
    opcion = (input("[2] Finalizar: "))
    while opcion != "1" and opcion != "2":
        print(Fore.RED + "...Opción incorrecta. Intente nuevamente." + Fore.RESET)
        opcion = (input("[2] Regresar: "))
    opcion = int(opcion)
    if opcion == 1:
        guardar_tablero(tablero, name, name_tablero)
        print(Fore.LIGHTGREEN_EX + "Tablero guardado con éxito" + Fore.RESET)
        return True
    elif opcion == 2:
        print(Fore.BLUE + "Gracias por jugar" + Fore.RESET)
        return True

def verificardigitosvalidos2(numbers):
    """ Esta funcion verifica que los digitos ingresados sean validos, permitiendo que se continue con el juego"""
    while len(numbers) != 1:
        print(Fore.RED +"...Error: " + Fore.RESET)
        return False
    while not numbers[0].isdigit():
        print(Fore.RED +"...Error: " + Fore.RESET)
        return False
    while int(numbers[0]) > 3 or int(numbers[0]) < 1:
        print(Fore.RED +"...Error: " + Fore.RESET)
        return False
    return numbers

def invalid(numbers):
    """ Esta funcion verifica que los digitos ingresados sean validos, permitiendo que se continue con el juego""" 
    while len(numbers) != 1:
        print(Fore.RED +"...Error: " + Fore.RESET)
        return False
    while not numbers[0].isdigit():
        print(Fore.RED +"...Error: " + Fore.RESET)
        return False
    return numbers