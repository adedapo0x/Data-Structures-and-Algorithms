class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        The approach here is that we always want to pick the one with maximum frequency each time in order for us to get the minimum number of CPU intervals, but whateverr
        we pick must not be available until after n intervals. you can try with examples to see that we must use the more frequent one
        
        so we take count of the characters, and we need a maxheap, python only provides native minheap, so we do the negative trick with the numbers to get the one that is biggest to be at the
        top of the heap. and we only need to store the frequencies in the heap since we do not need the letters themselves

        each time our loop runs that is an interval and we increase the time by one, after popping from the heap, we increment since we stored negative counts, and we store it in a queue in order to keep it until it can be used again 
        and hence put back in the heap. we store the [count, time + n], the time + n is the time whereby we can put that value back in the heap, so each time we run we check if we have something in the queue due to be put in the heap
        we only need to check the first element cos it is going to have the least time + n value in the entire queue. so when it is time, we add it back to the queue and can now use it in the next loop as specified by the question
        we keep our loop running as long as there is still something to be processed in either the maxheap or the queue

        TC: to get freq = O(n), heapify = O(n) or O(26) since the question says only capital letters in tasks. then we go for each element which is O(n) and each loop
        we have heap operations log(k) where k is the number of unique characters but in this case log(26) so it is constant. 
        we can say the loop runs for O(n + idleTimes) but the heap operations only happen during the n times not during idle times and we have O(mlogk)
        so for our leetcode question TC = O(m) since log(26) becomes constant
        but for general usecase where the tasks could be anything, we have O(nlogK)

        sc: O(1) since we have at most 26 characters
        would have been O(k) if we had any possible characters where k is the number of unique characters
        '''
        freq = Counter(tasks)
        maxheap = [ -count for count in freq.values() ]
        heapq.heapify(maxheap)

        queue = deque()
        time = 0

        while maxheap or queue:
            time += 1
            if maxheap:
                count = heapq.heappop(maxheap)
                count += 1
                if count != 0:
                    queue.append([count, time + n])

            if queue:
                if queue[0][1] == time:
                    count, _ = queue.popleft()
                    heapq.heappush(maxheap, count)

        return time