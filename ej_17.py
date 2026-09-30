'''
  Haz un programa que lea de un fichero un Sudoku, resuelto. Es decir, una tabla de 9 x 9 números enteros del 1 al 9 
  (todas las casillas están cubiertas). El programa debe decir si el sudoku está resuelto correctamente o no
'''

def leer_sudoku(nombre_archivo):
    sudoku = []

    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = list(map(int, linea.split()))
            sudoku.append(fila)

    return sudoku

def es_valido(sudoku):
    for i in range(9):
        fila = set()
        columna = set()
        cuadro = set()

        for j in range(9):
            # Verificar fila
            if sudoku[i][j] in fila:
                return False
            fila.add(sudoku[i][j])

            # Verificar columna
            if sudoku[j][i] in columna:
                return False
            columna.add(sudoku[j][i])

            # Verificar cuadro 3x3
            cuadro_x = (i // 3) * 3 + j // 3
            cuadro_y = (i % 3) * 3 + j % 3
            if sudoku[cuadro_x][cuadro_y] in cuadro:
                return False
            cuadro.add(sudoku[cuadro_x][cuadro_y])

    return True

def main():
    sudoku = leer_sudoku('sudoku.txt')

    if es_valido(sudoku):
        print("El Sudoku está resuelto correctamente.")
    else:
        print("El Sudoku no está resuelto correctamente.")

if __name__ == "__main__":
    main()