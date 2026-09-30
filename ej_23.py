'''
  Haz una función en Python que reciba una lista de números por parámetro y la ordene. Implementa para ello el algoritmo 
  quicksort.
'''


def quicksort(li):
    if len(li) <= 1:
        return li  # caso base

    pivote = li[len(li) // 2]

    menores = [i for i in li if i < pivote]
    iguales = [i for i in li if i == pivote]
    mayores = [i for i in li if i > pivote]

    return quicksort(menores) + iguales + quicksort(mayores)


def main():
    numeros = [3, 6, 8, 10, 1, 2, 1]
    print(quicksort(numeros))


if __name__ == "__main__":
    main()
