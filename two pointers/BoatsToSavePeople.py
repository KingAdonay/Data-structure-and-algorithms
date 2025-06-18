from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        boat_count = 0
        i = 0
        j = len(people) - 1
        while i <= j:
            summ = people[i] + people[j]
            if i != j and summ > limit:
                j -= 1
            else:
                j -= 1
                i += 1
            
            boat_count += 1
        
        return boat_count
    

# Tests
sol = Solution()
# Testcase 1:
print(sol.numRescueBoats([1,2],3) == 1)
# Testcase 2:
print(sol.numRescueBoats([3,2,2,1],3) == 3)
# Testcase 3:
print(sol.numRescueBoats([5,1,4,2],6) == 2)