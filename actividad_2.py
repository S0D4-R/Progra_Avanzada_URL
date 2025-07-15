import random
"""
# 1. Tabla de multiplicar: Cree un programa que imprima la tabla de multiplicar del 1 al 10 utilizando un ciclo for.
for number in range(1, 11):
    print("Esta es la tabala del {}".format(number))
    for number_x in range(1, 11):
        print(number * number_x)

# 2. Suma de pares: Pida un número al usuario y sume todos los números pares desde 1 hasta ese número usando un for.
try:
    max_match = int(input("Dame un número máximo"))
    if max_match < 0:
        print("Su número no es válido")
    else:
        prev_num = 0
        current = None
        for numbaa in range(1, max_match + 1):
            current = numbaa
            print("{}//{}".format(current, prev_num))
            if numbaa % 2 == 0:
                prev_num += current
        print("La suma total es: {}".format(prev_num))
except ValueError:
    print("Su número no es válido")

#Filtrar nombres por vocal: Solicite 10 nombres al usuario,
# guárdelos en una lista e imprima los que empiecen con vocal utilizando for.
nombres = []
vocales = ["a", "e", "i", "o", "u"]
for attempt in range(1, 11):
    nombre_x = input("Coloque un nombre")
    nombres.append(nombre_x)

for nombre in nombres:
    nombre_comparison = list(nombre)
    for vocal in vocales:
        if vocal == nombre_comparison[0].lower():
            print(nombre)
"""
#4. Pirámide de asteriscos: Pida un número n e imprima una pirámide de
# n niveles con asteriscos (*) usando un for.
""" 
#5. Múltiplos de 3: Cree una lista de 20 números aleatorios
# entre 1 y 100 e imprima solo los múltiplos de 3 utilizando for.
rand_list = []
for attempt in range(1, 21):
    numba_x = random.randint(1, 100)
    if numba_x % 3 == 0:
        rand_list.append(numba_x)
print(rand_list)
"""
""" 
#6.Contraseña con intentos infinitos: Cree un programa
# que solicite contraseñas hasta que el usuario escriba "admin123", usando un ciclo while.
key = True
contraseña = "admin123"
while key:
    attempt = input("Coloque la contraseña: ")
    if attempt == contraseña:
        print("Access Granted")
        key = False
"""
""" 
#7. Cajero automático con intentos limitados:
# Simule un cajero que permita hasta 3 intentos para ingresar el PIN correcto, luego bloquee la cuenta.
key = True
attempts = 0
while key:
    attempts += 1
    pin_lockdown = input("Coloque el PIN: ")
    if pin_lockdown == "1268":
        print("------------Bienvenido al cajero------------\n1. Retiro de dinero\n2. Salir")
        key = False
    elif attempts == 3:
        print("Cajero bloqueado, lo sentimos...")
        key = False
"""
""" 
#8. Promedio de positivos: Solicite al usuario una serie de números positivos.
# Termine cuando se ingrese uno negativo y muestre el promedio.
contador = 0
repositorio = 0
while True:
    contador += 1
    rep = int(input("Coloque un número"))
    if rep < 0:
        print(repositorio/contador)
        break
    else:
        repositorio += rep
"""
""" 
#9. Contador de pasos: Implemente un programa
# que registre los pasos caminados cada hora hasta alcanzar al menos 10,000 pasos, utilizando while.
pasos = 0
horas = 0
while not pasos >= 10000:
    horas += 1
    pasos = pasos**2 + 2
print(f"La persona caminó más de {pasos} pasos en {horas}")
"""
""" 
#10. Juego de adivinanza: El usuario debe adivinar un número secreto entre 1 y 100.
# El programa debe decirle si está por encima o por debajo hasta que acierte
secret_num = 34
while True:
    try:
        attempt = int(input("Adivine el número secreto: "))
        if attempt == secret_num:
            print("Felicidades, lo adivinó, gracias por jugar...")
            break
    except ValueError:
        print("Ese no es un número, pibe")
"""
#11. Número mayor en lista: Cree una función que reciba una lista de números y devuelva el número mayor.
""" 
#12. Área de figuras: Implemente una
# función que calcule el área de un círculo, cuadrado o triángulo, según lo elija el usuario.
key = True
while key:
    menu_op = input("Escoja la figura para calcular el área:\n1. Círculo\n2. Triángulo\n3. Cuadrado")
    match menu_op:
        case "1":
            radio = int(input("Coloque el radio del círculo: "))
            print(f"El área del círculo es: {3.1416*(radio**2)}")
            key = False
        case "2":
            base_x = int(input("Coloque la base del triángulo: "))
            height_x = int(input("Coloque la altura del triángulo: "))
            print(f"El área del triángulo es: {(base_x*height_x)/2}")
            key = False
        case "3":
            base_x = int(input("Coloque la base del cuadrado: "))
            height_x = int(input("Coloque la altura del cuadrado: "))
            print(f"El área del triángulo es: {base_x * height_x}")
            key = False
"""
""" 
#13. Conversión de temperatura: Haga una función que convierta temperaturas de Celsius a Fahrenheit y viceversa.
def convertor():
    key = True
    while key:
        mod = input("Qué desea convertir?\n1. Celsius a Farenhiet\n2.Farenheit a Celcius")
        match mod:
            case "1":
                grados = int(input("Cuántos grados va a convertir? "))
                print(f"{(grados * (9/5)) + 32} °F")
                key = False
            case "2":
                grados = int(input("Cuántos grados va a convertir? "))
                print(f"{(grados - 32) * (5 / 9)} °C")
                key = False
"""
""" 
#14. Contar vocales: Escriba una función que reciba una cadena de texto y devuelva cuántas vocales contiene.
contador = 0
vowels = ["a", "e", "i", "o", "u"]
string_ev = input("Escriba un texto")
string_ev_x = list(string_ev)
for letra in string_ev_x:
    for vowel in vowels:
        if letra.lower() == vowel:
            contador += 1

print(contador)
"""
""" 
#15. Verificador de número primo: Desarrolle una función que determine si un número ingresado es primo.
num_ver = int(input("Coloque un número"))
for test in range(2, 6):
    if num_ver**2 % test == 0:
        print("No es un número primo")
    else:
        print("El número es primo")
"""
""" 
#16.Clase Persona: Cree una clase Persona con atributos nombre y edad.
# Agregue un método que indique si la persona es mayor de edad.
class Persona: 
    def init(self, edad, nombre): 
        self.edad = edad 
        self.nombre = nombre 

    def age_tester(self): 
        if self.edad < 18: 
            print("Usted es menor de edad.") 
        else: 
            print("Usted es mayor de edad.")
"""
""" 
#17. Cuenta Bancaria: Diseñe una clase CuentaBancaria con métodos para depositar,
# retirar dinero y mostrar el saldo disponible.
class CuentaBancaria:
    def __init__(self, saldo, nombre):
        self.saldo = saldo
        self.nombre = nombre
    def deposit(self):
        destinatario = input("Coloque la cuenta a la que depositará el dinero: ")
        monto = int(input("Coloque el monto del depósito: "))
        if monto > self.saldo:
            print("Transacción no poder completarse")
        else:
            print(f"Transacción {monto} a {destinatario}")
    def retirar(self):
        monto = int(input("Coloque el monto a retirar: "))
        if monto > self.saldo:
            print("Transacción no pode completarse")
        else:
            print("Retiro exitoso")
    def available_balance(self):
        print(f"${self.saldo}")
"""
""" 
#18. Clase Producto: Implemente una clase Producto con nombre, precio y stock.
# Agregue un método para aplicar descuentos.
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def descuentos(self):
        print(self.precio - (self.precio*0.25))
"""
""" 
#19. Clase Auto: Cree una clase Auto con métodos para encender, apagar y mostrar si el auto está en marcha.
class Auto:
    def __init__(self, año, marca, estado):
        self.año = año
        self.marca = marca
        self.estado = estado
    def encender(self):
        self.estado = True
    def apagar(self):
        self.estado = False
    def marcha(self):
        if self.estado == True:
            print("El carro está en marcha")
"""
"""
#20. Clase Estudiante: Diseñe una clase Estudiante
# con atributos para almacenar notas de tres cursos y un método que calcule el promedio final.
class Student:
    def __init__(self, nombre, edad, nota_1, nota_2, nota_3):
        self.nombre = nombre
        self.edad = edad
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.nota_3 = nota_3
    def calculus(self):
        print(f"El promedio final es: {(self.nota_1 + self.nota_2 + self.nota_3)/3}")
"""
#21. Menú de cálculos: Haga un menú que permita al usuario elegir entre:
# (1) calcular un área, (2) convertir una temperatura, (3) salir del programa.
wiz = True
while wiz:
    modyyu = input("---Bienvenido---\n1. Calcular un área\n2. Convertir temperatura\nSalir")
    match modyyu:
        case "1":
            grados = int(input("Cuántos grados va a convertir? "))
            print(f"{(grados * (9 / 5)) + 32} °F")

        case "2":
            radio = int(input("Coloque el radio del círculo: "))
            print(f"El área del círculo es: {3.1416 * (radio ** 2)}")
        case "3":
            print("Gracias por usar el programa")
            wiz = False
        case _:
            print("Eso no vale")
#22. Menú con roles:
# Cree un menú que muestre diferentes opciones según el rol del usuario (administrador o estudiante).


#23. Menú de lista: Cree un menú para gestionar una lista: agregar elementos, buscar, eliminar y mostrartodo.

#24. Sistema de notas: Desarrolle un menú que permita registrar estudiantes,
# ingresar sus notas y consultar promedios.


#25. Tareas pendientes: Diseñe un sistema con menú donde el usuario pueda agregar tareas,
# marcarlas como completadas y ver la lista actual.