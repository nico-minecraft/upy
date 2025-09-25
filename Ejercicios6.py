# Ejercicio 1
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for i, nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(i)


# Ejercicio 2
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

# Edad mínima
edad_minima = min(diccionario_edades.values())

# Último nombre alfabéticamente
ultimo_nombre = max(diccionario_edades.keys())

print("Edad mínima:", edad_minima)
print("Último nombre:", ultimo_nombre)

# Ejercicio 3
import random

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
numeros = [15, 82, 92, 641, 54]

# Unir las dos listas
lista_total = nombres + numeros

# Escoger uno al azar
sorteo = random.choice(lista_total)

print("Elemento sorteado:", sorteo)


# Ejercicio 4
temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [(f - 32) * (5/9) for f in temperatura_fahrenheit]

print("Temperaturas en °C:", grados_celsius)


#Ejercicio 5
# Pedir nombre al usuario
nombre = input("Ingresa tu nombre: ")

print(f"\nBueno, {nombre}, he pensado un número entre 1 y 100, "
      "y tienes solo ocho intentos para adivinar cuál es el número.\n")

# Número secreto
numero_secreto = random.randint(1, 100)

# Intentos permitidos
intentos = 8

for intento in range(1, intentos + 1):
    try:
        numero = int(input(f"Intento {intento}: Ingresa tu número: "))
    except ValueError:
        print("Eso no es un número válido. Intenta de nuevo.")
        continue
    
    # Validar rango
    if numero < 1 or numero > 100:
        print("Has elegido un número fuera del rango permitido (1-100).")
        continue
    
    # Comparar con número secreto
    if numero < numero_secreto:
        print("Incorrecto. Has elegido un número menor al número secreto.\n")
    elif numero > numero_secreto:
        print("Incorrecto. Has elegido un número mayor al número secreto.\n")
    else:
        print(f"Adivinaste el número secreto ({numero_secreto}) "
              f"en {intento} intento(s).")
        break
else:
    print(f"Has agotado tus 8 intentos. "
          f"El número secreto era {numero_secreto}.")
