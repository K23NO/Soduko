import time
from colorama import Back, Fore, init
def menuprincipal():
    """Esta funcion permite imprimir el menu principal con un time sleep de 0.1""" 
    bienvenida =["█████████████████████████████████████████████████████████████████████████████████████████████", "█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░█░░░░░░██░░░░░░█","█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀░░█░░▄▀░░██░░▄▀░░█","█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░░░█░░▄▀░░██░░▄▀░░█","█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░█","█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░███░░▄▀░░██░░▄▀░░█","█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀░░██░░▄▀░░█","█░░░░░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░███░░▄▀░░██░░▄▀░░█","█████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░█","█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█","█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█","█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█","█████████████████████████████████████████████████████████████████████████████████████████████"]
    for i in bienvenida:
        print(i)
        time.sleep(0.05)
    print(Fore.BLUE +"Bienvenido al juego Sudoku del grupo GRUPO 5" + Fore.RESET) 
    print(Fore.YELLOW + "[1] Jugar tablero nuevo" + Fore.RESET) 
    print(Fore.GREEN + "[2] Ver/Jugar tablero guardado" + Fore.RESET)
    print(Fore.CYAN + "[3] Jugar tablero aleatorio por dificultad"  + Fore.RESET)

def alltableros():
    """ Aca se puede ver todos los tableros guardados y se puede elegir cual se desea jugar"""
    print("Tableros predetermniados guardados: ")
    print("[1] Tablero 1, [2] Tablero 2, [3] Tablero 3, [4] Tablero 4, [5] Tablero 5")
    print("[6] Tablero 6, [7] Tablero 7, [8] Tablero 8, [9] Tablero 9, [10] Tablero 10")
    print("[11] Tablero 11, [12] Tablero 12, [13] Tablero 13, [14] Tablero 14, [15] Tablero 15") 
    print("[16] Tablero 16, [17] Tablero 17, [18] Tablero 18, [19] Tablero 19, [20] Tablero 20")

def creditoss():
    """Esta funcion imprime los creditos del sudoku"""
    creditos = ["──────────────────────────────────────────────────────","─██████████████─██████──────────██████─████████████───","─██░░░░░░░░░░██─██░░██████████──██░░██─██░░░░░░░░████─","─██░░██████████─██░░░░░░░░░░██──██░░██─██░░████░░░░██─","─██░░██─────────██░░██████░░██──██░░██─██░░██──██░░██─", "─██░░██████████─██░░██──██░░██──██░░██─██░░██──██░░██─", "─██░░░░░░░░░░██─██░░██──██░░██████░░██─██░░██──██░░██─","─██░░██████████─██░░██──██░░░░░░░░░░██─██░░██──██░░██─", "─██░░██─────────██░░██──██████████░░██─██░░██──██░░██─", "─██░░██████████─██░░██──────────██░░██─██░░████░░░░██─", "─██░░░░░░░░░░██─██░░██──────────██░░██─██░░░░░░░░████─", "─██████████████─██████──────────██████─████████████───", "──────────────────────────────────────────────────────"]
    creditos1 = ["Game by: Grupo 5", "GRACIAS POR JUGAR yA TU ZABE","GRUPO 5 ES LA VOZ", "VIVA LA PROGRAMACION", "Real hasta muerlte brr", "#FreeTavara", "La vida, consiste en vivirla", "#Vivetuvida", "Se Veintea Progra", "#SeFiltrolaPC3", "#YaNoSoportoEsteSufrimientoUtec", "#El Sudoku se hace solo", "Traslada tu talento a la UPC", "Bye"]
    for i in creditos:
        print(Fore.LIGHTMAGENTA_EX +i + Fore.RESET)
        time.sleep(0.05)
    for i in creditos1:
        print(Fore.RED + i + Fore.RESET)
        time.sleep(0.5)

def creditosfinales():
    """Esta funcion imprime los creditos del juego cuand el usuario gana"""
    creditos = ["──────────────────────────────────────────────────────────────────────────────────────────────────────────────","─████████──████████─██████████████─██████──██████────██████──────────██████─██████████─██████──────────██████─","─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░██──██░░██────██░░██──────────██░░██─██░░░░░░██─██░░██████████──██░░██─","─████░░██──██░░████─██░░██████░░██─██░░██──██░░██────██░░██──────────██░░██─████░░████─██░░░░░░░░░░██──██░░██─","───██░░░░██░░░░██───██░░██──██░░██─██░░██──██░░██────██░░██──────────██░░██───██░░██───██░░██████░░██──██░░██─","───████░░░░░░████───██░░██──██░░██─██░░██──██░░██────██░░██──██████──██░░██───██░░██───██░░██──██░░██──██░░██─","─────████░░████─────██░░██──██░░██─██░░██──██░░██────██░░██──██░░██──██░░██───██░░██───██░░██──██░░██──██░░██─","───────██░░██───────██░░██──██░░██─██░░██──██░░██────██░░██──██░░██──██░░██───██░░██───██░░██──██░░██──██░░██─","───────██░░██───────██░░██──██░░██─██░░██──██░░██────██░░██████░░██████░░██───██░░██───██░░██──██░░██████░░██─","─────-─██░░██───────██░░██████░░██─██░░██████░░██────██░░░░░░░░░░░░░░░░░░██─████░░████─██░░██──██░░░░░░░░░░██─","───────██░░██───────██░░░░░░░░░░██─██░░░░░░░░░░██────██░░██████░░██████░░██─██░░░░░░██─██░░██──██████████░░██─","───────██████───────██████████████─██████████████────██████──██████──██████─██████████─██████──────────██████─","──────────────────────────────────────────────────────────────────────────────────────────────────────────────"]
    for i in creditos: 
        print(Fore.LIGHTBLUE_EX + i + Fore.RESET)
        time.sleep(0.02)
    
def gameover():
    """Este mensaje pertenece al easteregg del juego"""
    gameover = ["╭━━━┳━━━┳━╮╭━┳━━━╮╭━━━┳╮╱╱╭┳━━━┳━━━╮","┃╭━╮┃╭━╮┃┃╰╯┃┃╭━━╯┃╭━╮┃╰╮╭╯┃╭━━┫╭━╮┃","┃┃╱╰┫┃╱┃┃╭╮╭╮┃╰━━╮┃┃╱┃┣╮┃┃╭┫╰━━┫╰━╯┃","┃┃╭━┫╰━╯┃┃┃┃┃┃╭━━╯┃┃╱┃┃┃╰╯┃┃╭━━┫╭╮╭╯","┃╰┻━┃╭━╮┃┃┃┃┃┃╰━━╮┃╰━╯┃╰╮╭╯┃╰━━┫┃┃╰╮","╰━━━┻╯╱╰┻╯╰╯╰┻━━━╯╰━━━╯╱╰╯╱╰━━━┻╯╰━╯"]
    for i in gameover:
        print(Fore.RED + i + Fore.RESET)
        time.sleep(0.02)

