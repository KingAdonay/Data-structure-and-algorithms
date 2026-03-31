from typing import List

'''
    275. H-Index II
    
    Use binary search to find the largest h such that there are at least h papers with at least h citations.
    
    Inutition: 
    - If citations[mid] < n - mid, it means there are not enough papers with at least citations[mid] citations, so we need to search in the right half.
    - If citations[mid] > n - mid, it means there are more than enough papers with at least citations[mid] citations, so we can search in the left half to find a potentially larger h.
    - If citations[mid] == n - mid, it means we have found the exact h-index, so we can return it immediately.
    
    - If exact h-index is not found, the largest h will be the number of papers that have at least h citations, which is n - left after the loop ends,
    since left will be at the position where citations[left] is just greater than the last h found.
    
    Time Complexity: O(log(n)) since we perform binary search on the sorted citations array
    Space Complexity: O(1) since we only use a constant amount of extra space
'''

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2

            if citations[mid] == n - mid:
                return citations[mid]

            if citations[mid] < n - mid:
                left = mid + 1
            else:
                right = mid - 1
        
        # left is last valid h plus 1
        return n - left


# Testcases
sol = Solution()
# Testcase 1: citations = [0,1,3,5,6] -> 3
citations1 = [0,1,3,5,6]
print(sol.hIndex(citations1) == 3)
# Testcase 2: citations = [1,2,100] -> 2
citations2 = [1,2,100]
print(sol.hIndex(citations2) == 2)
# Testcase 3: citations = [0,0,0] -> 0
citations3 = [0,0,0]
print(sol.hIndex(citations3) == 0)  
# Testcase 4: citations = [1,1,3] -> 1
citations4 = [1,1,3]
print(sol.hIndex(citations4) == 1)  