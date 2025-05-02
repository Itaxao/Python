# Definição do tamanho das matrizes
matrizA = [[0 for _ in range(3)] for _ in range(3)]
matrizB = [[0 for _ in range(3)] for _ in range(3)]
matrizC = [[0 for _ in range(3)] for _ in range(3)]

# Loop para o usuário definir os valores das matrizes
print("Preencha a matriz A:")
for i in range(3):
    for j in range(3):
        matrizA[i][j] = int(input(f"Digite os valores para A: [{i}],[{j}]: "))

print("Preencha a matriz B:")
for i in range(3):
    for j in range(3):
        matrizB[i][j] = int(input(f"Digite os valores para B: [{i}],[{j}]: "))

# C[i][j] = Σ (A[i][k] * B[k][j]) para k de 0 a 2
for i in range(3):
    for j in range(3):
        for k in range(3):  # Para cada elemento da linha/coluna
            matrizC[i][j] += matrizA[i][k] * matrizB[k][j]

    
# Exibição das matrizes
def imprimir_matriz(nome, matriz):
    print(f"\n{nome}:")
    for linha in matriz:
        print(" ".join(f"{elem:3d}" for elem in linha))

imprimir_matriz("MATRIZ A", matrizA)
imprimir_matriz("MATRIZ B", matrizB)
imprimir_matriz("MATRIZ C (A × B)", matrizC)


