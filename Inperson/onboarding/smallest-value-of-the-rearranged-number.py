class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > -10 and num < 10:
            return num
            
        negative = False
        if num < 0:
            negative = True
            num *= -1
        s = str(num)
        if negative:
            numstr =  "".join([n for n in sorted(s, reverse=True)])
            return -int(numstr)

        zeros = s.count("0")
        
        num_array = [n for n in s if n != "0"]
        num_array.sort()

    
        ans = [""]*(zeros + len(num_array))
        ans[0] =  num_array[0]

        for i in range(zeros):
            ans[i+1] = "0"

        for j in range(1, len(num_array)):
            ans[j + zeros ] += num_array[j]

        return int("".join(ans))

        