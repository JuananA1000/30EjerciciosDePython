'''
  Haz un programa en Python para convertir de un número decimal a uno binario. 
  Y para convertir uno binario en decimal. 
  No te olvides del octal y el hexadecimal. 
'''


def decimal_a_binario(decimal):
    binario = ""

    while decimal > 0:
        binario = f"{decimal % 2}{binario}"
        decimal = decimal // 2

    if binario == "":
        return "0"
    else:
        return binario


def decimal_a_octal(decimal):
    octal = ""

    while decimal > 0:
        octal = f"{decimal % 8}{octal}"
        decimal = decimal // 8

    if octal == "":
        return "0"
    else:
        return octal


def decimal_a_hexadecimal(decimal):
    hexadecimal = ""
    caracteres_hexadecimales = "0123456789ABCDEF"

    while decimal > 0:
        hexadecimal = f"{caracteres_hexadecimales[decimal % 16]}{hexadecimal}"
        decimal = decimal // 16

    if hexadecimal == "":
        return "0"
    else:
        return hexadecimal


def binario_a_decimal(binario):
    decimal = 0
    potencia = 0

    for digito in reversed(binario):
        if digito == "1":
            decimal += 2 ** potencia
        potencia += 1

    return decimal


def main():
    num_decimal_input = int(input("Introduce un número decimal: "))
    num_binario_input = input("\nIntroduce un número binario: ")

    numero_binario = decimal_a_binario(num_decimal_input)
    numero_decimal = binario_a_decimal(num_binario_input)
    numero_octal = decimal_a_octal(num_decimal_input)
    numero_hexadecimal = decimal_a_hexadecimal(num_decimal_input)

    print(f"\nEl número {num_decimal_input} en binario es: {numero_binario}")
    print(f"El número {num_binario_input} en decimal es: {numero_decimal}")
    print(f"El número {num_decimal_input} en octal es: {numero_octal}")
    print(f"El número {num_decimal_input} en hexadecimal es: {numero_hexadecimal}")


if __name__ == "__main__":
    main()
