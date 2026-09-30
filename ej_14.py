'''
  Tenemos un fichero llamado agenda.txt que contiene contactos telefónicos. Cada línea está compuesta de un número de
  identificación único, un nombre (pueden ser varias palabras) y un número de teléfono.

  Por ejemplo, el contenido de un fichero con dos líneas puede ser el siguiente:
  20 María López +34612000000
  30 Pepe Martínez Contreras +17610111111

  Haz un programa que lea un fichero con este formato y cargue los datos en memoria. A continuación pedirá al usuario un
  número de identificación por teclado y el programa debe mostrar los datos del contacto con dicho número de
  identificación, en este formato (para el identificador 20):

  Nombre: María Pérez
  Teléfono: +34612000000
'''


def leer_agenda(nombre_fichero):
    agenda = {}
    with open(nombre_fichero, 'r', encoding='utf-8') as f:
        for linea in f:
            partes = linea.strip().split()
            id_contacto = partes[0]
            telefono = partes[-1]
            nombre = ' '.join(partes[1:-1])
            agenda[id_contacto] = (nombre, telefono)
    return agenda


def main():
    agenda = leer_agenda("agenda.txt")
    id_contacto = input("Introduce el número de identificación: ")

    if id_contacto in agenda:
        nombre, telefono = agenda[id_contacto]
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {telefono}")
    else:
        print("Contacto no encontrado.")


if __name__ == "__main__":
    main()
