class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
        More optimal solution in the amount of work we actually end up doing. here our counter is to note the index that the letter occurs, not the frequency of the 
        letter as in the second solution below, 

        here, first time we come across a letter we put it and its index, if we come across the same letter again, we update its value in the hashmap to n
        where n is the length of the str, so after we can then go over the hashmap, and get the minimum value

        this works since no index is going to be n in the string, highest index we can have is n - 1 for last element, so if a character value is n, that means it is not unique

        The optimization here is that we do not need to go over the string again from scratch, as if there were a lot of duplicates, this is unnecessary work

        TC: O(N + k) = O(N) where k is the number of individual letters in the hashmap, like aaa only occurs as {a: n} in the hashmap
        SC: O(26) = O(N)
        '''
        counter = {}
        n = len(s)
        for i in range(len(s)):
            if s[i] not in counter:
                counter[s[i]] = i
            else:
                counter[s[i]] = n

        ans = n
        for val in counter.values():
            ans = min(ans, val)

        return -1 if ans == n else ans



        # TC: O(2N) = O(N), SC: O(26) which is constant time, because the string can only consist of the lowercase letters which are 26 in number
        mapCount = {}

        for ch in s:
            mapCount[ch] = mapCount.get(ch, 0) + 1

        for i in range(len(s)):
            if mapCount[s[i]] == 1:
                return i

        return -1
            