'''
  Haz un programa que reciba un número que represente una cantidad de dinero D, incluyendo céntimos. Calcula la mínima 
  cantidad de monedas necesarias para sumar D, suponiendo que tenemos monedas de 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, y 
  0.01. 
  Muestra por pantalla la cantidad de cada una de las monedas. 
'''


def calcular_monedas(dinero):
    monedas = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    cantidad_monedas = {}

    for moneda in monedas:
        cantidad_monedas[moneda] = int(dinero // moneda)
        dinero -= cantidad_monedas[moneda] * moneda

    return cantidad_monedas


def main():
    dinero = float(input("Introduce la cantidad de dinero (incluyendo céntimos): "))
    resultado = calcular_monedas(dinero)

    print("Cantidad de monedas necesarias:")
    for moneda, cantidad in resultado.items():
        print(f"{cantidad} monedas de {moneda}€")

    print("_________________________________")
    print(f" \n {dinero:.2f}€")


if __name__ == "__main__":
    main()
