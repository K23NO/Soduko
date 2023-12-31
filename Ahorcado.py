import random
from SudokuF import creditosfinales
from SudokuF import gameover
from colorama import Back, Fore, init
import time
# by: google.com
def jueguito():
    AHORCADO = ['''
        +---+
        |   |
            |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========''']
    palabras = 'Fernando Palomita AguaMarina TonyRosado Copilot Mrc Dormilon Juguito PanConPapitas Dota Otorrinolaringologo izy twitch Fallguys funar trika Papitas Semanaveinte Lofi bzrp seveintea secerea help sos ProfeNoMeJalePlis Gaaa awa ñ visualgod quieromiveinte Halloween yanoquieroseringeniero ZzZzZz jalados Utec ELMT losmalditosdeprogra terrible pipipi Cumbion'
    palabras = palabras.lower()
    palabras = palabras.split()
    
    def buscarPalabraAleat(listaPalabras):
        # Esta funcion retorna una palabra aleatoria.
        palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
        return listaPalabras[palabraAleatoria]
    
    def displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta):
        print(AHORCADO[len(letraIncorrecta)])
        print ("")
        fin = " "
        print ('Letras incorrectas:', fin)
        for letra in letraIncorrecta:
            print (letra, end = "")
        print ("")
        print(Fore.MAGENTA + "Palabra a adivinar:" + Fore.RESET)
        espacio = '_' * len(palabraSecreta)
        for i in range(len(palabraSecreta)): # Remplaza los espacios en blanco por la letra bien escrita
            if palabraSecreta[i] in letraCorrecta:
                espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:]
        for letra in espacio: # Mostrará la palabra secreta con espacios entre letras
            print (letra, fin)
        print ("")
    
    def elijeLetra(algunaLetra):
        # Devuelve la letra que el jugador ingreso. Esta función hace que el jugador ingrese una letra y no cualquier otra cosa
        while True:
            print ('Adivina una letra:', end = " ")
            letra = input()
            letra = letra.lower()
            if len(letra) != 1:
                print ('Introduce una sola letra.') 
            elif letra in algunaLetra:
                print ('Ya has elegido esa letra ¿Qué tal si pruebas con otra?')
            elif letra not in 'abcdefghijklmnopqrstuvwxyz':
                print ('Elije una letra.')
            else:
                return letra
    
    def empezar():
        # Esta funcion devuelve True si el jugador quiere volver a jugar, de lo contrario devuelve False
        print ('Quieres jugar de nuevo? (Si o No)')
        return input().lower().startswith('s')
    
    ah = ["░█████╗░██╗░░██╗░█████╗░██████╗░░█████╗░░█████╗░██████╗░░█████╗░","██╔══██╗██║░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗","███████║███████║██║░░██║██████╔╝██║░░╚═╝███████║██║░░██║██║░░██║","██╔══██║██╔══██║██║░░██║██╔══██╗██║░░██╗██╔══██║██║░░██║██║░░██║","██║░░██║██║░░██║╚█████╔╝██║░░██║╚█████╔╝██║░░██║██████╔╝╚█████╔╝","╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░"]
    for i in ah:
        print(Fore.BLUE + i + Fore.RESET)
        time.sleep(0.1)
    letraIncorrecta = ""
    letraCorrecta = ""
    palabraSecreta = buscarPalabraAleat(palabras)
    finJuego = False
    while True:
        displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
        # El usuairo elije una letra.
        letra = elijeLetra(letraIncorrecta + letraCorrecta)
        if letra in palabraSecreta:
            letraCorrecta = letraCorrecta + letra
            # Se fija si el jugador ganó
            letrasEncontradas = True
            for i in range(len(palabraSecreta)):
                if palabraSecreta[i] not in letraCorrecta:
                    letrasEncontradas = False
                    break
            if letrasEncontradas:
                creditosfinales()
                print ('¡Muy bien! La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
                finJuego = True
        else:
            letraIncorrecta = letraIncorrecta + letra
            # Comprueba la cantidad de letras que ha ingresado el jugador y si perdió
            if len(letraIncorrecta) == len(AHORCADO) - 1:
                displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
                gameover()
                print ('¡Se ha quedado sin letras!\nDespues de ' + str(len(letraIncorrecta)) + ' letras erroneas y ' + str(len(letraCorrecta)) + ' letras correctas, la palabra era "' + palabraSecreta + '"')
                finJuego = True
        # Pregunta al jugador si quiere jugar de nuevo
        if finJuego:
            if empezar():
                letraIncorrecta = ""
                letraCorrecta = ""
                finJuego = False
                palabraSecreta = buscarPalabraAleat(palabras)
            else:
                break


