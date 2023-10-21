class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_palin(s):
            if len(s) <= 1:
                return True
            return s[1] == s[-1] and is_palin(s[1:-1])
        cleaned = ''
        for s in s:
            if s.isalpha():
                cleaned += s.lower()
        if len(cleaned) == 1:
            return True

        return is_palin(cleaned)
        