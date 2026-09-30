'''
  Haz un programa en Python que pida dos números enteros N y M al usuario. 
  Calcula y muestra por pantalla el máximo común divisor (MCD) de N y M.
  Calcula y muestra por pantalla el mínimo común múltiplo (MCM) de N y M. 
  ¿Lo tienes? Ahora haz lo mismo pero pidiendo varios números al usuario. Almacénalos 
  en una lista y calcula el MCM y el MCD de todos ellos.
'''


def calcular_mcd(n, m):
    while m:
        n, m = m, n % m
    return n


def calcular_mcm(n, m):
    return abs(n * m) // calcular_mcd(n, m)


def main():
    numeros = input("Introduce varios números enteros separados por espacios: ")
    numeros = list(map(int, numeros.split()))

    mcd = numeros[0]
    mcm = numeros[0]

    for num in numeros[1:]:
        mcd = calcular_mcd(mcd, num)
        mcm = calcular_mcm(mcm, num)

    print(f"El MCD de {numeros} es: {mcd}")
    print(f"El MCM de {numeros} es: {mcm}")


if __name__ == "__main__":
    main()
