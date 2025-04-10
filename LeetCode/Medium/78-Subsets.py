class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # recursive format of doing this, here for each element there are basically two options in order to create a subsequence, 
        # we either include the element or we don't. Explanation in strivers
        res = []
        self.printSeq([], nums, 0, res)
        return res

    def printSeq(self, arr, nums, indx, res):
        n = len(nums)
        if indx == n:
            res.append(arr[:])
            return
        arr.append(nums[indx])
        self.printSeq(arr, nums, indx+1, res)
        arr.pop()
        self.printSeq(arr, nums, indx+1, res)