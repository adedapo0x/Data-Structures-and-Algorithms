class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        Approach is from Striver's video. At each level of recursion, we try to avoid duplicates.
        TC: O(n * 2^n), SC: O(k) where k is average length of combination if we are ignoring stack space
        we also ignore the nlogn gotten by sorting since it is smaller to the 2^n complexity 
        '''
        candidates.sort()
        res = []
        def dfs(indx, temp, target):
            if target == 0:
                res.append(temp[:])
                return
            for i in range(indx, len(candidates)):
                if i > indx and candidates[i] == candidates[i-1]:
                    continue 
                if candidates[i] > target:
                    break
 
                temp.append(candidates[i])
                dfs(i+1, temp, target - candidates[i])
                temp.pop()
        dfs(0, [], target)
        return res
    

        # Brute force approach, works but gets TLE on Leetcode
        # Similar code to Combination 1, but since we can't repeat same index here, we change the initial recursion call to index and to deal with 
        # duplicates we make use of a set. a tuple to wrap our temp since a list cannot be added to a set as it is mutable.
        # TC: O(n * 2^n) 
        candidates.sort()
        res = set()
        def dfs(indx, temp, total):
            if total == target:
                res.add(tuple(temp[:]))
                return
            if indx == len(candidates) or total > target:
                return

            temp.append(candidates[indx])
            dfs(indx+1, temp, total + candidates[indx])
            temp.pop()
            dfs(indx+1, temp, total)

        dfs(0, [], 0)
        ans = [list(combination) for combination in res]
        return ans
