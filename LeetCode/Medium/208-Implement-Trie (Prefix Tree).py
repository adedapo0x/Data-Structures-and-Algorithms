'''
Here we create our TrieNode by ourselves that represent the nodes of our prefix tree. we start all operations from the root, the first node with its
dict and isEnd of word flag, this helps us know when we get to the end of a word, or if it is just a prefix. to return True when searching we must get to the end of the word
in our trie, unlike when we are just checking for prefix.

Not too complex logic.
TC: O(m) for each operation where m is the length of the word
SC: O(n.m) where n is the number of words stored in our trie and m is the average length of each word
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.isEnd
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)