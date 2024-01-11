class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        if n <= 3:
            if len(set(fruits)) == 3:
                return 2
            else:
                return n
        left = 0    #2 1 2 2 2 3 3 4
        right = 1
        s = set()
        s.add(fruits[left])
        s.add(fruits[right])
        right += 1
        ans = 2

        while right < n:
            s.add(fruits[right])
            if len(s) > 2:
                prev_num =  fruits[right-1]
                a, b , c = s
                if a != prev_num and a != fruits[right]:
                    s.remove(a)
                elif b != prev_num and b != fruits[right]:
                    s.remove(b)
                else:
                    s.remove(c)

                left = right - 1
                while fruits[left] == prev_num:
                    left -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans