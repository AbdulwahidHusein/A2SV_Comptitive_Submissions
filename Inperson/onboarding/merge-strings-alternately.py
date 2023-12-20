class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1, ptr2 = 0,0
        length1, length2 = len(word1), len(word2)
        ans =  [""]*(length1+length2)

        while ptr1< length1 and ptr2 < length2:
            ans[ptr1+ptr2] = word1[ptr1]
            ptr1 += 1
            ans[ptr1+ptr2] = word2[ptr2]
            ptr2 += 1
        while ptr1< length1:
            ans[ptr1+ptr2] = word1[ptr1]
            ptr1 += 1
        while ptr2< length2:
            ans[ptr1+ptr2] = word2[ptr2]
            ptr2 += 1
        return "".join(ans)

        