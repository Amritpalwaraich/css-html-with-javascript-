# point is an (x,y) tuple
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
    
print(transposed)
 
print(matrix[0][1])
print(matrix[1][1])
print(matrix[2][1])



 