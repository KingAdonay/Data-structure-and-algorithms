'''
    1517. Minimum Non-Zero Product of an Array Elements
    
    We can use the properties of powers of 2 to find the minimum non-zero product of an array of elements from 1 to 2^p - 1.
    The maximum element in the array is 2^p - 1, and the second largest element is 2^p - 2. The minimum non-zero product can 
    be obtained by multiplying the maximum element with the second largest element raised to the power of half of the maximum
    element (which is (2^p - 1) // 2).
    
    Time Complexity: O(log m), where m is the maximum element (2^p - 1). The pow function uses modular exponentiation which runs in logarithmic time.
    Space Complexity: O(1) since we are using only a constant amount of extra space
'''

class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        maxx = 2**p-1
        mod = 10**9 + 7
        return (pow(maxx - 1, maxx // 2, mod) * maxx) % mod
    
# Testcases
# Testcase 1: p = 1 -> 1
# Testcase 2: p = 2 -> 6
# Testcase 3: p = 3 -> 1512
