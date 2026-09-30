'''
  Haz un programa que muestre por pantalla todos los años bisiestos entre el 1 y N para cualquier número entero N 
  introducido por teclado.
'''


def es_bisiesto(year):
    return (year % 4 == 0)


def main():
    n = int(input("Introduce un año: "))
    
    print(f"Años bisiestos entre 1 y {n}:")
    for year in range(1, n + 1):
        if es_bisiesto(year):
            print(year)


if __name__ == "__main__":
    main()
