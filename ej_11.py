'''
  Haz un programa en Python que dibuje por pantalla los siguientes patrones para un
  número N leído por teclado. Por ejemplo, para N = 5:

  *****
  ****
  ***
  **
  *

  *****
  *   *
  *   *
  *   *
  *****

  * * *
   * *
  * * *
   * *
  * * *

    *
   ***
  *****
'''


def triangulo_invertido(num):
    for i in range(num, 0, -1):
        print('*' * i)


def cuadrado_vacio(num):
    for i in range(num):
        if i == 0 or i == num - 1:
            print('*' * num)
        else:
            print('*' + ' ' * (num - 2) + '*')


def patron_alternado(num):
    for i in range(num):
        if i % 2 == 0:
            print('* ' * (num // 2 + num % 2))
        else:
            print(' ' + '* ' * (num // 2))


def piramide_virtual(num):
    for i in range(1, num + 1, 2):
        espacios = (num - i) // 2
        print(" " * espacios + "*" * i)


def main():
    n = int(input("Introduce un número: "))

    print("\nTriángulo invertido:")
    triangulo_invertido(n)

    print("\nCuadrado vacío:")
    cuadrado_vacio(n)

    print("\nPatrón alternado:")
    patron_alternado(n)

    print("\nPirámide virtual:")
    piramide_virtual(n)


if __name__ == "__main__":
    main()
