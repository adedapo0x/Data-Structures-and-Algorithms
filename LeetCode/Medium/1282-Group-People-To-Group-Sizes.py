class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        hashMap = defaultdict(list)
        ans = []

        for i in range(len(groupSizes)):
            hashMap[groupSizes[i]].append(i)

        for key, val in hashMap.items():
            times = len(val) // key
            l, r = 0, 1
            for i in range(times):
                ans.append(val[l * key: key * r])
                l += 1
                r += 1
        return ans
