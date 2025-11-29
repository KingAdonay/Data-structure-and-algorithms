'''
Design a data structure that supports adding new words and finding if a string matches any previously added string

Use a trie (prefix tree) to store the words. Each node in the trie represents a character and has a dictionary of its children nodes, and an is_word flag. The search function uses depth-first search (DFS) to handle the '.' wildcard character, which can match any letter.

Time Complexity:
- addWord: O(m), where m is the length of the word being added.
- search: O(m * n) in the worst case, where m is the length of the search word and n is the number of nodes in the trie (due to the '.' wildcard).
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True

    def search(self, word: str) -> bool:

        def dfs(i, root):
            cur = root

            for j in range(i, len(word)):
                if word[j] == '.':
                    for child in cur.children.values():
                        if dfs(j+1, child):
                            return True
                    return False
                else:
                    if word[j] not in cur.children:
                        return False
                    cur = cur.children[word[j]]
                    
            return cur.is_word
            

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Example usage:
if __name__ == "__main__":
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print(wordDictionary.search("pad"))  # return False
    print(wordDictionary.search("bad"))  # return True
    print(wordDictionary.search(".ad"))  # return True
    print(wordDictionary.search("b.."))  # return True