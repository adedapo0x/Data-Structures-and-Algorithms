class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
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
