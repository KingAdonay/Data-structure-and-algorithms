'''
208. Implement Trie (Prefix Tree)

# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.
# There are various applications of this data structure, such as autocomplete and spellchecker.

A trie node contains the children of the node and a boolean flag to indicate if the node represents a complete word (Terminal node).
The key for a node is the character it represents.

Time complexity:
- Insertion: O(m), where m is the length of the word being inserted.
- Search: O(m), where m is the length of the word being searched.
- Prefix Search: O(m), where m is the length of the prefix being searched.

'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return curr.is_word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)