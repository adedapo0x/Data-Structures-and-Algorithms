class Leaderboard:

    '''
    Heap solution here, we keep a dictionary of ID to score, to get top, we create a heap of size K, since python gives us min heap by default, 
    as we add to the heap, once the number of elements in the heap is greater than K, we want to do heap.pop, this helps us remove the smallest score in the heap
    leaving the maximum ones, which is exactly what we want. we make sure the heap doesn't grow beyond size K, after going through all the scores, we can then
    sum up the values in the heap as our ans. to reset, we can either delete from the mapper, or we just reset to score to 0. better to delete if there are a lot of players and scores

    TC: to addScore, O(1), to get top, O(NlogK + logK) = O(NlogK), to reset is O(1)
    SC: O(N + K) N from the dictionary , K from the heap 

    another way to implement this heap is to use a maxheap, we put all of the scores in a maxheap, using the negative trick on the scores to make python minheap behave like maxheap
    then we can pop the first K elements summing them and returning that as our answer. That is more straightforward, but costlier. O(N) to get the scores to be negative in a list,
    O(N) to heapify, then O(KlogN) to pop from the heap K times. so we have O(N + klogN)

    so the approach I implemented with a minheap direct is better.
    '''
    def __init__(self):
        self.mapper = {}
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.mapper:
            self.mapper[playerId] = 0
        self.mapper[playerId] += score

    def top(self, K: int) -> int:
        heap = []

        for score in self.mapper.values():
            heapq.heappush(heap, score)
            if len(heap) > K:
                heapq.heappop(heap)
        
        res = 0
        while heap:
            res += heapq.heappop(heap)
        return res
        

    def reset(self, playerId: int) -> None:
        del self.mapper[playerId]

        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)