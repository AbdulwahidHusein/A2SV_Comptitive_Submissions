class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        ans = 10**6
        left = 0
        right = 0
        curr_cards = set()

        while right < n:
            if cards[right] in curr_cards:
                while cards[left] != cards[right]:
                    curr_cards.remove(cards[left])
                    left += 1
                ans = min(ans, right - left + 1)
                left += 1

            curr_cards.add(cards[right])
            right += 1
        return ans if ans < 10**6 else -1