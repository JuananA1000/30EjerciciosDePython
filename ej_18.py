'''
  Haz un programa de Python que lea dos matrices de números enteros y muestre por pantalla el resultado de 
  multiplicarlas
'''
mat1 = [[1, 2],
        [3, 4]]

mat2 = [[5, 6, 3],
        [7, 8, 4]]

for i in range(len(mat1)):
    for j in range(len(mat2[0])):
        sum = 0
        for k in range(len(mat2)):
            sum += mat1[i][k] * mat2[k][j]
        print(sum, end=' ')
    print()
