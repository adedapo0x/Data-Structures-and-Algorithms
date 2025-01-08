class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Optimal way to solve this would be to use the XOR operator (more research to be done on this)
        # TC: O(N), SC: O(1)
        XOR = 0
        for n in nums:
            XOR = XOR ^ n
        return XOR

        # Another way, loop through the list, count occurences in an hashmap, then traverse the hashmap to check for the element with one occurrence
        # TC: O(N) + O(N) = O(N), SC: O(N)
        maps = {}
        for n in nums:
            maps[n] = maps.get(n, 0) + 1

        for key, val in maps.items():
            if val != 2:
                return key 

        # Another method would have been to sort the list, then each elements that appear beside each other would be the same except for one of them, since it occurs only once
        # TC: O(NlogN) + O(N) = O(NlogN), SC: O(1)


        # Brute force solution, two loops, initial loop picks each element, second one counts the occurence of the element picked by first loop
        # TC: O(N^2), SC: O(1)
        for n in nums:
            count = 0 
            for k in nums:
                if n == k:
                    count += 1
            if count == 1:
                return n 