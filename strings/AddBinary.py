'''
    67. Add Binary
    
    Use two pointer starting from the end of both strings. Add corresponding bits along with carry.
    Calculate the current bit and the new carry by using modulo and integer division by 2 respectively, because we are working in base 2.
    Prepend the current bit to the result string.
    Continue until both strings are fully traversed. If there's a remaining carry, prepend it to the start of the result.
    
    Time complexity: O(max(N, M)), where N and M are the lengths of strings a and b.
    Space complexity: O(max(N, M)), for the result string.
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        i, j, carry = len(a)-1, len(b)-1, 0
        while i >= 0 or j >= 0:
            int_i = int(a[i]) if i >= 0 else 0
            int_j = int(b[j]) if j >= 0 else 0

            total = int_i + int_j + carry
            cur = total % 2
            carry = total // 2

            ans = str(cur) + ans

            i -= 1
            j -= 1
        
        return str(carry) + ans if carry == 1 else ans
    

# Testcases:
sol = Solution()
print(sol.addBinary("11", "1") == "100")
print(sol.addBinary("1010", "1011") == "10101")
print(sol.addBinary("0", "0") == "0")
print(sol.addBinary("1111", "1111") == "11110") 