'''
    190. Reverse Bits
    Reverse bits of a given 32 bits unsigned integer.
    
    Using bit manipulation:
    Iterate through each of the 32 bits of the integer. For each bit, extract it using right shift and bitwise AND, with 1.
    Place the extracted bit in its reversed position using left shift and bitwise OR.
    Finally, return the resulting integer which has the bits reversed.

    Time complexity: O(1), since the number of bits is fixed (32 bits).
    Space complexity: O(1), using a constant amount of space.
    
    Using string manipulation:
    Convert the integer to its binary string representation, ensuring it is 32 bits long by padding with leading zeros.
    Use two pointers to swap bits from the start and end of the string, moving towards the center.
    Convert the modified binary string back to an integer and return it.
    
    Time complexity: O(1), since the number of bits is fixed (32 bits).
    Space complexity: O(1), using a constant amount of space.
'''

class Solution:
    def reverseBitsAsString(self, n: int) -> int:
        b_str = list(f'{n:b}'.zfill(32))
        i, j = 0, len(b_str) - 1
       
        while i <= j:
            b_str[i], b_str[j] = b_str[j], b_str[i]
            i += 1
            j -= 1
        
        return int(''.join(b_str), 2)
        
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << 31 - i)
        
        return res
    
# Testcases:
sol = Solution()
print(sol.reverseBits(43261596) == 964176192)
print(sol.reverseBitsAsString(43261596) == 964176192)
print(sol.reverseBits(4294967293) == 3221225471)
print(sol.reverseBitsAsString(4294967293) == 3221225471)