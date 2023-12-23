class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        #this is the worst code i ever write
        pos1 = {}
        pos2 = {}
        for i in range(len(list1)):
            pos1[list1[i]] = i
        for i in range(len(list2)):
            pos2[list2[i]] = i
        commons = []
        for w in pos2:
            if w in pos1:
                commons.append([w, pos1[w]+pos2[w]])
        least = float("inf")
        for _, s in commons:
            least = min(s, least)
        ans = []
        for a in commons:
            if a[1] == least:
                ans.append(a[0])
        return ans
        