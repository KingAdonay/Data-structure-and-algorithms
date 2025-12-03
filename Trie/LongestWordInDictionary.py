from typing import List

'''
    720. Longest Word in Dictionary
    
    Use a Trie to store all words. Then perform a DFS to find the longest word.
    
    Since we only want to consider words that can be built one character at a time, from a other words,
    we stop exploring a branch if we reach a node that is not marked as a word.
    
    To return the lexicographically smallest word in case of ties, we explore children in order from 'a' to 'z',
    and always update the longest word found if we find a longer one.
    To esure that we always explore the lexicographically smaller option first, we use an array to srote children
    instead of a dictionary.
    
    Time complexity: O(N * L) where N is the number of words and L is the average length of the words.
    Space complexity: O(N * L) for the Trie.
'''

class TrieNode:
    def __init__(self, value: str):
        self.children = [None] * 26
        self.value = value
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode('')
    
    def insert(self, word: str):
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not cur.children[i]:
                cur.children[i] = TrieNode(c)
            cur = cur.children[i]
        cur.is_word = True
    
    def get_longest_word(self) -> str:
        def dfs(node: TrieNode | None, longest: str) -> str:
            if node.value and not node.is_word:
                return longest
            
            lg = longest + node.value
            for child in node.children:
                if child:
                    new_lg = dfs(child, longest + node.value)
                    if len(lg) < len(new_lg):
                        lg = new_lg
            
            return lg
        
        return dfs(self.root, '')

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()

        for word in words:
            trie.insert(word)
        
        return trie.get_longest_word()
                
# Testcases:
sol = Solution()
print(sol.longestWord(["w","wo","wor","worl","world"]) == 'world')  # Output: "world"
print(sol.longestWord(["a","banana","app","appl","ap","apply","apple"]) == 'apple')  # Output: "apple" 
print(sol.longestWord(["yo","ew","fc","zrc","fcm","qm","qmo","fcmz","z","ewq","ewqz","y"]) == 'yo')  # Output: "yo" 