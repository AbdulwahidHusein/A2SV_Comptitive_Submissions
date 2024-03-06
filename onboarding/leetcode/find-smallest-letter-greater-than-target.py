class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        left = bisect_left(letters, target)
        right = bisect_right(letters, target)
        if left == n:
            return letters[0]
        if letters[left] == target and left == n-1:
            return letters[0]
        if letters[left] != target:
            return letters[left]
        if right == n:
            return letters[0]
        return letters[right]