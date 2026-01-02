'''
    2220. Minimum Bit Flips to Convert Number
    
    Use bit manipulation to determine the minimum number of bit flips required to convert one integer to another.
    A bit flip is defined as changing a bit from 0 to 1 or from 1 to 0.
    The approach involves comparing the bits of the two integers starting from the least significant bit (LSB) and counting the number of differing bits.
    
    By right-shifting both integers and comparing their LSBs, we can determine if a bit flip is needed.
    If the LSBs differ, we increment the count of bit flips and flip the LSB of the starting integer using the XOR operation.
    This process continues until both integers are equal.
    
    Time complexity: O(k), where k is the number of bits in the integers. In the worst case, we may need to compare all bits.
    Space complexity: O(1), using a constant amount of space.
'''
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count=0

        while start != goal:
            lsbs = start & 1 # least significant bit of start
            lsbg = goal & 1 # least significant bit of goal
            if lsbs != lsbg :
                count+=1
                start ^=1
                
            start = start>>1
            goal = goal>>1
        return count
    
    def minBitFlipsXOR(self, start: int, goal: int) -> int:
        '''
        Calculates the minimum number of bit flips required to convert one integer to another using XOR.
        
        After calculating the XOR of the two integers, the number of set bits in the result indicates the number of differing bits.
        Remove the rightmost set bit iteratively and count how many times this operation is performed until the result becomes zero.
        
        :param start: Number to be converted
        :type start: int
        :param goal: Number to convert to
        :type goal: int
        :return: the minimum number of bit flips required
        :rtype: int
        '''
        x = start ^ goal
        count = 0
        while x:
            count += 1
            x = x & (x - 1)
            
        return count
    

# Testcases:
sol = Solution()
print(sol.minBitFlips(10, 7) == 3)
print(sol.minBitFlips(3, 4) == 3)
print(sol.minBitFlips(0, 0) == 0)
print(sol.minBitFlipsXOR(10, 7) == 3)
print(sol.minBitFlipsXOR(3, 4) == 3)
print(sol.minBitFlipsXOR(0, 0) == 0)