from typing import List

'''
    820. Short Encoding of Words
    
    In this case, we can use a trie to store the words in reverse order. This way, 
    words that are suffixes of other words will share the same path in the trie. When we finish inserting all words, 
    we can traverse the trie to find all the leaf nodes, which represent the unique words that need to be included in the encoding. 
    The length of the encoding will be the sum of the lengths of these unique words plus one for each word to account for the '#' character.
    
    Eg: words = ["time", "me", "bell"]
        Inserted in reverse order so that "me" is a suffix of "time".
    
    A node should only be marked as a word if it has no children, meaning it's not a suffix of any other word.
                
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word:str) -> None:
        cur = self.root
        for i in range(len(word) - 1, -1, -1):
            c = word[i]
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.is_word = False
        
        if not cur.children:
            cur.is_word = True
    
    def get_encoded_string_length(self) -> int:
        def dfs(node: TrieNode, count:int):
            if node.is_word:
                return count + 1
            
            res = 0
            for child in node.children.values():
                res += dfs(child, count + 1)
            
            return res
        
        return dfs(self.root, 0)

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        return trie.get_encoded_string_length()
    
# Testcases:
sol = Solution()
print(sol.minimumLengthEncoding(["time", "me", "bell"]) == 10)  # Output: 10
print(sol.minimumLengthEncoding(["t"]) == 2)
print(sol.minimumLengthEncoding(["me", "time"]) == 5)
print(sol.minimumLengthEncoding(["fe", "e", "f"]) == 5) 