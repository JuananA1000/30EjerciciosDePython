'''
  Le tengo un poco de manía al típico ejercicio de “Hola, Mundo”. Esta es una alternativa un pelín más compleja.

  Haz un programa en Python que pida por teclado al usuario su nombre, su edad y su altura en metros. 
  Después muestra por pantalla un mensaje del tipo: 

  “El usuario NOMBRE, de EDAD años de edad y mide ALTURA metros”. 
  ¿Eres capaz de modificarlo para que el mensaje sea de la siguiente manera? Solo pidiendo los tres valores indicados. 
  “El usuario NOMBRE, de EDAD años de edad y mide METROS metros y CENTÍMETROS centímetros.”.

  Ejemplos: 
  “El usuario Juan tiene 44 años de edad y mide 1.85 metros”. 
  “El usuario Juan tiene 44 años de edad y mide 1 metro y 85 centímetros”. 
'''

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
altura = float(input("Introduce tu altura en metros: "))  # Introducir la altura con PUNTO, por ejemplo: 1.85

metros = int(altura)
centimetros = int((altura - metros) * 100)

print(f"El usuario {nombre}, de {edad} años de edad y mide {altura} metros.")
print(f"El usuario {nombre}, de {edad} años de edad y mide {metros} metros y {centimetros} centímetros.")
