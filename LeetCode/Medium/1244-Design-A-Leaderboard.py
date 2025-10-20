from sortedcontainers import SortedDict
class Leaderboard:
    '''
    This is an optimization of the getting top operation, in our normal queue solution we would create a queue each time then run through the scores in NlogK time
    here we optimize the top operation while sacrificing the addScore and reset operations O(1) efficiency

    we make use of a sortedDict, this is not natively supported by Python unlike other languages, so we have to import from sortedContainers. a sorted dict is like a normal dict in 
    application but here the keys are sorted in ascending order as they are added to the dict. It is efficient with its lookup, insert and remove operation in O(logN) rather than if we wanted to insert then
    call sort ourselves on the key, that would be O(NlogN) per operation.

    so since the sortedDict is in ascending order, we do the negative trick, so the largest score , say 100, we put it as -100, so it is the first in the dict
    we map the score to how many people have that score. so to add score, if the player doesn't already exist, we add to both dicts. But if the player exists in our system beforee,
    we need to get rid of the player's previous score in our sortedDict, so we reduce the number of the people with that prevScore by 1, then put the new updated score, which is 
    the sum of the prevScore and this new input score, into both our dicts
    to get top, we basically iterate through the sorted dict, for each score, we keep a count that is increasing by the total number of people that has that score
    and once we reach K we want to break and return res
    to reset, we need to update both dicts, if the score of the player is only scored by one person in the sorted dict, we can delete the key which is the score,
    but if it is scored by more than 1 player, we just decrement the number, then delete the player from our normal dict

    TC: to addScore -> O(logN), to get top -> O(K) since the loop only runs until we have gotten K scores, to reset -> O(logN)
    SC: O(N)

    '''

    def __init__(self):
        self.scores = {}
        self.sortedScores = SortedDict()
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1
        else:
            prevScore = self.scores[playerId]
            self.sortedScores[-prevScore] -= 1

            newScore = prevScore + score

            self.scores[playerId] = newScore
            self.sortedScores[-newScore] = self.sortedScores.get(-newScore, 0) + 1 

    def top(self, K: int) -> int:
        res, count = 0, 0
        for score, numbers in self.sortedScores.items():
            for _ in range(numbers):
                res += (-score) # negate back since we initially stored as -score, so --score == score
                count += 1
                if count == K:
                    break

            if count == K:
                break
        return res
        
    def reset(self, playerId: int) -> None:
        score = self.scores[playerId]
        number = self.sortedScores[-score]

        if number == 1:
            del self.sortedScores[-score]
        else:
            self.sortedScores[-score] -= 1
        del self.scores[playerId]



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