class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # basically same greedy approach solution as 455 (Assign cookies)
        m = n = 0

        players.sort()
        trainers.sort()

        while m < len(players) and n < len(trainers):
            if players[m] <= trainers[n]:
                m += 1
            n += 1

        return m        


       
        

