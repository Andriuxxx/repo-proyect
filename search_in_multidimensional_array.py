# Cambie el antiguo texto por el programa: Búsqueda en Arreglo Multidimensional
# Estudiante: Andres Eduardo Ramirez Delgado
# Tecnologias de la informacion | Primer nivel "G"

def buscar_en_matriz(matriz, valor):
    """Busca un valor en una matriz y devuelve su posición."""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"Valor encontrado en la posición: ({i}, {j})"
    return "Valor no encontrado"

def main():
    matriz = [
        [5, 8, 3],
        [6, 2, 9],
        [4, 7, 1]
    ]
    print("Matriz:")
    for fila in matriz:
        print(fila)
    
    valor = int(input("Ingrese el número a buscar: "))
    resultado = buscar_en_matriz(matriz, valor)
    print(resultado)

if __name__ == "__main__":
    main()
