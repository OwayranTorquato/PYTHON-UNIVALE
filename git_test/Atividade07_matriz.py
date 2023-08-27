import numpy as np

dieimes_matriz = np.array([[3,4,1],[3,2,1]])
total = 0
for linha in dieimes_matriz:
    for indice in linha:
        total += indice
print("Matriz:")
print(dieimes_matriz)
print(f"A soma dos dados presentes na matriz é: {total}")
