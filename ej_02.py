'''
  Haz un programa de Python que pida un número entero N al usuario entre 10 y 20. 
  Muestra por pantalla todos los números enteros entre el 1 y el N. 
  Muestra por pantalla todos los números enteros entre el 30 y el N, en orden inverso. 
'''

num = int(input("Introduce un número entero entre 10 y 20: "))

if num <= 10 or num >= 20:
    print("Número no válido. Por favor, introduce un número entre 10 y 20.")
else:
    print(f"\nNúmeros enteros entre 1 y {num}:", end=" ")
    for i in range(1, num + 1):
        print(i, end=" ")

    print(f"\nNúmeros enteros entre 30 y {num}:", end=" ")
    for i in range(30, num - 1, -1):
        print(i, end=" ")
    print()
