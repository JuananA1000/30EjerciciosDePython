'''
  Tienes una lista de números enteros que representa el precio de N bombones.
  También tienes una cantidad entera D de dinero.
  Tienes que comprar exactamente dos bombones de forma que te sobre la mayor cantidad (no negativa) de dinero.
  Haz una función que, para una lista de precios de bombones y una cantidad de dinero D, devuelva la cantidad que sobra 
  después de hacer la compra. Si no hay manera de comprar dos bombones, devuelve D.
'''


def sobra_compra_bombones(precios, D):
    precios.sort()
    max_sobra = D

    for i in range(len(precios)):
        for j in range(i + 1, len(precios)):
            suma = precios[i] + precios[j]
            if suma <= D:
                sobra = D - suma
                max_sobra = min(max_sobra, sobra)

    return max_sobra


def main():
    precios = [5, 10, 15, 20]
    D = 25
    resultado = sobra_compra_bombones(precios, D)

    print(resultado)


if __name__ == "__main__":
    main()
