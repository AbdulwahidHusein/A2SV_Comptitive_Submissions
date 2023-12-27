class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name_height = dict(zip(heights, names))
        n = len(heights)
        name = sorted(name_height.items(), key=lambda x:x[0], reverse=True)
        ans = []
        for n in name:
            ans.append(n[1])
        return ans