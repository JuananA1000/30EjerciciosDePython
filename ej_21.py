'''
  Haz una función que reciba una lista de palabras por parámetro. La función debe devolver otra lista con aquellas 
  palabras que pueden ser escritas en un teclado QWERTY utilizando solo una fila del teclado.
  La primera fila de un teclado QWERTY tiene las letras "qwertyuiop", la segunda tiene "asdfghjklñ", y la tercera tiene 
  "zxcvbnm".
'''


def palabras_una_fila(lista_palabras):
    fila1 = set("qwertyuiop")
    fila2 = set("asdfghjklñ")
    fila3 = set("zxcvbnm")

    resultado = []

    for palabra in lista_palabras:
        letras = set(palabra.lower())

        if (
            letras.issubset(fila1) or
            letras.issubset(fila2) or
            letras.issubset(fila3)
        ):
            resultado.append(palabra)

    return resultado


def main():
    palabras = ["dad", "tipo", "casa", "alas", "pop", "zxc"]
    print(palabras_una_fila(palabras))


if __name__ == "__main__":
    main()
