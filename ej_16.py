'''
  Haz una programa en Python que ordene una lista de tuplas. Cada tupla tiene dos elementos. La lista debe quedar 
  ordenada de mayor a menor por el segundo elemento de cada tupla.
'''
lista_tuplas = [(1, 3), (2, 1), (3, 2)]
lista_ordenada = sorted(lista_tuplas, key=lambda x: x[1], reverse=True)
print(lista_ordenada)
