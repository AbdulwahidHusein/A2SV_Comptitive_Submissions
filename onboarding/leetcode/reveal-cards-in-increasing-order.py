class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        if n == 1:
            return deck
        deck.sort()
        q = deque()
        q.append(deck.pop())
        q.append(deck.pop())
        while deck:
            if q:
                left = q.popleft()
                q.append(left)
            q.append(deck.pop())
        q.reverse()
        return q