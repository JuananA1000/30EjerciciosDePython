'''
  Haz una función en Python que reciba una lista por parámetro y devuelva dos listas diferentes, una con los elementos 
  de la lista recibida, pero sin los repetidos, y otra con los repetidos.

  Por ejemplo, de [1, 2, 3, 2, 2, 3, 4] se devuelve [1, 2, 3, 4] y [2, 2, 3].
'''


def extraer_repetidos(lista):
    sin_repetidos = []
    repetidos = []

    for i in lista:
        if i not in sin_repetidos:
            sin_repetidos.append(i)
        else:
            repetidos.append(i)

    return sin_repetidos, repetidos


def main():

    lista = []
    print("Números para la lista ('fin' para terminar):")

    j = 0
    while True:
        num = input(f"Número [{j + 1}]: ")

        if num == "fin":
            break
        lista.append(num)
        j += 1

    sin_repetidos, repetidos = extraer_repetidos(lista)

    print("Sin repetidos:", sin_repetidos)
    print("Repetidos:", repetidos)


if __name__ == "__main__":
    main()
