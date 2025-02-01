from typing import List

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        time_to_impact = []
        for i in range(n):
            time_to_impact.append(dist[i] / speed[i])
        
        time_to_impact.sort()
        
        count = 1
        for i in range(1, n):
            if time_to_impact[i] > i:
                count += 1
            else:
                return count
            
        return n
    
# Tests
sol = Solution()
# Testcase 1:
dist = [1,1,2,3]
speed = [1,1,1,1]
eliminated = sol.eliminateMaximum(dist, speed)
print(eliminated == 1)
# Testcase 2:
dist = [3,5,7,4,5]
speed = [2,3,6,3,2]
eliminated = sol.eliminateMaximum(dist, speed)
print(eliminated == 2)
# Testcase 3:
dist = [4,3,3,3,4]
speed = [1,1,1,1,4]
eliminated = sol.eliminateMaximum(dist, speed)
print(eliminated == 3)
# Testcase 4:
dist = [1,3,4]
speed = [1,1,1]
eliminated = sol.eliminateMaximum(dist, speed)
print(eliminated == 3)
# Testcase 5:
dist = [46,33,44,42,46,36,7,36,31,47,38,42,43,48,48,25,28,44,49,47,29,32,30,6,42,9,39,48,22,26,50,34,40,22,10,45,7,43,24,18,40,44,17,39,36]
speed = [1,2,1,3,1,1,1,1,1,1,1,1,1,1,7,1,1,3,2,2,2,1,2,1,1,1,1,1,1,1,1,6,1,1,1,8,1,1,1,3,6,1,3,1,1]
eliminated = sol.eliminateMaximum(dist, speed)
print(eliminated == 7)