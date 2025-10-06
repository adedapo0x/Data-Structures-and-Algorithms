'''
Bruteforce is to use a list to store the words and go through the words in the list when we want to search, allowing for "." to match with anything.

The optimal approach that is implemented here uses a DFS with a trie, The trie is used to store the words to reduce the time complexity, and the DFS is used to 
handle wildcards.
the constructor and addWord is straightforward, initialize root trienode and go through each character in the word adding to it to our trie
for the search, there are two cases, when the character is an actual letter and the other when it is a wildcard, "."
for when it is a wildcard, it can match with anything so we need to go through all the trienodes that are present in the hashmap and use backtracking to check if
it is valid, to know if the element is at the end of the word we check the isEnd flag after the loop

one way we can build the dfs method intuitively is to first implement like as if we are just doing a normal search, after we get the logic down for when it is an alphabet,
we can then modify to allow for wildcards as done by neetcode

TC: O(L) to add word, for the search word, best case is if it contains just normal letters, no wildcard so it is O(L) also
but for the average case of searching we might have O(26 * L) since we might have to check the 26 possible branchings per word, in worst ever possible case, say we have 
a string like ".....a, at every possible index we can have 26 checks so that is leading to exponential since for every wildcard we have to check 26 branches at that level
so we can have O(26^k * L), where K is the number of wildcards (we use 26 here since we are only dealing with letters)

SC: O(N * L) for the trie, where N is the number of words and L is the average length of each word
and also, O(L) for our max recursion space
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(indx, root):
            curr = root
            for i in range(indx, len(word)):
                ch = word[i]
                if ch == ".":
                    for val in curr.children.values():
                        if dfs(i+1, val):
                            return True
                    return False
                else:
                    if ch not in curr.children:
                        return False
                    curr = curr.children[ch]
            return curr.isEnd 
        return dfs(0, self.root)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)