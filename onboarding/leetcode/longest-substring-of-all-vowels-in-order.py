class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        _next = {'a':['a','e'], 'e':['e','i'], 'i':['i','o'], 'o':['o','u'],'u':['u']}
		
        ans, stack = 0, []
        for c in word: 
            if len(stack) == 0:
                if c == 'a':
                    stack.append(c)
                continue 
            if c in _next[stack[-1]]:
                stack.append(c)
                if c == 'u':
                    ans = max(ans, len(stack))
            else:
                stack = [] if c != 'a' else ['a']
                
        return ans