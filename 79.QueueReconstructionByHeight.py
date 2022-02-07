from typing import List
import heapq

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # heapq is based on array
        heap = []
        result = []

        for person in people:
            #(function) heappush: (__heap: list[_T@heappush], __item: _T@heappush) -> None
            heapq.heappush(heap, [-person[0], person[1]])
            print(heap)
        
        while heap:
            print(heap)
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        
        return result


a = Solution()
print(a.reconstructQueue(people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]))
# Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
