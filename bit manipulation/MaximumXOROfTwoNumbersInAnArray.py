from typing import List

'''
    421. Maximum XOR of Two Numbers in an Array
    
    Using Trie data structure to store the binary representation of numbers.
    For each number, we try to find the number in the Trie that gives the maximum XOR, which is achieved by trying to take the opposite bit at each position.
    Time complexity is O(N), where N is the number of elements in the array.
    Space complexity is O(N).
'''

class Helper:
    @staticmethod
    def get_bit_string(num: int, min_length: int = 0):
        bits = bin(num)
        i = bits.index('b')
        return bits[i+1:].zfill(min_length)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.num = -1

class Trie:
    def __init__(self, max_len):
        self.root = TrieNode()
        self.max_len = max_len
    
    def add(self, num: int) -> None:
        cur = self.root
        bits = Helper.get_bit_string(num, self.max_len)
        
        for val in bits:
            if val not in cur.children:
                cur.children[val] = TrieNode()
            cur = cur.children[val]
        cur.num = num
    
    def search(self, num:int) -> str:
        cur = self.root

        bits = Helper.get_bit_string(num, self.max_len)

        for bit in bits:
            val = '1' if bit == '0' else '0'
            if val not in cur.children:
                val = bit
            cur = cur.children[val]
        return cur.num
            
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maxx = float('-inf')
        
        max_len = len(Helper.get_bit_string(max(nums)))

        trie = Trie(max_len)
        
        for num in nums:
            trie.add(num)
            closest_value = trie.search(num)
            
            value = closest_value ^ num
            
            maxx = max(maxx, value)
        
        return maxx

# Testcases:
solution = Solution()
print(solution.findMaximumXOR([3,10,5,25,2,8]))  # Expected output: 28
print(solution.findMaximumXOR([0]))  # Expected output: 0
print(solution.findMaximumXOR([2,4]))  # Expected output: 6
print(solution.findMaximumXOR([8,10,2]))  # Expected output: 10
print(solution.findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]))  # Expected output: 127