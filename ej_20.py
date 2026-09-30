'''
  Haz una función en Python que reciba una cadena de texto por parámetro y que devuelva la suma de todos los números que 
  haya en esa cadena de texto. 
  
  Por ejemplo: para la cadena de texto “Tengo 5 gatos con 4 patas cada uno. Uno tiene 12 años.” habría que devolver el 
  valor 21
'''

import re

texto = "Tengo 5 gatos con 4 patas cada uno. Uno tiene 12 años."
numeros = re.findall(r'\d+', texto)
suma = sum(int(num) for num in numeros)

print(suma)  # Salida: 21
