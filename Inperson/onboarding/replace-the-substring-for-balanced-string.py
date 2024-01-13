class Solution:
    def balancedString(self, s: str) -> int:
        def comp_dict(first, second):
            for key in first:
                if first[key] > second[key]:
                    return False
            return True
            
        c = Counter(s)
        n = len(s)
        exp = n // 4
        tobe_replaced = Counter()
        for w in c:
            if c[w] > exp:
                tobe_replaced[w] =  c[w] - exp
        if not tobe_replaced:
            return 0
        left = 0
        count = Counter()
        
        ans = 10**5

        for i in range(n):
            count[s[i]] += 1
            while tobe_replaced - count == Counter():
                ans = min(ans, i - left + 1)
                count[s[left]] -= 1
                left += 1
                
        return ans

        