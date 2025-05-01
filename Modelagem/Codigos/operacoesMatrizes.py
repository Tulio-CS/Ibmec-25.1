import numpy as np

# Matrizes fornecidas
A = np.array([[4, 7], [1, 2], [5, 6]])         # 3x2
B = np.array([[4, 3, 7], [1, 2, 7], [2, 0, 4]]) # 3x3
C = np.array([[3], [6], [1]])                  # 3x1
D = np.array([[9, 4, 3, -6], [2, -1, 7, 5]])    # 2x4
E = np.array([[1, 5, 8], [7, 2, 3], [4, 0, 6]]) # 3x3
F = np.array([[3, 0, 1], [1, 7, 3]])            # 2x3
I = np.identity(3)                              # 2x2


# Operações
print("1. E + B:")
try:
    print(E + B)
except ValueError as err:
    print("Erro:", err)

print("\n2. A + F:")
try:
    print(A + F)
except ValueError as err:
    print("Erro:", err)

print("\n3. B - E:")
try:
    print(B - E)
except ValueError as err:
    print("Erro:", err)

print("\n4. 7 * B:")
print(7 * B)

print("\n5. E x B (multiplicação matricial):")
try:
    print(np.dot(E, B))
except ValueError as err:
    print("Erro:", err)

print("\n6. C Transposta:")
print(C.T)

print("\n7. B x A:")
try:
    print(np.dot(B, A))
except ValueError as err:
    print("Erro:", err)

print("\n8. D Transposta:")
print(D.T)

print("\n9. A x C:")
try:
    print(np.dot(A, C))
except ValueError as err:
    print("Erro:", err)

print("\n10. I x B:")
try:
    print(np.dot(I, B))
except ValueError as err:
    print("Erro:", err)

print("\n11. E.T x E:")
print(np.dot(E.T, E))

print("\n12. C.T x C:")
print(np.dot(C.T, C))
