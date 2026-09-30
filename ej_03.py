'''
  Haz un programa que pida tres números al usuario y muestre por pantalla cuál es el mínimo y cuál es el máximo y que
  indique si son pares o impares. No uses listas.
'''

print(f'\nIngresa 3 números: ')
num1 = int(input('n1: '))
num2 = int(input('n2: '))
num3 = int(input('n3: '))

mayor = num1
menor = num1

if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print(f'\nCálculos a mano:')
print(f'El {mayor} es el mayor')
print(f'El {menor} es el menor')

# También se puede hacer con la función max() y min()

print(f'\nCálculos con funciones:')
print(f'El {max(num1, num2, num3)} es el mayor')
print(f'El {min(num1, num2, num3)} es el menor')
