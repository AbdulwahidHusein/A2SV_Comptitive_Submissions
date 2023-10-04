class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)

        remaining_selections = len(piles) // 3
        my_piles = sum(piles[1:2*remaining_selections:2])

        return my_piles