'''
  Haz una función en Python que reciba un diccionario por parámetro y devuelva el valor más frecuente de dicho 
  diccionario y las claves en las que se encuentra.
'''

def valor_mas_frecuente(dicc):
    frecuencia = {}

    for valor in dicc.values():
        if valor in frecuencia:
            frecuencia[valor] += 1
        else:
            frecuencia[valor] = 1

    valor_mas_frecuente = max(frecuencia, key=frecuencia.get)
    claves_con_valor_mas_frecuente = [clave for clave, valor in dicc.items() if valor == valor_mas_frecuente]

    return valor_mas_frecuente, claves_con_valor_mas_frecuente


# Ejemplo de uso
diccionario = {
    'a': 1,
    'b': 2,
    'c': 4,
    'd': 3,
    'e': 4,
    'f': 2,
    'g': 4
}
valor, claves = valor_mas_frecuente(diccionario)
print(f"Valor más frecuente: {valor}")
print(f"Claves con ese valor: {claves}")
