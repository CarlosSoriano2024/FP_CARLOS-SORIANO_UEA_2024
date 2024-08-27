def ordenar_fila(matriz, fila):
    # Copiar la fila especificada para ordenarla
    fila_a_ordenar = matriz[fila].copy()

    # Aplicar el algoritmo de ordenación de selección
    for i in range(len(fila_a_ordenar)):
        min_idx = i
        for j in range(i+1, len(fila_a_ordenar)):
            if fila_a_ordenar[j] < fila_a_ordenar[min_idx]:
                min_idx = j
        fila_a_ordenar[i], fila_a_ordenar[min_idx] = fila_a_ordenar[min_idx], fila_a_ordenar[i]

    # Actualizar la fila en la matriz original
    matriz[fila] = fila_a_ordenar

# Definir una matriz de ejemplo
matriz = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 1, 8]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la segunda fila (índice 1)
ordenar_fila(matriz, 1)
# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:print(fila)