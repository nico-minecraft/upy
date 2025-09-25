import random

# EJERCICIO 1
def funcion1(x, y, z):
    suma = x + y + z
    numeros = [x, y, z]
    if suma > 15:
        return max(numeros)
    elif suma < 10:
        return min(numeros)
    else:
        return sorted(numeros)[1] 
    
# EJERCICIO 2    
def funcion2(palabra):
    return sorted(list(set(palabra)))

# EJERCICIO 3
def funcion3(*args):
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i+1] == 0:
            return True
    return False

# EJERCICIO 4
def lista_palitos():
    return ['-', '--', '---', '----']

def mezclar_palitos(palitos):
    random.shuffle(palitos)
    return palitos

def pedir_intento():
    intento = 0
    while intento not in [1, 2, 3, 4]:
        try:
            intento = int(input("Elige un número del 1 al 4: "))
        except ValueError:
            continue
    return intento

def comprobar_intento(palitos, intento):
    if palitos[intento - 1] == '-':
        print("¡Perdiste! Te toca comprar papitas.")
    else:
        print("¡Te salvaste!")

# palitos main
def jugar_palitos():
    palitos = lista_palitos()
    palitos = mezclar_palitos(palitos)
    intento = pedir_intento()
    comprobar_intento(palitos, intento)



# EJERCICIO 5

palabras = ["ros", "python", "marrufo", "tiburon", "tepache"]

def elegir_palabra(palabras):
    return random.choice(palabras)

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    return ' '.join([letra if letra in letras_adivinadas else '_' for letra in palabra_secreta])

def pedir_letra(letras_usadas):
    while True:
        letra = input("Elige una letra: ").lower()
        if len(letra) == 1 and letra.isalpha() and letra not in letras_usadas:
            return letra
        print("Letra inválida o ya usada. Intenta de nuevo.")

def ahorcado():
    palabra = elegir_palabra(palabras)
    letras_adivinadas = set()
    letras_usadas = set()
    vidas = 6

    print("¡Bienvenido al juego del Ahorcado!")
    while vidas > 0:
        print(f"\nPalabra: {mostrar_tablero(palabra, letras_adivinadas)}")
        print(f"Vidas restantes: {vidas}")
        print(f"Letras usadas: {' '.join(sorted(letras_usadas))}")
        letra = pedir_letra(letras_usadas)
        letras_usadas.add(letra)
        if letra in palabra:
            letras_adivinadas.add(letra)
            if all(l in letras_adivinadas for l in palabra):
                print(f"¡Felicidades! Adivinaste la palabra: {palabra}")
                return
        else:
            vidas -= 1
            print("¡Letra incorrecta!")
    print(f"Perdiste. La palabra era: {palabra}")
    
    
print("Funciones posibles:\nfuncion1(x, y, z) - Ingresar 3 números distintos\nfuncion2(palabra) - Ingresar una palabra\nfuncion3(*args) - Ingresar números indefinidos\njugar_palitos() - Jugar palitos\nahorcado() - Jugar ahorcado   ")