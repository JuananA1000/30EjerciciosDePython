'''
  Haz un programa que muestre por pantalla los N primeros elementos de la sucesión de Fibonacci. 
  Mmmm, y ahora, escríbelos a un fichero llamado fibonacci.txt. 
'''

n = 10
a, b = 0, 1

fibonacci_numbers = []

for _ in range(n):
    fibonacci_numbers.append(str(a))
    a, b = b, a + b

# Mostrar por pantalla
print(' '.join(fibonacci_numbers))

# Escribir en el fichero
with open('fibonacci.txt', 'w') as file:
    file.write(' '.join(fibonacci_numbers))
