from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 숫자 로그와 문자 로그 분리
        charLog, numLog = [],[]
        for log in logs :
            if "".join(log.split()[1:]).isalpha() : charLog.append(log)
            else : numLog.append(log)
        
        charLog.sort(key = lambda log : (log.split()[1:], log.split()[0]))

        return charLog + numLog

a = Solution()
print(a.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))