# Problem: Node With Highest Edge Score - https://leetcode.com/problems/node-with-highest-edge-score/description/

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        idg = [0] * n

        for u, v in enumerate(edges):
            idg[v] += u
        
        res = (0, idg[0])
        for i, node_idg in enumerate(idg):
            if node_idg > res[1]:
                res = (i, node_idg)
        
        return res[0]