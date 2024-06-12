# Problem: Long Pressed Name - https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = len(name)
        m = len(typed)
        if m < n:
            return False

        ptr1 = 0
        ptr2 = 0

        while ptr1 < n and ptr2 < m:
            if name[ptr1] == typed[ptr2]:
                ptr1 += 1
                ptr2 += 1
            elif ptr2 > 0 and typed[ptr2] == typed[ptr2 - 1]:
                ptr2 += 1
            else:
                return False
        if ptr1 < n:
            return False
        while ptr2 < m:
            if name[-1] != typed[ptr2]:
                return False
            ptr2 += 1

        return True
            