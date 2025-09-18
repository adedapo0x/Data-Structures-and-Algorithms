import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        The approach here is to sort the intervals based on their start times and then we use a minheap to store the end times as we come across them
        so initially if the minheap is empty, this is when the loop just starts, we need a new room. We also need a new room if the current start time is lesser than the smallest end time 
        in the heap, as that means those other meetings are still in session. so we add the end times to the heap to be able to know when they end

        in the else statement, this occurs when the start time is greater or equal to the smallest end time in the heap, here that means the meeting has ended and we are hence free to reuse that
        room and we replace the end times, (ie we remove/pop the end time of that which has finished and push the end time of the new meeting about to start which is basically what heapq.replace does)

        so at the end we return the length of the minHeap, we can say this is the number of the rooms we need cos if you notice throughout the program we add to the heap when we need a new room
        and update when we can reuse a room, we do not decrease its length throughout so this would contain the amount of rooms to accommodate all

        good follow up, is why a heap instead of a list, this is because to find the smallest end time, we would need to traverse through the entire list, which is an O(N) operation.
        this would worsen the entire program TC, heap is better since it gives us O(logN)

        TC: O(NlogN)
        SC: O(N)        
        '''
        sortedIntervals = sorted(intervals, key= lambda x: x[0])
        minHeap = []

        for interval in sortedIntervals:
            if not minHeap or interval[0] < minHeap[0]:  # we need a new room
                heapq.heappush(minHeap, interval[1])
            else:
                heapq.heapreplace(minHeap, interval[1]) # we can reuse a room

        return len(minHeap)
                

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