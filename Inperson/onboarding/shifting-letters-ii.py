class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        string = list(s)
        forward_pref = [0]*len(s)
        backward_pref = [0]*len(s)

        for start, end, direct in shifts:
            if direct == 0:
                backward_pref[start] += 1
                if end + 1< len(s):
                    backward_pref[end+1] -= 1
            else:
                forward_pref[start] += 1
                if end + 1 <len(s):
                    forward_pref[end+1] -= 1
        fs, bs = 0,0
        for i in range(len(s)):
            fs += forward_pref[i]
            bs += backward_pref[i]
            shift = fs - bs

            curr_ord = ord(string[i])
            curr_ord = (curr_ord - 97 + shift) % 26 + 97
            string[i] = chr(curr_ord)
            
        return "".join(string)




    
                


            