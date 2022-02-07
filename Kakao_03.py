import collections
import math
    
def strTimeToInt(time):
    hh, mm = time.split(":")
    hh, mm = int(hh), int(mm)
    return hh*60+mm

def solution(fees, records):
    answer = []
    inOutInfo = collections.defaultdict(list)
    for record in records:
        time, carID, state = record.split(" ")[0], record.split(" ")[1], record.split(" ")[2]
        time = strTimeToInt(time)
        inOutInfo[carID].append((state, time))

    print(inOutInfo)
    chargeInfo = []

    for key, value in inOutInfo.items():
        print(f"carID : {key}")
        charge, time, inTime, outTime = 0, 0, 0, 0
        for item in value:
            if item[0] == "IN": 
                inTime = item[1]
                print(f"{item[0]}time : {inTime}")
            else:
                if item[1] == 0: 
                    outTime = strTimeToInt("23:59")
                    print(f"{item[1]}time : {outTime}")
                else: 
                    outTime = item[1]
                    time += outTime - inTime
                    print(f"{item[0]}time : {outTime}")
        if item[0] != "OUT": 
            outTime = strTimeToInt("23:59")
            time += outTime - inTime
            print(f"{item[1]}time : {outTime}")
        if time < fees[0]: 
            charge = fees[1]
        else:
            print(math.ceil((time-fees[0])/fees[2])*fees[3])
            charge = fees[1] + math.ceil((time-fees[0])/fees[2])*fees[3]
        print(f"total time : {time}, charge : {charge}")
        chargeInfo.append((key, charge))
    
    print(sorted(chargeInfo))
    return list(item[1] for item in sorted(chargeInfo))


print(solution([180, 5000, 10, 600], 
["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])==[14600, 34400, 5000])
print(solution([120, 0, 60, 591], 
["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])==[0, 591])
print(solution([1, 461, 1, 10], ["00:00 1234 IN"])==[14841])