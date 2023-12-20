class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            next_num = 0
            while n > 0:
                digit = n % 10
                next_num += digit * digit
                n //= 10
            return next_num
        
        slow = n
        fast = getNext(n)

        while fast != 1 and slow != fast:
            slow = getNext(slow)
            fast = getNext(getNext(fast))

        return fast == 1