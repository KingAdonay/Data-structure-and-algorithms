from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 1 if citations[0] > 0 else 0

        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h = i + 1
            else:
                break
        
        return h
            

# Tests
sol = Solution()
# Testcase 1: [3,0,6,1,5], expected = 3
print(3 == sol.hIndex([3,0,6,1,5]))
# Testcase 2: [1,3,1], expected = 1
print(1 == sol.hIndex([1,3,1]))