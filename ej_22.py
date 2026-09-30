'''
  Haz una función en Python que reciba una lista cuyos elementos pueden ser números o listas de números. A su vez, cada 
  sublista puede contener también listas de números.
  Tu función debe “aplanar” la lista recibida para que sea una lista simple de números.
  
  Ejemplo: de [1, [2, 3], [4, [5, 6, [7]]]] a [1, 2, 3, 4, 5, 6, 7].
'''


def aplanar_lista(li):
    resultado = []

    for i in li:
        if isinstance(i, list):
            resultado.extend(aplanar_lista(i))
        else:
            resultado.append(i)

    return resultado


def main():
    lista = [1, [2, 3], [4, [5, 6, [7]]]]

    print("Lista original:", lista)
    print("Lista aplanada:", aplanar_lista(lista))


if __name__ == "__main__":
    main()
