# Estudiante: Andres Eduardo Ramirez Delgado
# Tecnologias de la informacion | Primer nivel "G"

def bubble_sort(fila):
    """Ordena una fila de la matriz usando Bubble Sort."""
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila

def ordenar_fila_matriz(matriz, fila_index):
    """Ordena una fila específica de la matriz en orden ascendente."""
    if 0 <= fila_index < len(matriz):
        matriz[fila_index] = bubble_sort(matriz[fila_index])
    else:
        print("Índice de fila fuera de rango")

def main():
    matriz = [
        [5, 8, 3],
        [6, 2, 9],
        [4, 7, 1]
    ]
    print("Matriz original:")
    for fila in matriz:
        print(fila)
    
    fila_index = int(input("Ingrese el índice de la fila a ordenar (0-2): "))
    ordenar_fila_matriz(matriz, fila_index)
    
    print("\nMatriz con la fila ordenada:")
    for fila in matriz:
        print(fila)

if __name__ == "__main__":
    main()
