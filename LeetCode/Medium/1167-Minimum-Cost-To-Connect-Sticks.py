import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        '''
        Here to get the cost, we put the lengths in a minheap in order to be able to get the smallest lengths that we currently have with a better TC
        joining sticks together using the smallest lengths give us the minimum cost

        TC: O(NlogN)
        '''
        heap = []

        for stick in sticks:
            heapq.heappush(heap, stick)

        cost = 0
        while len(heap) > 1:  
            stick1 = heapq.heappop(heap)
            stick2 = heapq.heappop(heap)

            cost += stick1 + stick2

            heapq.heappush(heap, stick1 + stick2)

        return cost