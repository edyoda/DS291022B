# 2D Array

# 1 2 3
# 4 5 6
# 7 8 9

row = int(input("Enter rows : "))
cols = int(input("Enter cols : "))

matrix = []

for i in range(row):
    rows = []
    for j in range(cols):
        element = int(input("Enter element  : "))
        rows.append(element)
    matrix.append(rows)

print(matrix)

for row in matrix:
    for element in row:
        print(element, end=' ')
    print()

# # 2 menthod
# for row in matrix:
#     row_str = ' '.join(str(x) for x in row)
#     print(row_str)


# 1 2           4 5            5 7
# 3 4           6 7            9 11