'''
  Haz un programa en Python que convierta de números romanos a enteros y de enteros a números romanos.
'''


def romano_a_entero(num):
    # Diccionario con los valores de los símbolos romanos
    simbolos = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    resultado = 0
    prev_value = 0

    for char in num:
        value = simbolos[char]

        # Si el valor actual es mayor que el valor anterior, restamos el doble del valor anterior
        if prev_value < value:
            resultado += value - 2 * prev_value
        else:
            resultado += value

        prev_value = value

    return resultado


def entero_a_romano(num):
    # Lista de tuplas con los valores y sus símbolos romanos (ordenados de mayor a menor)
    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    resultado = ""
    for valor, simbolo in valores:
        # Mientras el número sea mayor o igual al valor actual
        while num >= valor:
            resultado += simbolo
            num -= valor

    return resultado


def main():
    print("\nRomano -> entero:")
    print(romano_a_entero("MCDLXXXVIII"))  # Salida: 1488
    print(romano_a_entero("MMXXVI"))   # Salida: 2026

    print("\nEntero -> romano:")
    print(entero_a_romano(1987))  # Salida: MCMLXXXVII
    print(entero_a_romano(449))   # Salida: CDXLIX


if __name__ == "__main__":
    main()
