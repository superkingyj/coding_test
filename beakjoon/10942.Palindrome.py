import sys

def check_palindrome(n, m, array, question_list):
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for i in range(n-1):
        if array[i] == [i+1]: dp[i][i+1] = 1
    
    for i in range(2, n):
        for j in range(n-i):
            if array[j] == array[i+j] and dp[j+1][i+j-1] == 1: dp[j][i+j] = 1
    
    for i,j in question_list:
        print(dp[i-1][j-1])

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    array = []
    input = list(sys.stdin.readline().split())
    for i in range(n):
        array.append(int(input[i]))
    m = int(sys.stdin.readline())
    question_list = []
    for i in range(m):
        question = []
        input = list(sys.stdin.readline().split())
        question.append(int(input[0]))
        question.append(int(input[1]))
        question_list.append(question)
    check_palindrome(n, m, array, question_list)



'''
7 --> n
 1  2  1  3  1  2  1 --> array
-1 -2 -3 -4 -5 -6 -7
4 --> m
1 3 --> question_list
2 5 --> question_list
3 3 --> question_list
5 7 --> question_list

 v
'''