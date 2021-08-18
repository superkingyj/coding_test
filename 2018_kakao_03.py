from collections import deque

def solution(cacheSize, cities):
    cache = deque(maxlen = cacheSize)
    time = 0
    for city in cities :
        city = city.lower()
        if city in cache:
            time += 1
            cache.remove(city)
            cache.append(city)
        elif city not in cache :
            time += 5
            cache.append(city)
    return time

# def solution(cacheSize, cities)
#   loop item in cities
#       if deque empty --> insert
#           answer+=5
#       else if: deque contains item
#           answer+=1
#           del item from deque
#           insert item into deque
#       else if: deque is full, but not found
#           answer+=5
#           delete first from deque
#           insert item into deque
#       else: (deque is not full, but not found)
#           answer+=5
#           insert item into deque

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 50)
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]) == 21)
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]) == 60)
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]) == 52)
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]) == 16)
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 25)

# size : 3, output <-- [Jeju] <-- input 5
# size : 3, output <-- [Jeju, Pangyo] <-- input 10
# size : 3, output <-- [Jeju, Pangyo, Seoul] <-- input 15
# size : 3, output <-- [Pangyo, Seoul, NewYork] <-- input 20
# size : 3, output <-- [Seoul, NewYork, LA] <-- input 25

# size : 3, output <-- [Jeju] <-- input 5
# size : 3, output <-- [Jeju, Pangyo] <-- input 10
# size : 3, output <-- [Jeju, Pangyo, Seoul] <-- input 15
# size : 3, output <-- [Pangyo, Seoul, Jeju] <-- input 16
# size : 3, output <-- [Seoul, Jeju, Pangyo] <-- input 17
# size : 3, output <-- [Jeju, Pangyo, Seoul] <-- input 18
# size : 3, output <-- [Pangyo, Seoul, Jeju] <-- input 19
# size : 3, output <-- [Seoul, Jeju, Pangyo] <-- input 20
# size : 3, output <-- [Jeju, Pangyo, Seoul] <-- input 21
