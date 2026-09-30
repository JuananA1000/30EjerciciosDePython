'''
  Tenemos una lista de números enteros que representan los pesos de N piedras. Ahora vamos a jugar a un juego. Se trata 
  de tomar las dos piedras más pesadas y hacerlas chocar entre sí. Si los pesos de las piedras son iguales, ambas quedan 
  destruidas. Si no, la más ligera queda destruida y la mayor pasa a tener el peso que tenía restándole el de la más
  ligera. Las piedras destruidas se eliminan de la lista. Y así, se sigue jugando hasta que solo queda una piedra. O 
  ninguna, que puede suceder.
  Haz una función en Python que, para una lista con los pesos de las piedras, devuelva el peso final de la piedra 
  ganadora. O cero si no queda ninguna
'''


def piedra_ganadora(piedras):

    while len(piedras) > 1:
        piedras.sort()
        piedra1 = piedras.pop()
        piedra2 = piedras.pop()
        if piedra1 != piedra2:
            piedras.append(piedra1 - piedra2)

    return piedras[0] if piedras else 0


def main():
    piedras = [25, 7, 34, 18, 45, 6]
    resultado = piedra_ganadora(piedras)

    print(resultado)


if __name__ == "__main__":
    main()
