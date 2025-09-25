# Ejercicio 1
def cuadrado(numero):
    print(numero ** 2)

print(cuadrado(5))   # imprime 25



# Ejercicio 2
def invertir_palabra(palabra):
    return palabra[::-1].upper()

# Ejemplo
print(invertir_palabra("minecraft"))

# Ejercicio 3
def contar_pares(lista):
    return sum(1 for n in lista if n % 2 == 0)

# Ejemplo
lista_numeros = [1, -50, 502, -5000, 755, 600, 33, 61]
print(contar_pares(lista_numeros))

# Ejercicio 4
import random
def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])

def procesar_resultado(resultado, lista):
    if resultado == "Cara":
        print("La lista se autodestruirá")
        return []
    elif resultado == "Cruz":
        print("La lista fue salvada")
        return lista

lista_numeros = [10, 20, 30, 40]

resultado = lanzar_moneda()
print(f"moneda: {resultado}")

lista_final = procesar_resultado(resultado, lista_numeros)
print("Lista resultante:", lista_final)


# Ejercicio 5
def suma_absolutos(*args):
    return sum(abs(num) for num in args)

# Ejemplo
print(suma_absolutos(5, -3, -7, 10))  

# Ejercicio 6
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for atributo, valor in kwargs.items():
        print(f"{atributo}: {valor}")

# Ejemplo
describir_persona("nico", color_ojos="negros", color_pelo="negro")
