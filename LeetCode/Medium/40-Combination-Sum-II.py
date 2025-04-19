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