'''
  Haz un programa en Python que pida números al usuario que se vayan almacenando en una lista. El programa deja de pedir 
  números cuando el usuario introduce un cero. 
  Muestra por pantalla los números en posición par de la lista. 
  Muestra por pantalla los números en orden inverso. 
  Parte la lista en dos mitades. Si el número de elementos es impar, no importa qué mitad tiene un elemento más. Muestra 
  las dos mitades por pantalla. Muestra por pantalla todos los elementos de la primera mitad, exceptuando el primero y 
  el último. Muestra por pantalla el máximo y el mínimo de la segunda mitad. 
'''

lista_num = []
while True:
    num = int(input("Introduce un número (0 para terminar): "))
    if num == 0:
        break
    lista_num.append(num)

print("\nLista completa: ", end="")
for num in lista_num:
    print(num, end=" ")

print("\nNúmeros en posición par:", end=" ")
for i in range(1, len(lista_num), 2):
    print(lista_num[i], end=" ")

print("\nNúmeros en orden inverso:", end=" ")
for num in reversed(lista_num):
    print(num, end=" ")

print("\n\nMitades de la lista:")
mid = len(lista_num) // 2
primera_mitad = lista_num[:mid]
segunda_mitad = lista_num[mid:]
print(f"Primera mitad: {primera_mitad}")
print(f"Segunda mitad: {segunda_mitad}")
print("Elementos de la primera mitad, exceptuando el primero y el último:", end=" ")
for num in primera_mitad[1:-1]:
    print(num, end=" ")
if segunda_mitad:
    print(f"\nMáximo de la segunda mitad: {max(segunda_mitad)}")
    print(f"Mínimo de la segunda mitad: {min(segunda_mitad)}")
