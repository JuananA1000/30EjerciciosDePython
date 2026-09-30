'''
  Una transacción es probablemente inválida si excede de 1000$ o si ocurre dentro de un intervalo de 60 minutos con otra 
  transacción con el mismo nombre pero en diferente ciudad.
  Tenemos una lista de cadenas de texto que consisten en valores separados por comas y que representan, en este orden, 
  el nombre de la transacción, el tiempo (en minutos desde la primera transacción), la cantidad en $ y la ciudad. 
  Por ejemplo: [“Juan, 0, 500, Madrid”, “Rubén, 30, 750, Barcelona”].
  Haz una función que para una lista de transacciones devuelva aquellas que son probablemente inválidas.
'''


def transacciones_invalidas(transac):
    invalidas = []

    for i in range(len(transac)):
        nombre, tiempo, cantidad, ciudad = transac[i].split(',')
        cantidad = int(cantidad)
        tiempo = int(tiempo)

        if cantidad > 1000:
            invalidas.append(transac[i])
        else:
            for j in range(len(transac)):
                if i != j:
                    nombre2, tiempo2, cantidad2, ciudad2 = transac[j].split(',')
                    cantidad2 = int(cantidad2)
                    tiempo2 = int(tiempo2)

                    if nombre == nombre2 and ciudad != ciudad2 and abs(tiempo - tiempo2) <= 60:
                        invalidas.append(transac[i])
                        break

    return invalidas


def main():
    transac = ["Juan, 0, 500, Madrid", "Rubén, 30, 750, Barcelona",
               "Juan, 20, 1500, Valencia", "Juan, 50, 200, Barcelona"]
    resultado = transacciones_invalidas(transac)
    print(resultado)


if __name__ == "__main__":
    main()
