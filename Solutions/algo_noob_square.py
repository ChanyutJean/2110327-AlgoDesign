def check(i, j, size):
    for k in range(size):
        if data[i+size-1][j+k] == '0':
            return False
    else:
        for m in range(size):
            if data[i+m][j+size-1] == '0':
                return False
        else:
            return True
def run(i, j):
    size = 1
    while True:
        if (i + size >= len(data)) or (j + size >= len(data[0])):
            return size
        size = size + 1
        if not check(i, j, size):
            return size - 1
row, column = map(int, input().split())
data = []
for i in range(row):
    data.append(input())
output = 0
for i in range(row):
    for j in range(column):
        if data[i][j] == '1':
            a = run(i, j)
            if a > output:
                output = a
print(output)
