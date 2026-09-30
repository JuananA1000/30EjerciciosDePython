'''
  Haz una función en Python que reciba una lista de números por parámetro y devuelva el número de buenos pares que 
  contiene. Un buen par de números está definido por las siguientes condiciones:
  
  - numeros[i] == numeros[j]
  
  - i < j
'''

def contar_buenos_pares(li):
    contador = 0

    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            if li[i] == li[j]:
                contador += 1

    return contador


def main():
    numeros = [1, 2, 3, 1, 1, 3]
    print(contar_buenos_pares(numeros))


if __name__ == "__main__":
    main()
