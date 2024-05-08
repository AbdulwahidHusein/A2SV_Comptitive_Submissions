# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        plp = 0
        trp = 0
        matches = 0
        n1 = len(players)
        n2 = len(trainers)
        while plp < n1 and trp < n2:
            if players[plp] <= trainers[trp]:
                matches += 1
                plp += 1
            trp += 1
        return matches
                