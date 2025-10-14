class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        Approach here is to sort the input intervals by their start time, then we have our ans array initially with the first interval.
        so the idea is that that is the start of the intervals so from there we want to check if any merges with it, since we have sorted we know that if something has a start time
        that is overlapping, it would be near the first interval

        so we go through the array from the second interval, checking if the start time for that overlaps with the most recent interval end time in our ans array,
        if it overlaps, we need to update the end time, and we take the max of both endings because either ending could be larger, we want the one with the larger ending to cover both intervals
        if they do not overlap, we simply append that interval to our ans

        TC: O(NlogN + O(N)) from sorting and iteration, so O(NlogN)
        SC: O(N) due to the output list
        '''
        intervals.sort()

        ans = [intervals[0]]

        for start, end in intervals[1:]:
            mostRecentEnd = ans[-1][1]

            if start <= mostRecentEnd:
                ans[-1][1] = max(end, mostRecentEnd)
            else:
                ans.append([start, end])

        return ans        