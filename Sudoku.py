import random
import time
from colorama import Back, Fore, init
from SudokuF import *
from SudokuT import *
from Menus import *
from Ahorcado import *

lop = 0
while lop == 0: 
    menuprincipal()
    opcionprincipal = input(Fore.BLUE + "[4] Finalizar: " + Fore.RESET)
    if opcionprincipal == "Fernando": #Easter egg
        newgame()
    if opcionprincipal == "Endgame": #Easter egg
        creditoss()
        exit()
    if opcionprincipal == "Ayuda": #Easter egg
        jueguito()
    if opcionprincipal == "Mario":
        from mario_level_1 import *
        if __name__ == '__main__':
            main()
            pg.quit()
            #sys.exit()
    numbers2 = opcionprincipal.split() 
    while len(numbers2) != 1 or not numbers2[0].isdigit() or int(numbers2[0]) > 4 or int(numbers2[0]) < 1:
        print(Fore.RED + "...Opción incorrecta. Intente nuevamente." + Fore.RESET)
        opcionprincipal = input(Fore.BLUE + "[4] Finalizar: " + Fore.RESET)
        numbers2 = opcionprincipal.split()
    opcionprincipal = int(numbers2[0])                               
    loop = True
    while loop == True: 
        if opcionprincipal == 1:
            name = input(Fore.MAGENTA + "Nombre del jugador: " + Fore.RESET)
            name_tablero = input(Fore.LIGHTMAGENTA_EX +"Nombre del tablero: " + Fore.RESET)
            tablero = tableros() #[[1,3,4,5,8,9,2,6,7],[8,5,7,2,6,3,1,9,4],[9,6,2,1,4,7,8,3,5],[2,9,3,7,1,8,4,5,6],[5,4,1,3,2,6,7,8,9],[7,8,6,9,5,4,3,2,1],[4,7,9,8,3,5,6,1,2],[6,2,8,4,9,1,5,7,3],[3,1,5,6,7,2,9,4,0]] 
            imprimeTablero(tablero, name_tablero)
            tablerverificar = []
            for i in range(9):
                tablerverificar.append([])
                for j in range(9):
                    tablerverificar[i].append(tablero[i][j])
            while not tableroCompleto(tablero):
                numbers = input("Ingrese fila columna cifra: ")
                numbers = numbers.split() 
                while verificardigitosvalidos(numbers) == False:
                    numbers = input("Ingrese fila columna cifra: ")
                    numbers = numbers.split()
                x = int(numbers[0])
                y = int(numbers[1])
                d = int(numbers[2])   
                if verificarjugadavalida(tablero, x, y, d, tablerverificar) == True:
                    tablero[x-1][y-1] = d
                    imprimeTablero(tablero, name_tablero)
            if final(tablero, name, name_tablero) == True:
                loop = False        
        elif opcionprincipal == 2:
            print("Desea cargar un tablero propio?")
            print("[1] Si")
            opcion = (input("[2] Cargar Tableros predefinidos: "))
            while opcion != "1" and opcion != "2": 
                print(Fore.RED + "Opción incorrecta. Intente nuevamente." + Fore.RESET)
                opcion = (input("[2] Cargar Tableros predefinidos: "))
            opcion = int(opcion)
            if opcion == 1:
                vertablerosguardados()
            if opcion == 2: 
                print()
                alltableros()               
                numero = input("Ingrese el número del tablero que desea ver/jugar: ")
                while not numero.isdigit() or int(numero) > 10 or int(numero) < 1:
                    print(Fore.RED + "Opción incorrecta. Intente nuevamente." + Fore.RESET)
                    numero = input("Ingrese el número del tablero que desea ver/jugar: ")
                numero = int(numero)
                tablero = selecionartablero(numero)
                imprimeTablero(tablero, " ")
                print("Desea jugar este tablero?:")
                print("[1] Si")
                opcion = (input("[2] Regresar: "))
                opcion = opcion.split()
                while len(opcion) != 1 or not opcion[0].isdigit() or int(opcion[0]) > 2 or int(opcion[0]) < 1:
                    print(Fore.RED + "...Opción incorrecta. Intente nuevamente." + Fore.RESET)
                    opcion = (input("[2] Regresar: "))
                    opcion = opcion.split()
                opcion = int(opcion[0])
                # verificar que la opcion introducida sea valida
                if opcion == 1:
                    tablerverificar = []
                    for i in range(9):
                        tablerverificar.append([])
                        for j in range(9):
                            tablerverificar[i].append(tablero[i][j])
                    imprimeTablero(tablero, name_tablero = "")
                    while not tableroCompleto(tablero):
                        numbers = input("Ingrese fila columna cifra: ")
                        numbers = numbers.split() 
                        while verificardigitosvalidos(numbers) == False:
                            numbers = input("Ingrese fila columna cifra: ")
                            numbers = numbers.split()
                        x = int(numbers[0])
                        y = int(numbers[1])
                        d = int(numbers[2])  
                        if verificarjugadavalida(tablero, x, y, d, tablerverificar) == True:
                            tablero[x-1][y-1] = d
                            imprimeTablero(tablero, name_tablero = "")
                    creditosfinales()
                    print(Fore.MAGENTA + "Felicidades, has ganado el juego" + Fore.RESET) 
                    loop = False
                elif opcion == 2:
                    print("volviendo al menu principal")
                    loop = False
        elif opcionprincipal == 3:
            print("Selecione la dificultad del tablero")
            print(Fore.GREEN + "[1] Fácil" + Fore.RESET)
            print(Fore.YELLOW+ "[2] Medio" + Fore.RESET)
            print(Fore.RED + "[3] Difícil"+ Fore.RESET)
            opcion = (input("[4] Regresar: "))
            while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
                print(Fore.RED + "Opción incorrecta. Intente nuevamente." + Fore.RESET)
                opcion = (input("[4] Regresar: "))
            opcion = int(opcion)
            tablero = tablerodificultad(opcion)
            name = input(Fore.MAGENTA + "Nombre del jugador: " + Fore.RESET)
            name_tablero = input(Fore.LIGHTMAGENTA_EX +"Nombre del tablero: " + Fore.RESET)
            imprimeTablero(tablero, name_tablero)
            tablerverificar = []
            for i in range(9):
                tablerverificar.append([])
                for j in range(9):
                    tablerverificar[i].append(tablero[i][j])
            while not tableroCompleto(tablero):
                numbers = input("Ingrese fila columna cifra: ")
                numbers = numbers.split() 
                while verificardigitosvalidos(numbers) == False:
                    numbers = input("Ingrese fila columna cifra: ")
                    numbers = numbers.split()
                x = int(numbers[0])
                y = int(numbers[1])
                d = int(numbers[2])   
                if verificarjugadavalida(tablero, x, y, d, tablerverificar) == True:
                    tablero[x-1][y-1] = d
                    imprimeTablero(tablero, name_tablero)
            if final(tablero, name, name_tablero) == True:
                loop = False
        elif opcionprincipal == 4:
            print(Fore.RED + "Gracias por jugar."+ Fore.RESET)
            exit()
