'''
  Haz un programa en Python que pida 10 números al usuario y los almacene en una lista. 
  Muestra todos los números por pantalla indicando junto a cada número un mensaje que diga “NEGATIVO” si dicho número es 
  negativo. 
  ¿Lo tienes? Modifícalo para que muestre “REPETIDO” al lado de cada número que se encuentre más de una vez en la lista. 
'''

print("Introduce 10 números:")

numeros = []
for i in range(10):
    num = int(input(f"Número {i + 1}: "))
    numeros.append(num)

print("\nNúmeros ingresados:")
for num in numeros:
    if num < 0:
        print(f"{num} NEGATIVO")
    else:
        print(f"{num}")

    if numeros.count(num) > 1:
        print(f"{num} REPETIDO")
