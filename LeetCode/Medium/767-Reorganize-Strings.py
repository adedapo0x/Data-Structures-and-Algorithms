class Solution:
    def reorganizeString(self, s: str) -> str:
        '''
        The approach here is to use get a count of the characters in the input string. so in order to reorganize, we need to take the most frequent character available, 
        use it then have it on hold, ie we want to pick another element before we can consider using it again. because take this example, aaab, we use a first, but a is still the most frequent after we
        decrease its count, so we need to keep it off and use another element that is the most frequent apart from that a. 

        we can use our dictionary to always get the most frequent, but that comes at a cost of O(N). In this leetcode question, the characters can only be lowercase letters so we have
        O(26) which is constant, but say in the real world scenario, we could possibly have any character, and that would give us an O(n) lookup time for each element we want to pick. 
        but there is a better data structure that does it in log(n) time, using the heap. In python, the heap is minheap, but here we need a maxheap to keep the most frequent character at the top so we do a lil
        trick of making the count, negative, so if count of a is 5 and it is the highest, then in our heapq (minheap in python), we have -5, still being the one at the top, just like we need

        so we get the most frequent, add it to the res, then put it on hold in prev, we don't want to use it again for the next round so we do not keep it in our heap.
        then we pick another element with the greatest freq, then add prev back to be considered for the next round. since our count was put in negative, we increment the count rather than decrement which is how it is 
        actually supposed to be, so once the freq of a character is zero that means we can no longer select that character, so we do not put it in prev, in order for it not to be put back into the heap in the second round.

        note that we use a list instead of a string because strings are immutable in py and what we would have been doing is copying the entire strring again and again each time there is an addition
        which can be O(N), the list way is cleaner, append in O(1) time, that concat the characters once in O(N)
        
        TC and SC: for the leetcode version of only 26 letters, TC: to get count, create maxheap and heapify is O(26) which is simply O(1)
        then the loop runs O(n) times, and in it we have log(k) heap operations going on, in this case log(26) so still constant
        so the entire TC is O(n), SC: O(26) = O(1) since characters are just lowercase letters and we do not count res that denotes the output

        but for if the characters could be anything, with our heap solution we have O(nlogK) where n is the length of characters and k is the number of unique characters
        if we used our hashmap directly it'll be O(n^2). SC here is O(N) from the freq, and heap.
        

        '''
        res = []
        freq = Counter(s)
        maxheap = [[-count, char] for char, count in freq.items() ]

        heapq.heapify(maxheap)

        prev = None
        while maxheap or prev:
            if not maxheap and prev:
                return ""

            count, char = heapq.heappop(maxheap)
            res.append(char)
            count += 1

            if prev:
                heapq.heappush(maxheap, prev)
                prev = None

            if count != 0:
                prev = [count, char]

        return "".join(res)
        