import sys

def get_biggest_number(n, k):
    answer = -1
    len_str_n  = len(n)

    if len_str_n <= 1 or (len_str_n == 2 and n[1] == '0'): return -1
    if k == 0: return n

    visited = [[False for _ in range(11)] for _ in range(1000001)]
    q = []
    q.append([[num for num in n], 0])
    visited[int(n)][0] = True

    while q: 
        num, depth = q.pop()

        if depth == int(k):
            answer = max(answer, int("".join(num)))
            continue
        
        for i in range(len_str_n):
            for j in range(i+1, len_str_n):
                if i == 0 and num[j] == '0': continue

                temp = num[i]
                num[i] = num[j]
                num[j] = temp

                num_int = int("".join(num))

                if not visited[num_int][depth+1]:
                    visited[num_int][depth+1] = True
                    q.append([num.copy(), depth+1])
                
                temp = num[i]
                num[i] = num[j]
                num[j] = temp
    
    return answer


if __name__ == "__main__":
    n, k  = sys.stdin.readline().split()
    print(get_biggest_number(n, k))
