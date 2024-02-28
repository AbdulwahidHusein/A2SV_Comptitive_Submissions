class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        letters = {"2":["a","b","c"], "3":['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'],
        '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        combs = []
        def comb(s):
            nonlocal letters
            if len(s) == 1:
                return letters[s[0]]
            first_dig = s[0]
            subs = s[1:]
            arr = []
            for l in letters[first_dig]:
                for sb in comb(subs):
                    arr.append(l+sb)
            return arr
        return comb(digits)


        