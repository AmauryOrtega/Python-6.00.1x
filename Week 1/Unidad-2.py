# -*- coding: utf-8 -*-
"""
Created on 03/09/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""

import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


hi = "Hello"
name = "Amaury"

greetings = hi + " " + name

print(greetings)

# Operaciones con string

# Concatenacion
print('ab' + 'cd')

# Concatenacion sucesiva
print(3 * "amaury")

# Tamaño
print(len("amaury"))

# Indexacion
print("amaury"[0])
print("amaury"[1])  # Si se pone un numero (+) muy grande, IndexError
print("amaury"[-1])  # Cuenta desde "y" hasta "a"

# Separar
"""
[#1:#2:#3]
Desde #1 hasta justo antes de #2
si #1 no esta, se toma desde 0
si #2 no esta, se toma hasta el final
si solo se pone :, se hace una _copia_ de todo
"""
print("amaury"[1:3])
print("amaury"[:3])
print("amaury"[1:len("amaury")])
print("amaury"[:])

cls()

x = 1
x_str = str(x)
print("my number is", x, ".", "x = ", x)
print("my number is " + x_str + ". " + "x = " + x_str)
print("my number is {0}. x = {1}".format(x_str, x_str))

cls()

texto = input("Ingrese algo: ")
numero = int(input("Ingrese numero: "))

cls()
# Forma tradicional
n = 0
while n < 5:
    print(n)
    n += 1

# Reemplaza al <
n = 0
for n in range(5):
    print(n)

# Limites inf y sup
n = 0
for i in range(7, 10):
    n += i
print(n)

# Incrementos
n = 0
for i in range(5, 11, 2):
    n += i
print(n)

# Salir de loop
n = 0
for i in range(5, 11, 2):
    n += i
    if n == 5:
        break
print(n)

cls()

# X^2
x = 3
answer = 0
pasos = x
while pasos != 0:
    answer += x
    pasos -= 1
print(str(x) + "*" + str(x) + " = " + str(answer))

# Guess and check method
# Raiz cubica
x = int(input("Ingrese un entero: "))
answer = 0
while answer ** 3 < x:
    answer += 1
if answer ** 3 != x:
    print(str(x) + " no es un cubo perfecto")
else:
    print("Raiz cubica de " + str(x) + " es " + str(answer))

# Raiz cubica con signo
x = int(input("Ingrese un entero: "))
answer = 0
while answer ** 3 < abs(x):
    answer += 1
if answer ** 3 != abs(x):
    print(str(x) + " no es un cubo perfecto")
else:
    if x < 0:
        answer = - answer
    print("Raiz cubica de " + str(x) + " es " + str(answer))

# Guess and check con for
cube = 8
for guess in range(cube + 1):
    if guess ** 3 == cube:
        print("Raiz cubica de", cube, "is", guess)

# Mejora
cube = 8
guess = 0
for guess in range(abs(cube + 1)):
    if guess ** 3 >= abs(cube):
        break
if guess ** 3 != abs(cube):
    print(cube, "is not a perfect cube")
else:
    if cube < 0:
        guess = -guess
    print("Raiz cubica de", cube, "is", guess)
