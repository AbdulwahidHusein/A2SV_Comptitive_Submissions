class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            l = s[left]
            r = s[right]
            if not l.isalnum() or not r.isalnum():
                if not l.isalnum():
                    left += 1
                if not r.isalnum():
                    right -= 1
            else:
                if l.lower() != r.lower():
                    print(l.lower()==r.lower())
                    return False
                left += 1
                right -= 1
        return True
                
        