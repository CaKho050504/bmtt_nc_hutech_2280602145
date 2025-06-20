x_y = input("Nhập X,Y: ")
D = [int(x) for x in x_y.split(',')]
# print(D[0]," ",D[1])
rowNum = D[0]
colNum = D[1]

A = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        A[row][col] = row*col;

print(A)