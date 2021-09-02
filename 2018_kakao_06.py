from typing import *

def getInitializedBoardArray(m: int, n: int, board:List[str]) -> List[List[str]]:
    boardArray = [[""]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            boardArray[i][j] = (board[i][j])
    return boardArray

def findSameTwoCharacters(m: int, n: int, boardArray: List[List[str]]) -> List[tuple]:
    sameTwoCharactersList = []
    for i in range(m-1):
        for j in range(n-1):
            if boardArray[i][j] == boardArray[i][j+1] and boardArray[i][j] != None: sameTwoCharactersList.append((i,j))
    return sameTwoCharactersList

def findSameFourCharacters(m: int, n: int, boardArray: List[List[str]]) -> List[tuple]:
    sameFourCharactersList = []
    for i,j in findSameTwoCharacters(m, n, boardArray):
        if boardArray[i][j] == boardArray[i+1][j] and boardArray[i][j]==boardArray[i+1][j+1]: sameFourCharactersList.append((i,j))
    return sameFourCharactersList

def deleteSameFourCharacters(sameFourCharatersList: List[tuple], boardArray: List[List[str]]):
    for i, j in sameFourCharatersList:
        boardArray[i][j], boardArray[i+1][j], boardArray[i][j+1], boardArray[i+1][j+1] = None, None, None, None

def moveCharactersDown(m: int, n: int, boardArray: List[List[str]]):
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

def countTotalCharacters(m: int, n: int, boardArray: List[List[str]]) -> int:
    return m*n - len([boardArray[i][j] for i in range(m) for j in range(n) if boardArray[i][j]])

# Return False When Game Cannot Continue Else Return True
def runOneStep(m, n, boardArray):
    sameFourCharatersList = findSameFourCharacters(m, n, boardArray)
    if not sameFourCharatersList: return False
    deleteSameFourCharacters(sameFourCharatersList, boardArray)
    moveCharactersDown(m, n, boardArray)
    return True

def solution(m, n, board):
    boardArray = getInitializedBoardArray(m, n, board)
    while runOneStep(m, n, boardArray): continue
    return countTotalCharacters(m, n, boardArray)


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