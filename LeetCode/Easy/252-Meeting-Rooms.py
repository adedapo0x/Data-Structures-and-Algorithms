class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        Optimal approach here. so we initially sort the intervals by start time, so all we need to check are consecutive meetings to see if they overlap.
        say we have intervals of length 4 (ie i = 0 to 3), and we are at index 1, we only compare 1 and 0, there is no need to compare with 2 or 3, as since we have sorted by start
        time, if i = 0 and i = 1 do not overlap, there is no way that i = 2 is going to overlap with i = 0 so no neeed to check

        TC: O(NlogN + N) = O(NlogN)
        SC: O(1)
        """
        
        if not intervals or len(intervals) == 1:
            return True

        intervals.sort(key= lambda i: i[0])

        for i in range(1, len(intervals)):
            A = intervals[i]
            B = intervals[i - 1]

            if B[1] > A[0]:
                return False

        return True


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
        
