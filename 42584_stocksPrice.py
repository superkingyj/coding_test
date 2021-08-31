from collections import deque

def solution(prices):
    prices, answer = deque(prices), []
    while len(prices) > 1:
        stockPrice, index = prices.popleft(), 0
        for price in prices:
            if stockPrice > price: 
                index += 1
                break
            index += 1
        answer.append(index)
    answer.append(0)
    return answer

print(solution([1, 2, 3, 2, 3])==[4, 3, 1, 1, 0])