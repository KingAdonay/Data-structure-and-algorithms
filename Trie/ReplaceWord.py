from typing import List

'''
    648. Replace Words
    
    Use a Trie to store the root words from the dictionary. For each word in the sentence, traverse the Trie 
    to find the shortest root that matches the prefix of the word.
    If a matching root is found, replace the word with this root; otherwise, keep the original word.
    
    Time Complexity: O(M + N * L) where M is the total length of all root words, N is the number of words in the sentence, and L is the average length of the words in the sentence.
    Space Complexity: O(M) for storing the Trie.
'''

class TrieNode:
    def __init__(self):
        self.children={}
        self.is_word=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word):
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True

    def search(self, word):
        cur = self.root
        w=''
        for c in word:
            if c not in cur.children:
                return word
            w += c
            cur = cur.children[c]
            if cur.is_word:
                return w

        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        words = sentence.split(' ')
        res = []
        for word in words:
            res.append(trie.search(word))

        return ' '.join(res)

# Testcases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))  # Output: "the cat was rat by the bat"
    print(solution.replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs"))  # Output: "a a b c"