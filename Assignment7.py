A = ((1, 3, 5), (2, 4, 6))
B = ()
C = ()

for i in range(len(A[0])):
    row_transpose = ()
    for j in range(len(A)):
        row_transpose += (A[j][i],)
    B += (row_transpose,)

for i in range(len(A)):
    row_ATA = ()
    for j in range(len(B[0])):
        value_ij = 0
        for k in range(len(A[0])):
            value_ij += A[i][k] * B[k][j]
        row_ATA += (value_ij,)
    C += (row_ATA,)

print("-" * 90)
print("Matrix with Tuple".center(90))
print("-" * 90)

row_A = int(input('Enter row number of the "A" matrix:'))
col_A = int(input('Enter column number of the "A" matrix:'))
print(
    'The "a{}{}" element in the "A" matrix is {}'.format(
        row_A, col_A, A[row_A - 1][col_A - 1]
    )
)
print("-" * 90)
row_B = int(input('Enter row number of the transposed "A" matrix:'))
col_B = int(input('Enter column number of the transposed "A" matrix:'))
print(
    'The "b{}{}" element in the transposed "A" matrix is {}'.format(
        row_B, col_B, B[row_B - 1][col_B - 1]
    )
)
print("-" * 90)
row_C = int(
    input('Enter row number of multiplication of matrices "A" and transpose of "A":')
)
col_C = int(
    input('Enter column number of multiplication of matrices "A" and transpose of "A":')
)
print(
    'The "c{}{}" element in multiplication of the "A" matrix and the transposed "A" matrix is {}'.format(
        row_C, col_C, C[row_C - 1][col_C - 1]
    )
)
print("-" * 90)
