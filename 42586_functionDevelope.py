def solution(progresses, speeds):
    answer = []
    leftDates = []

    for i in range(len(progresses)):
        leftDate = 0 
        leftWork = 100-progresses[i]  
        if leftWork % speeds[i] != 0: leftDate = leftWork / speeds[i] + 1
        else: leftDate = leftWork / speeds[i]
        leftDates.append(int(leftDate))
    
    while leftDates:
        index, popCount = leftDates.index(leftDates[0]), 0
        if len(leftDates) <= 1 :
            answer.append(1)
            break
        while True:
            if index <= len(leftDates)-1 and leftDates[0] >= leftDates[index]: 
                index +=1
                continue
            break   
        while index > 0:
            leftDates.pop(0)
            popCount += 1
            index -= 1
        answer.append(popCount)

    return answer

print(solution([93, 30, 55], [1, 30, 5])==[2, 1])
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])==[1, 3, 2])
print(solution([85, 88, 87],[1, 1, 1])==[3])