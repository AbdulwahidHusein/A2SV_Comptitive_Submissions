class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        ac = palindrome.count("a")
        if ac == n or ac == n-1:
            return "".join([palindrome[i] for i in range(n-1)]) + "b"

        ind = 0
        for i in range(n):
            if palindrome[i] != 'a':
                ind = i
                break
        ans = []
        for i in range(n):
            if i != ind:
                ans.append(palindrome[i])
            else:
                ans.append("a")
        return "".join(ans)
        
