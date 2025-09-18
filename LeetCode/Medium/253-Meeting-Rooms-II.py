class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        The approach here is using two pointers. so we sort both the start time and end time to be able to look at it.
        we can visualize using a number line. since it is sorted, we have the order at which meetings start also the order at which they end, so we know if a new
        meeting wants to start and there is no free room we have to use another new room

        so we put the start time and end times in diff arrays and sort them, so since we can only decide on using new rooms whenever a meeting wants to start, our loop goes on 
        for only until we traverse to the end of start, and we use two pointers to go through start and end, s and e
        so if start[s] < end[e] that means the meeting is yet to end and we need a new room. 
        the else covers if start[s] > end[e] or start[s] == end[e]. in the case of if they are equal we want to end the meeting before starting the other, since (1, 8) and (8, 10) are considered
        not to be overlapping. and if start[s] > end[e] means a meeting is done and we need to decrement the count and shift the pointer by one

        TC: O(NlogN)
        SC: O(N)
        """
        res, count = 0, 0
        start = sorted([m[0] for m in intervals])
        end = sorted([m[1] for m in intervals])
        s, e = 0, 0

        while s < len(start):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)

        return res