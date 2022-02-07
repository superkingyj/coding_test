import sys

def mul_matrix(N, matrix1, matrix2):
    result_matrix = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
            result_matrix[i][j] %= 1000
    return result_matrix

def power(N, B, matrix):
    if B == 1:
        result_matrix = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N): 
            for j in range(N):
                result_matrix[i][j] = matrix[i][j] % 1000
        return result_matrix
    elif B == 2:
        return mul_matrix(N, matrix, matrix)
    else: 
        temp= power(N, B//2, matrix)
        if B % 2: 
            return mul_matrix(N, mul_matrix(N, temp, temp), matrix)
        else:
            return mul_matrix(N, temp, temp)

def solve(N, B, matrix):
    result_matrix = power(N, B, matrix)
    for row in result_matrix:
        for num in row:
            print(num, end=" ")
        print()

if __name__ == "__main__":
    N, B = map(int, sys.stdin.readline().split())
    matrix =  [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        input = list(sys.stdin.readline().split())
        for j in range(len(input)):
            matrix[i][j] = int(input[j])

    solve(N,B,matrix)