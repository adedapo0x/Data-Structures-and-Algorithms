class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        Here we go through it in one pass and get our answwer, unlike the 3 pass own below

        Here it is either our newInterval is non-overlapping with any other and we get the position it should be by doing a check (first if statement), if that is the case
        then we can add the newInterval to the res we are building, add the rest of the intervals and return res

        or before we find the actual position, to build res, we check if the end of the interval we are in is less than the start of newInterval, so we know that 
        cannot be its position and we have to look further, so we append the intervals[i] to res, building res and continue looking

        now if the newInterval is overlapping, we want to merge it into newInterval, we cannot just append the merged interval into res immediately because we do not 
        know if it also overlaps with other intervals down the array that needs merging, so we merge overlaps, put it in newInterval and keep checking for overlaps.

        if at the end of the array, we have not returned, can be because we never found its spot or we kept on merging the ending intervals till it finished,
        then we just update the newInterval to res after the loop.

        in our implementation here, the if and elif covers if we found its non-overlapping position and need to return or if we haven't found its position and it is not overlapping(we build res here)
        the else covers when it is overlapping, the actual case is if:
        intervals[i][0] < newInterval[1] or newInterval[0] < intervals[i][1] ie if the start of one is lesser than the ending of the other

        TC: O(N) and in one pass
        SC: O(N)
        '''
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res += [newInterval] + intervals[i:]
                return res
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(intervals[i][1], newInterval[1])]
            
        res.append(newInterval)
        return res
        '''
        Here we first get what position to put the newInterval, we then put the newInterval in such a way that the intervals list is still in ascending order
        then we merge intervals should incasee there are overlapping intervals. then we return this as our element 
        

        TC: O(N + N + N) = O(N) done in three passes
        SC: O(N)
        '''
        # get the index newInterval should be in
        indx = -1
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                indx = i
                break
        
        temp = []
        if indx == -1: # if our indx didn't change, that means the newInterval should be at the end
            temp = intervals +[newInterval]
        else:
            temp = intervals[:indx] + [newInterval] + intervals[indx:] 
        

        # merge all possible overlapping intervals and return
        res = [temp[0]]

        for start, end in temp[1:]:
            recentEnd = res[-1][1]

            if start <= recentEnd:
                res[-1][1] = max(end, recentEnd)
            else:
                res.append([start, end])

        return res
