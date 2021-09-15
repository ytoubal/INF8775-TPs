#Inspired by https://stackoverflow.com/a/10508133
# 2D array initialisation https://stackoverflow.com/a/44382900
def multiply(matrix1, matrix2):
    N = len(matrix1)
    result = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    #print(result)
    return result