rows= 3
cols =3
matrix = []

for i in range(rows):
    row = list(map(int,input().split()))
    matrix.append(row)

for i in range(rows):
    for j in range(cols):
        matrix[i][j]*=3
        print(matrix[i][j], end=" ")
    print()