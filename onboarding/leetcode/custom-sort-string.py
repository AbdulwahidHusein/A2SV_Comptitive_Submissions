class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ori = defaultdict(lambda :27)
        for i, c in enumerate(order):
            ori[c] = i
        st = [a for a in s]
        st.sort(key = lambda x:ori[x])
        return "".join(st)