'''
  Dada una cadena de texto que representa un número entero N no negativo y un número entero K, haz una función que 
  devuelva el número entero más pequeño resultante de eliminar K dígitos de N.
'''


def eliminar_digitos(N, K):
    digitos = list(N)
    for _ in range(K):
        for i in range(len(digitos) - 1):
            if digitos[i] > digitos[i + 1]:
                del digitos[i]
                break
        else:
            digitos.pop()
    return ''.join(digitos).lstrip('0') or '0'


def main():
    numero_N = "1432219"
    numero_K = 3
    resultado = eliminar_digitos(numero_N, numero_K)

    print(resultado)


if __name__ == "__main__":
    main()
