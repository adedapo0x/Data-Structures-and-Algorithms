'''
Optimal approach here is to use a Trie (prefix tree). so when we initialize, we create the trie root node, so the build dict basically just goes through each word
and populates our trie setting .isEnd to true after we get to the end of each word
to search, we use DFS, takes in index to track where we are in searchWord, node for where we are in trie, and useDiff to see if we have previously found a mismatch

the base case for us to return True is if we are at the end of the word ie indx == len(searchWord), so we return either True or False here
if where we are in the trie is also the end of a word and we have previously had a mismatch (ie useDIff is true), then we return True
else we return False

so since it can match with any word in our magic dictionary, we have to go through all the trienodes for each character, if letters match, we go to the next letter and next node in the 
trie. if letters do not match, we want to make sure that we have not previously seen a mismatch, if we have and letters do not still match again, no point going further
we check for this with "if not useDiff", ie we have not to have previously seen a mismatch in that particular line of recursion, then when we now call the next dfs call, we set useDiff to True, and if
the call returns and it is True, we can then return True.

TC: for buildDict = O(N.L) where N is number of words in dictionary and L is the average length of each word
for search, we have O(26 * L) as TC, since we only allow branching once, worst case is we have a very populated trie, then we go through each 26 characters in the trie since we haven't used 
useDiff yet, so one match, 25 mismatch, then after that level, no more branching as we can only go down straight, as we are not allowed anymore mismatches, so if no match again, the loop simply ends at that level and
we return False as shown in our implementation.

SC: O(N.L)

'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class MagicDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.isEnd = True

    def search(self, searchWord: str) -> bool:
        def dfs(indx, node, usedDiff):
            if indx == len(searchWord):
                return node.isEnd and usedDiff

            ch = searchWord[indx]
            for c, child in node.children.items():
                if c == ch:
                    if dfs(indx + 1, child, usedDiff):
                        return True
                else:
                    if not usedDiff and dfs(indx+1, child, True):
                        return True

            return False

        return dfs(0, self.root, False)
    


'''
Using Pattern matching. Here since we know that there is only one mismatch allowed, we are allowed to have one wildcard
say for book, we have *ook, b*ok, bo*k, boo*, so for each position that * is in, we are allowed to have any character there
so we use a hashmap to store the wildcard patterns to the words that generated this pattern
so for book and cook, our hashmap, would be something like this
{ *ook: [book, cook], b*ok: [book], ..., c*ok: [cook]}, something like this

so whenn we get a searchWord, we try every pattern, ie making each position a wildcard and checking if we have that wildcard in our hashmap, if we do, 
we go to those words that previously generated that pattern, and we go through them, we want to make sure that our searchWord is not the same word as what is in our dictionary,
as at least one letter must have changed

so if we were given book and cook during buildDict, and we are given look as our searchWord, we can return True since look has patterrn *ook, that is also generated
by book and cook. if searchWord is cook, *ook, we have it in our hashmap, we would return True because of book also generated this pattern not because cook is in our hashmap, remember one letter
must have changed, so searchWord must be different from what we have in our hashmap

TC: for buildict, we have O(N.L^2) cos of we create a new pattern string of size L for each character in each word,
and for search, O(L.K) where K is the number of words that generated same pattern we are looking for
SC: O(N.L^2) we create O(N^L) patterns and each is of size L
'''


class MagicDictionary:
    def __init__(self):
        self.patterns = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                self.patterns[pattern].append(word)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            pattern = searchWord[:i] + "*" + searchWord[i+1:]
            if pattern in self.patterns:
                for word in self.patterns[pattern]:
                    if word != searchWord:
                        return True

        return False
        

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)