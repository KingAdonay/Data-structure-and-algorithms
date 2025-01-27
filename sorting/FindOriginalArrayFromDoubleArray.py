from typing import List

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 != 0:
            return []

        changed.sort()

        dictt = {}
        for idx, num in enumerate(changed):
            if num in dictt:
                dictt[num].add(idx)
            else:
                dictt[num] = {idx}

        doubles_idx = set()

        originals = []

        i = 0
        while i < n:
            if i in doubles_idx:
                i += 1
                continue
            
            original = changed[i]
            double = original * 2
            if double in dictt and len(dictt[double]) > 0:
                idx = dictt[double].pop()
                if idx == i:
                    if len(dictt[double]) > 0:
                        idx = dictt[double].pop()
                    else:
                        i += 1
                        continue
                
                originals.append(original)
                doubles_idx.add(idx)
            
            i += 1

        if len(originals) == n / 2:
            return originals
        
        return []

solution = Solution()
# Tests
# Testcase 1
originalArr = solution.findOriginalArray([40,7,78,12,40,28,33,27,35,90,56,44,42,38,36,3,12,68,86,14,27,80,33,40,12,74,20,50,15,54,76,13,40,3,43,88,14,54,20,0,100,10,23,30,27,50,84,24,15,45,94,66,6,22,20,34,25,100,28,6,37,10,18,82,96,0,76,40,32,33,48,70,24,80,20,40,50,4,19,25,66,38,46,44,98,47,26,54,38,39,41,20,49,8,16,6,50,30,20,66])
expected = [0,3,3,4,6,7,10,10,12,12,13,14,15,15,16,18,19,20,20,20,20,22,23,25,25,27,27,27,28,33,33,33,34,35,37,38,38,39,40,40,41,42,43,44,45,47,48,49,50,50]
print(originalArr == expected)
# Testcase 2
originalArr = solution.findOriginalArray([1,3,4,2,6,8])
expected = [1, 3, 4]

print(originalArr == expected)