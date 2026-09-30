'''
  Tienes una lista de N números enteros. Cada número representa la calificación de un niño.
  Les vas a repartir caramelos de forma que cada niño tenga al menos un caramelo.
  Además, un niño debe tener más caramelos que sus vecinos (los que están junto a él en la lista) si tiene una 
  calificación más alta que ellos.
  Haz una función que, para la lista de calificaciones de niños, devuelva el número mínimo de caramelos necesarios que 
  hay que repartir para que se cumplan las condiciones.
'''

def repartir_caramelos(calificaciones):
    n = len(calificaciones)
    caramelos = [1] * n

    for i in range(1, n):
        if calificaciones[i] > calificaciones[i - 1]:
            caramelos[i] = caramelos[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if calificaciones[i] > calificaciones[i + 1]:
            caramelos[i] = max(caramelos[i], caramelos[i + 1] + 1)

    return sum(caramelos)

def main():
    calificaciones = [1, 0, 2]
    resultado = repartir_caramelos(calificaciones)

    print(resultado)

if __name__ == "__main__":
    main()