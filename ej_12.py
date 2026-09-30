'''
  Haz un programa en Python que compruebe la validez de un password introducido
  por pantalla.
  El password debe cumplir todas estas condiciones para ser válido:
  - Al menos una letra minúscula (a-z) y al menos una mayúscula (A-Z).
  - Al menos un número (0-9).
  - Al menos un símbolo (#, $, /, @).
  - Al menos 10 caracteres de longitud.
'''


def es_valido(password):
    if len(password) < 10:
        return False

    tiene_mayuscula = any(c.isupper() for c in password)
    tiene_minuscula = any(c.islower() for c in password)
    tiene_numero = any(c.isdigit() for c in password)
    tiene_simbolo = any(c in '#$/@' for c in password)

    return tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_simbolo


def main():

    while True:
        password = input("Introduce un password: ")

        if es_valido(password) or password == "exit":
            print("El password es válido.")
            break
        else:
            print("El password no es válido.")


if __name__ == "__main__":
    main()
