def solution(m, n, board):

    boardArray = [[""]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            boardArray[i][j] = (board[i][j])

    while True:
        sameTwoCharactersList = []
        for i in range(m-1):
            for j in range(n-1):
                if boardArray[i][j] == boardArray[i][j+1] and boardArray[i][j] != None: sameTwoCharactersList.append((i,j))
        
        sameFourCharatersList = []
        for i,j in sameTwoCharactersList:
            if boardArray[i][j] == boardArray[i+1][j] and boardArray[i][j]==boardArray[i+1][j+1]: sameFourCharatersList.append((i,j))
        
        if not sameFourCharatersList: break

        for i, j in sameFourCharatersList:
            boardArray[i][j], boardArray[i+1][j], boardArray[i][j+1], boardArray[i+1][j+1] = None, None, None, None
        
        for i in range(m-1,0,-1):
            for j in range(n):
                if not boardArray[i][j]: 
                    index = i 
                    while True:
                        index -= 1
                        if index >= 0 and boardArray[index][j] : 
                            boardArray[i][j] = boardArray[index][j]
                            boardArray[index][j] = None
                            break
                        if index < 0 : break
        
    return m*n - len([boardArray[i][j] for i in range(m) for j in range(n) if boardArray[i][j]])


print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"])==14)
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])==15)


'''
while True:

1. 배열을 돌면서 두 문자가 같은 곳의 index를 찾는다
sameTwoCharactersList = []
for i in range(m-1):
    for j in range(n-1):
        if board[i][j] == board[i][j+1] : sameTwoCharactersList.append((i,j))

2. 찾은 index를 돌면서 그 아래 문자도 같은지 확인한다
sameFourCharactersList = []
for i in sameTwoCharactersList:
    if board[i][j] == board[i+1][j] and board[i][j]==board[i+1][j+1] : sameFourCharactersList.append((i,j))

3. if not sameFourCharactersList: break

4. 찾은 index를 돌면서 공백으로 대치한다
newPosition = []
for i in sameFourCharactersList:
    borad[i][j], board[i+1][j], board[i][j+1], board[i+1][j+1] = " ", " ", " ", " "
    newPosition.append(" ")

5. 공백으로 대치한 곳을 문자열로 밀어넣는다
for i in range(m-1,0,-1):
    for j in range(n):
        if board[i][j] == " " : 
            board[i][j] = board[i-1][j]
            board[i-1][j] = " "

6. while --> break : m*n - len([boardArray[i][j] for i in range(m) for j in range(n) if boardArray[i][j]])
'''