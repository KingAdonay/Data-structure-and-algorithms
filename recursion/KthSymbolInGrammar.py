class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # 0, 01, 0110, 01101001,... 

        # def getGrammar(s: str) -> str:
        #     len_of_s = len(s)
        #     s_inverse = format(~int(s, 2) & ((1 << len_of_s) - 1), f'0{len_of_s}b')
            
        #     return f"{s}{s_inverse}"
        
        # def helper(rows: int) -> str:
        #     if rows == 1 or k == 1:
        #         return '0'

        #     return getGrammar(helper(rows - 1))
        
        # return int(helper(n)[k-1])
        # 
        
        # Optimal way would be using binary search since we are guaranted to find 
        # the kth value in the final answer and by visualising it as a tree
        # 
        # Notice the pattern only changes when we change the left pointer, it always keeps the same on the left hand of the tree
        #      0
        #    0   1
        #  0  1 1  0
        # 01 10 10 01
        curr = 0

        left = 1
        right = 2 ** (n-1)
        for _ in range(n - 1):
            mid = (left + right) // 2
            if k <= mid:
                right = mid
            else:
                left = mid + 1
                curr = 0 if curr == 1 else 1
                
        return curr

# Tests
sol = Solution()
# Testcase 1:
n = 1
k = 1
expected = 0
print (expected == sol.kthGrammar(n, k))
# Testcase 2:
n = 2
k = 2
expected = 1
print (expected == sol.kthGrammar(n, k))
# Testcase 3:
n = 20
k = 20
expected = 1
print (expected == sol.kthGrammar(n, k))
# Testcase 4:
n = 30
k = 434991998
expected = 0
print (expected == sol.kthGrammar(n, k))
