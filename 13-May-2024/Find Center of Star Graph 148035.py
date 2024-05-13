# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return  Counter([edges[0][0], edges[0][1], edges[1][0], edges[1][1]]).most_common(1)[0][0]