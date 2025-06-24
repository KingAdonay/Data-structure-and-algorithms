from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # only have two baskets, each basket only holds a single type
        # selected trees must be contiguous
        baskets = {}
        max_fruits = 0
        i = 0
        for idx, fruit in enumerate(fruits):
            while len(baskets) == 2 and fruit not in baskets and i < idx:
                baskets[fruits[i]] -= 1
                if baskets[fruits[i]] == 0:
                    del baskets[fruits[i]]
                i += 1 
            
            if fruit in baskets:
                baskets[fruit] += 1
            else:
                baskets[fruit] = 1
            
            max_fruits = max(max_fruits, idx - i + 1)

        return max_fruits


# Tests
sol = Solution()
# Testcase 1:
fruits = [1,0,1,4,1,4,1,2,3]
print(sol.totalFruit(fruits) == 5)
# Testcase 2:
fruits = [0,1,2,2]
print(sol.totalFruit(fruits) == 3)
# Testcase 3:
fruits = [1,2,1]
print(sol.totalFruit(fruits) == 3)