def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    det = 0
    for column in range(n):
        sign = (-1) ** column
        minor = [row[:column] + row[column+1:]
    for row in matrix[1:]]
        det += sign * matrix[0][column] * determinant(minor)
    return det
def trace(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))
def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
def cofactor(matrix):
    n = len(matrix)
    cof = []
    for i in range(n):
        row = []
        for j in range(n):
            minor = [r[:j] + r[j+1:] for r in (matrix[:i] + matrix[i+1:])]
            row.append(((-1) ** (i + j)) * determinant(minor))
        cof.append(row)
    return cof
def adjoint(matrix):
    return transpose(cofactor(matrix))
dimension = int(input("Enter the order of the square matrix: "))
print("Enter the elements row-wise (space separated):")
matrix = []
for _ in range(dimension):
    row = list(map(int, input().split()))
    if len(row) != dimension:
        raise ValueError("Each row must have exactly ",dimension,"elements.")
    matrix.append(row)
detA = determinant(matrix)
transposeA = transpose(matrix)
traceA = trace(matrix)
cofactorA = cofactor(matrix)
adjointA = adjoint(matrix)
print("Determinant of matrix =", detA)
print("Transpose of matrix =")
for row in transposeA:
    print(row)
print("Trace of matrix  =", traceA)
print("Cofactor Matrix =", cofactorA)
print("Adjoint matrix = ", adjointA)
