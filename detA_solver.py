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

dimension = int(input("Enter the order of the square matrix: "))
print("Enter the elements row-wise (space separated):")
matrix = []
for _ in range(dimension):
    row = list(map(int, input().split()))
    if len(row) != dimension:
        raise ValueError("Each row must have exactly ",dimension,"elements.")
    matrix.append(row)
detA = determinant(matrix)
print("Determinant =", detA)