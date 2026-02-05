from functools import cache
'''
    365. Water and jug problem
    
    DP to try all possibilities with a maximum increment of the sum the capacity of the of jugs plus the target value.
    
    
'''
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:

        @cache
        def helper(jug1, jug2, fills):
            if fills > jug1 + jug2 + target:
                return False

            if jug1 + jug2 == target or jug1 == target or jug2 == target:
                return True

            # pour
            j1, j2 = max(0, jug1 - (y - jug2)), min(y, jug2 + jug1)

            j3, j4 = min(x, jug1 + jug2), max(0, jug2 - (x - jug1))
            
            # empty either
            # transfer
            # refill either
            

            return helper(j1, j2, fills + 1) or helper(j3, j4, fills + 1) or helper(j1, 0, fills + 1) or helper(0, j2, fills + 1) or helper(j3, 0, fills + 1) or helper(0, j4, fills + 1) or helper(min(x, j2), 0, fills + 1) or helper(0, min(y, j1), fills + 1) or helper(min(x, j4), 0, fills + 1) or helper(0, min(y, j3), fills + 1) or helper(j1, y, fills + 1) or helper(x, j2, fills + 1) or helper(j3, y, fills + 1) or helper(x, j4, fills + 1)

        return helper(x,0,0) or helper(0,y,0)

# Testcases
sol = Solution()

print(sol.canMeasureWater(3,5,4) == True)
print(sol.canMeasureWater(2,6,5) == False)
print(sol.canMeasureWater(34,5,6) == True)