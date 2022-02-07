def solution(N, number):
    if N == number: return 1

    numberSet = [set() for _ in range(8)]
    for index, num in enumerate(numberSet, start=1):
        num.add(int(str(N)*index))

    for i in range(1,len(numberSet)):
        for j in range(i):
            for num1 in numberSet[j]:
                for num2 in numberSet[i-j-1]:
                    numberSet[i].add(num1+num2)
                    numberSet[i].add(num1-num2)
                    numberSet[i].add(num1*num2)
                    if num2 != 0: numberSet[i].add(num1//num2)
        if number in numberSet[i]: 
            answer = i + 1
            break
    else: answer = -1
    
    return answer

print(solution(5,12)==4)
print(solution(2,11)==3)

'''
12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

11 = 22 / 2
11 = 2 * 2 * 2 + 2 + 2/2
'''

