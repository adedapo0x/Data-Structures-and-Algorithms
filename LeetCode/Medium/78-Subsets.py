class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # recursive format of doing this, here for each element there are basically two options in order to create a subsequence, 
        # we either include the element or we don't. Explanation in strivers
        # TC: O(n * 2 ^ n), 2 ^ n to generate all possible subset and n is the cost of copying the susbset to res
        # S: O(n * 2 ^ n), our res is of size 2 ^ n and each individual subset has worse case of being size n, so n * 2 ^ n
        # considering auxilliairy stack space used in recursion, this comes with extra cost of O(N)
        res = []
        self.printSeq([], nums, 0, res)
        return res

    def printSeq(self, arr, nums, indx, res):
        n = len(nums)
        if indx == n:
            res.append(arr[:]) # doing the arr[:] because we need the actual elements that arr has, if we do just arr, we end up storing just it's reference which would be tampered with by append and pop
            return
        arr.append(nums[indx])
        self.printSeq(arr, nums, indx+1, res)
        arr.pop()
        self.printSeq(arr, nums, indx+1, res)




class Solution:
    '''
    The iterative approach. The mindset here is that we still use the idea that for every element in the nums array, we either take or we do not take
    so here, our res starts with the empty array that is always going to be a subset. then we go through the nums array, for each num, we generate more
    subsets by adding that particular num to the current subsets we have while still keeping those initial subsets as they are, so it is still like as we do not change
    the initial subsets there, that is us not including, then when we add num to each subset there, that would be us including. so 2 choices, include or don't include

    e.g for [1,2,3]
    res = [[]]
    when num is 1, we add 1 to susbsets present, [] + [1] = [1], then we add it to res, [[], [1]], rememeber leave the initial subsets but add the num to all of the subsets in extra list created during list comprehension and include those in res
    when num is 2, res is [[], [1]] so we go through res and add 2 to each subset in our list created by list comprehension, [[2], [1, 2]], then add this to res,
    so res is [[], [1], [2], [1, 2]], when num is 3, we go through res, add 3 to each in additional list created, [[3], [1,3], [2,3], [1,2,3]]
    then we add this to res and we have a combined, [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]], and all the subsets possible are generated

    TC: O(n * 2 ^ n) cost of generating all subsets and n from cost of copying into res
    SC: O(n * 2 ^ n) similar reason as I gave for the recursive implementation. tho here, auxillary stack space is O(1)
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            res += [subset + [num] for subset in res]

        return res