class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        Came up with this solution myself. After sorting so we can get the duplicates side by side, in this solution, the empty array which is a subset is not gotten from the solution
        so we cover that edgecase by including it from the beginning. Then we run the recursion knowing that from every index we can choose from index up to the last 
        element which is (n - 1) where n in length of nums as the next element. So here we run the recursions and it is as they return that we append the subsets to our res array

        TC: O(2^N * N) , 2^N since we generate 2^n subsets and N as the average length of each subset since we make a copy of each subset to append which is not a constant operation
        SC: O(2^N) for storing the O(2^N) possible subsets, if we are to consider auxilliary stack space here that is an additional SC of O(N)
        '''
        nums.sort()
        res = [[]]

        def getSubset(indx, temp):
            if indx == len(nums):
                return
            for i in range(indx, len(nums)):
                if i > indx and nums[i] == nums[i-1]:
                    continue
                temp.append((nums[i]))
                getSubset(i+1, temp)
                res.append(temp[:])
                temp.pop()

        getSubset(0, [])
        return res
