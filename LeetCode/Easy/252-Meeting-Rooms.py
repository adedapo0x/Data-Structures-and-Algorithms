class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        Bruteforce approach: we basically go through the rest of the intervals for each interval, trying to see if we have an overlap between any two

        we use the min and max trick here because we cannot just say A.end > B.start
        because take the example of [[10, 13], [14, 21], [2, 3]], when i is at 0, A = [10, 13] and when j = 2, B = [2, 3] so if we do, A.end > B.start, we get true, which is not what we want
        in this case because no overlap actually occurs. so it is better to say, if the minimum of their end times is greater than the maximum of the start times, then definitely an overlap
        occurs and we can accurately return False

        TC: O(N**2)
        SC: O(1)
        """
        if not intervals or len(intervals) == 1:
            return True

        for i in range(len(intervals)):
            A = intervals[i]
            for j in range(i+1, len(intervals)):
                B = intervals[j]

                if min(A[1], B[1]) > max(A[0], B[0]):
                    return False

        return True
        
