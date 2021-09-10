import collections
def solution(n, results):
    answer = 0
    win, lose = collections.defaultdict(set), collections.defaultdict(set)
    for result in results:
        win[result[0]].add(result[1])
        lose[result[1]].add(result[0])
    
    for i in range(1,n+1):
        for winner in lose[i]: win[winner].update(win[i])
        for loser in win[i]: lose[loser].update(lose[i])

    for i in range(1,n+1):
        if len(win[i]|lose[i]) == n-1 : answer += 1
    
    return answer

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])==2)