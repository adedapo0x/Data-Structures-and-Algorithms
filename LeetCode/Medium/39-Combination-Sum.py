class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        Striver's video as guide here
        Approach here is a bit similar to subset problem. Each time, there are two options, include or exclude. But the difference here is that
        since an element can occur indefinite amount of time while within range of the target, we have to take account of that in our recursion. 
        So that would mean that for each element we take, we can readd that element or choose to move to the next element to consider adding
        say we have an array, [2,3,6,7], target = 7, so initially we take only 2 on left tree, leave right tree empty. for left tree, we can either retake 2 again
        since adding it still has us in range of target, or we leave it and update our index to consider taking 3, so we have either [2, 2] or [2] with a call to take 3, then repeat and repeat again

        We keep track of the elements we are considering relative to the target by subtracting each element in the temporary subsequence holder array from the target,
        so when target equals 0 we know that the sum of all the elements in the arr is target.

        Base case is if target = 0, we have found one with sum as target, another is if we have checked all indexes, in order not to go out of bounds, we return

        '''
        res = []
        def compareTarget(indx, arr, target):
            if target == 0: 
                res.append(arr[:])
                return
                
            if indx == len(candidates):
                return

            if candidates[indx] <= target:
                arr.append(candidates[indx])

                # could replace the two lines below with compareTarget(indx, arr, target + candidates[indx]), cleaner but less intuitive I suppose
                target -= candidates[indx]
                compareTarget(indx, arr, target)

                arr.pop()
                target += candidates[indx] # if we do what is in the comments to make it one line, no need for this addition, as target is the same when it returns
                # if we don't actually alter the target value
            compareTarget(indx+1, arr, target)

        compareTarget(0, [], target)
        return res
            
        