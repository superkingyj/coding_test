def solution(n, lost, reserve):
    reserve, lost = set(reserve) - set(lost), set(lost) - set(reserve)
    for student in reserve :
        if (student - 1) in lost :
            lost.remove(student-1)
            continue
        lost.discard(student+1) 
    return n - len(lost)

print(solution(5,[2, 4],[1, 3, 5])==5)
print(solution(5,[2, 4],[3])==4)
print(solution(3,[3],[1])==2)
print(solution(3,[3],[3])==3)
print(solution(3,[3],[])==2)
print(solution(3,[2,3],[3])==2)

# 1. lost && reserve --> 제외 : 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
# 2. for student in reserve:
# 3.     if front in lost:
# 4.        save front --> lost 제외
#           continue
# 5.     if back in lost:
# 6.        save back --> lost 제외
# 7. return n - len(lost)

'''
O 체육복 있음
X 체육복 없음

OOOO 4
XXXX 0

OOOX 1
OOXO 1
OXOO 1
XOOO 1

XOX --> SOX
OOX --> OOS

XXOO 3
XOXO 4
XOOX 4
OXXO 4
OXOX 4
OOXX 3

XXXO 1
XXOX 1
XOXX 1
OXXX 1

OOSXSOSOOOSOOOSOSXSOOSXSOOO
'''
