import collections
def solution(student, k):
    answer = 0
    old = collections.Counter(student)
    if old[1] < k: return 0

    for window in range(k, len(student)+1):
        print(f"window: {window}")
        for i in range(len(student)-window+1):
            print(f"student[{i}:{i+window}] : {student[i:i+window]}")
            old = collections.Counter(student[i:i+window])
            if old[1]==k : answer += 1
        print(f"answer :{answer}")

    return answer

print(solution([0,1,0,0],1)==6)
print(solution([0,1,0,0,1,1,0],2)==8)
print(solution([0, 1, 0],2)==0)

