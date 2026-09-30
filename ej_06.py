'''
  Pide al usuario las coordenadas X e Y de dos puntos en el espacio. 
  Muestra por pantalla la distancia en línea recta entre esos dos puntos. 
  Muestra por pantalla las coordenadas del punto medio exacto de ambos.   
'''

import math


def calcular_distancia(p1, p2):
    # d = √((x2 - x1)² + (y2 - y1)²)
    distancia = math.sqrt(math.pow(p2[0] - p1[0], 2) + math.pow(p2[1] - p1[1], 2))

    return distancia


def calcular_punto_medio(p1, p2):
    punto_medio = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]

    return punto_medio


def main():
    punto1 = [int(input("P1(x): ")),
              int(input("P1(y): "))]

    punto2 = [int(input("\nP2(x): ")),
              int(input("P2(y): "))]

    distancia = calcular_distancia(punto1, punto2)
    print(f"\nLa distancia entre los puntos es: {distancia}")

    punto_medio = calcular_punto_medio(punto1, punto2)
    print(f"El punto medio entre los puntos es: {punto_medio}")


if __name__ == "__main__":
    main()
