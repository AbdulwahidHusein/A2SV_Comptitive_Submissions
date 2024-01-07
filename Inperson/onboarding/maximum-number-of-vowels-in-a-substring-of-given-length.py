class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a",'e','i','o','u']
        n = len(s)

        curr_vowel = 0
        for i in range(k):
            if s[i] in vowels:
                curr_vowel += 1
        ans = curr_vowel
        left = 1
        right = k

        while right < n:
            if s[left-1] in vowels:
                curr_vowel -= 1
            if s[right] in vowels:
                curr_vowel += 1
            ans = max(ans, curr_vowel)
            left += 1
            right += 1
        ans = max(ans, curr_vowel)
        return ans