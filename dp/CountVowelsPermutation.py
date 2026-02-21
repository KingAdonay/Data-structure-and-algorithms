from functools import cache

'''
    1220. Count Vowels Permutation
    
    Intuition:
    We can use a recursive approach to find the number of valid strings of length n.
    We can define a mapping of which characters can follow which characters based on the rules given in the problem statement.
    Then we can use a helper function that takes in the previous character and the current size of the string being formed.
    If the size is equal to n, we can return 1 to indicate that we have found a valid string.
    Otherwise, we can iterate through the possible next characters based on the mapping and recursively call the helper function for each of those characters,
    while also incrementing the size by 1.
    We can also use memoization to store the results of previously computed states to avoid redundant calculations. That way we would only recompute
    the number of valid strings for a given previous character only when the size changes.
    
    Approach:
    1. Define a mapping of which characters can follow which characters based on the rules given in the problem statement.
    2. Define a helper function that takes in the previous character and the current size of the string being formed.
    3. If the size is equal to n, return 1 to indicate that we have found a valid string.
    4. Otherwise, iterate through the possible next characters based on the mapping and recursively call the helper function for each of those characters, while also incrementing the size by 1.
    5. Use memoization to store the results of previously computed states to avoid redundant calculations.
    6. Finally, call the helper function with the initial previous character as 's' (indicating the start of the string) and the initial size as 0, and return the result modulo 10^9 + 7.
    
    Complexity Analysis:
    Time Complexity: O(n)
    Space Complexity: O(n) due to the recursion stack and memoization storage.
'''
class Solution:
    def countVowelPermutation(self, n: int) -> int:

        mappings = {'s': ['a', 'e', 'i', 'o', 'u'], 'a': ['e'], 'e': ['a', 'i'], 'i': ['a', 'e', 'o', 'u'], 'o': ['i', 'u'], 'u': ['a']}

        @cache
        def helper(prev, size):
            if size == n:
                return 1
            
            count = 0
            for c in mappings[prev]:
                count += helper(c, size + 1)
            
            return count % (10**9 + 7)
        
        return helper('s', 0)

# Testcases:
s = Solution()
print(s.countVowelPermutation(1) == 5) # 5
print(s.countVowelPermutation(2) == 10) # 10
print(s.countVowelPermutation(5) == 68) # 68
print(s.countVowelPermutation(144) == 18208803) # 18208803

