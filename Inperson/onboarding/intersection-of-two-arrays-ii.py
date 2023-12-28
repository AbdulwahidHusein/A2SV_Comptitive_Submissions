class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = Counter(nums1)
        set2 = Counter(nums2)
        
        inters = list(set1 & set2)
        ret = []
        for n in inters:
            for i in range(min(set1[n], set2[n])):
                ret.append(n)

        return ret

